# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T21:52:27.184731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12697`

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

- `market_context_high->unknown_24h` score `12872.2417` n `68` status `ready` deltaP `12.5102` edge `1072.6086` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `382.486` n `82` status `ready` deltaP `-5.6996` edge `31.954` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.2566` n `77` status `ready` deltaP `38.4357` edge `1.4122` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.6158` n `77` status `ready` deltaP `31.9918` edge `1.3035` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `12.3311` n `68` status `ready` deltaP `26.6442` edge `0.9327` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.8312` n `68` status `ready` deltaP `43.75` edge `0.5276` maxDD `0.0`
- `news_risk_high->equity_24h` score `7.116` n `77` status `ready` deltaP `17.776` edge `0.6151` maxDD `-5.2482`
- `news_risk_high->index_24h` score `6.493` n `77` status `ready` deltaP `45.0825` edge `0.2582` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.4904` n `77` status `ready` deltaP `32.3458` edge `0.287` maxDD `-0.6086`
- `market_context_high->index_24h` score `3.2431` n `68` status `ready` deltaP `34.712` edge `0.0782` maxDD `-0.1483`
- `market_context_high->commodity_24h` score `3.1734` n `68` status `ready` deltaP `34.661` edge `0.0469` maxDD `-0.0817`
- `risk_on_high->crypto_alt_4h` score `1.3184` n `47` status `ready` deltaP `14.2871` edge `0.1969` maxDD `-5.1832`
- `risk_on_and_context->crypto_alt_4h` score `1.3184` n `47` status `ready` deltaP `14.2871` edge `0.1969` maxDD `-5.1832`
- `market_context_high->equity_4h` score `0.1629` n `94` status `ready` deltaP `12.3021` edge `0.0374` maxDD `-2.8821`
- `risk_on_high->index_1h` score `0.0983` n `55` status `ready` deltaP `7.1339` edge `0.0004` maxDD `-0.162`
- `risk_on_and_context->index_1h` score `0.0983` n `55` status `ready` deltaP `7.1339` edge `0.0004` maxDD `-0.162`
- `news_risk_high->index_4h` score `0.066` n `82` status `ready` deltaP `6.5549` edge `0.0276` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `-0.0516` n `55` status `ready` deltaP `4.2025` edge `0.0007` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0516` n `55` status `ready` deltaP `4.2025` edge `0.0007` maxDD `-0.3081`
- `risk_on_high->equity_1h` score `-0.1718` n `55` status `ready` deltaP `8.1818` edge `0.0016` maxDD `-1.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
