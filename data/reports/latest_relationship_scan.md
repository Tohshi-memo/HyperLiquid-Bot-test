# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T00:37:26.577413+00:00`
- Price records: `672`
- Market context records: `5094`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `21.0114` n `79` status `ready` deltaP `27.7206` edge `1.6004` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.9161` n `113` status `ready` deltaP `4.1188` edge `0.7797` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `8.3303` n `101` status `ready` deltaP `21.3611` edge `0.654` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.6867` n `101` status `ready` deltaP `14.056` edge `0.4531` maxDD `-9.1665`
- `market_context_high->crypto_major_4h` score `2.483` n `101` status `ready` deltaP `13.3708` edge `0.4531` maxDD `-13.5793`
- `market_context_high->equity_4h` score `2.2771` n `101` status `ready` deltaP `13.3663` edge `0.2138` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.6456` n `113` status `ready` deltaP `10.3267` edge `0.0671` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.4375` n `101` status `ready` deltaP `9.8662` edge `0.0468` maxDD `-1.0893`
- `market_context_high->crypto_alt_1h` score `0.4209` n `113` status `ready` deltaP `6.2278` edge `0.1086` maxDD `-5.0257`
- `market_context_high->metal_1h` score `0.3349` n `113` status `ready` deltaP `9.2086` edge `0.0312` maxDD `-1.3057`
- `market_context_high->crypto_major_1h` score `0.3239` n `113` status `ready` deltaP `6.8663` edge `0.1203` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.0998` n `113` status `ready` deltaP `5.7522` edge `0.0131` maxDD `-0.7594`
- `market_context_high->metal_4h` score `-0.0825` n `101` status `ready` deltaP `5.3747` edge `0.0765` maxDD `-3.1662`
- `market_context_high->commodity_1h` score `-1.0675` n `113` status `ready` deltaP `-1.5871` edge `-0.0026` maxDD `-2.062`
- `market_context_high->fx_24h` score `-1.5769` n `79` status `ready` deltaP `-3.3162` edge `-0.0081` maxDD `-1.7626`
- `market_context_high->commodity_4h` score `-1.5841` n `101` status `ready` deltaP `4.9188` edge `-0.0199` maxDD `-6.5922`
- `market_context_high->fx_1h` score `-1.5994` n `113` status `ready` deltaP `-9.8379` edge `-0.0036` maxDD `-0.7944`
- `market_context_high->commodity_24h` score `-1.6636` n `79` status `ready` deltaP `7.7004` edge `0.0316` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-2.2343` n `101` status `ready` deltaP `-10.319` edge `-0.0101` maxDD `-1.9169`
- `market_context_high->metal_24h` score `-4.5114` n `79` status `ready` deltaP `-6.5995` edge `0.0111` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
