from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data storage for NFTs
nfts = []

@app.route('/')
def home():
    return render_template('home.html', nfts=nfts)

@app.route('/nft/<int:nft_id>')
def nft_detail(nft_id):
    nft = next((nft for nft in nfts if nft['id'] == nft_id), None)
    if nft is None:
        return "NFT not found", 404
    return render_template('nft_detail.html', nft=nft)

@app.route('/list_nft', methods=['GET', 'POST'])
def list_nft():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        uri = request.form['uri']
        price = request.form['price']
        
        nft_id = len(nfts) + 1
        nft = {
            'id': nft_id,
            'name': name,
            'description': description,
            'uri': uri,
            'price': price,
            'image': 'default_image.png'  # Placeholder image
        }
        nfts.append(nft)
        return redirect(url_for('home'))
    return render_template('list_nft.html')

@app.route('/owned_nfts')
def owned_nfts_view():
    # Sample logic for owned NFTs
    owned_nfts = [nft for nft in nfts if nft.get('owner') == 'current_user']
    return render_template('owned_nfts.html', owned_nfts=owned_nfts)

if __name__ == '__main__':
    app.run(debug=True)
