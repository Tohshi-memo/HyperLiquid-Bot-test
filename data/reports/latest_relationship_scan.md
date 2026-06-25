# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T22:37:26.064218+00:00`
- Price records: `672`
- Market context records: `4767`
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

- `market_context_high->unknown_1h` score `7.8443` n `127` status `ready` deltaP `13.2974` edge `0.6068` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.0407` n `127` status `ready` deltaP `16.4202` edge `0.5983` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3513` n `112` status `ready` deltaP `12.8968` edge `0.2023` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.0522` n `127` status `ready` deltaP `3.9476` edge `0.0281` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.0747` n `127` status `ready` deltaP `10.175` edge `0.0448` maxDD `-4.7772`
- `market_context_high->equity_4h` score `-0.4945` n `127` status `ready` deltaP `7.0482` edge `0.0582` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.5116` n `127` status `ready` deltaP `5.7279` edge `0.0031` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5125` n `127` status `ready` deltaP `1.6384` edge `0.001` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.9895` n `127` status `ready` deltaP `0.4326` edge `-0.0086` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.0009` n `127` status `ready` deltaP `-2.2738` edge `-0.0033` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4767` n `127` status `ready` deltaP `-2.3009` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1786` n `112` status `ready` deltaP `19.7668` edge `0.0998` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2353` n `127` status `ready` deltaP `-0.5882` edge `-0.0651` maxDD `-14.0715`
- `market_context_high->crypto_major_1h` score `-3.5044` n `127` status `ready` deltaP `-2.0852` edge `-0.0948` maxDD `-24.5799`
- `market_context_high->fx_24h` score `-3.5478` n `112` status `ready` deltaP `-14.5337` edge `-0.0204` maxDD `-3.6022`
- `market_context_high->crypto_alt_1h` score `-4.2297` n `127` status `ready` deltaP `-1.6691` edge `-0.0746` maxDD `-18.6733`
- `market_context_high->crypto_alt_4h` score `-4.9813` n `127` status `ready` deltaP `4.3055` edge `-0.0249` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.0969` n `112` status `ready` deltaP `-7.5645` edge `-0.108` maxDD `-19.9714`
- `market_context_high->crypto_major_4h` score `-8.1454` n `127` status `ready` deltaP `3.7978` edge `-0.1465` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.4328` n `127` status `ready` deltaP `4.9417` edge `-0.29` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
