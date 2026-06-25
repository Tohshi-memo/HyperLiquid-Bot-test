# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T21:07:35.923601+00:00`
- Price records: `672`
- Market context records: `4760`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_1h` score `7.073` n `133` status `ready` deltaP `12.2665` edge `0.5494` maxDD `-1.674`
- `market_context_high->unknown_4h` score `6.5915` n `130` status `ready` deltaP `15.2603` edge `0.5686` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.8792` n `118` status `ready` deltaP `14.395` edge `0.2363` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4077` n `133` status `ready` deltaP `2.3085` edge `0.0219` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.4166` n `130` status `ready` deltaP `7.7064` edge `0.0638` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4197` n `130` status `ready` deltaP `7.0755` edge `0.0059` maxDD `-5.5505`
- `market_context_high->commodity_4h` score `-0.4848` n `130` status `ready` deltaP `8.9939` edge `0.0309` maxDD `-7.2409`
- `market_context_high->fx_4h` score `-0.609` n `130` status `ready` deltaP `-0.007` edge `-0.0004` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.8386` n `133` status `ready` deltaP `-0.672` edge `-0.0162` maxDD `-4.9467`
- `market_context_high->fx_1h` score `-1.1255` n `133` status `ready` deltaP `-3.6964` edge `-0.0042` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.6176` n `133` status `ready` deltaP `-3.8224` edge `-0.0089` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.4281` n `133` status `ready` deltaP `-2.3491` edge `-0.069` maxDD `-14.7975`
- `market_context_high->commodity_24h` score `-2.4314` n `118` status `ready` deltaP `17.9938` edge `0.0792` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.9727` n `133` status `ready` deltaP `-1.8831` edge `-0.0707` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.3945` n `133` status `ready` deltaP `-1.138` edge `-0.0845` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.97` n `118` status `ready` deltaP `-15.1719` edge `-0.0207` maxDD `-4.052`
- `market_context_high->crypto_alt_4h` score `-5.4268` n `130` status `ready` deltaP `2.1412` edge `-0.0429` maxDD `-48.0361`
- `market_context_high->index_24h` score `-6.655` n `118` status `ready` deltaP `-10.2431` edge `-0.1135` maxDD `-21.8234`
- `market_context_high->crypto_major_4h` score `-8.2098` n `130` status `ready` deltaP `2.9033` edge `-0.1488` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2932` n `130` status `ready` deltaP `5.6472` edge `-0.2768` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
