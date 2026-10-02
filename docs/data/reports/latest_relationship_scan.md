# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T04:37:28.759865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6656`

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

- `market_context_high->unknown_1h` score `340.8588` n `50` status `ready` deltaP `9.5269` edge `28.3463` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0643` n `50` status `ready` deltaP `8.9939` edge `23.9454` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2455` n `68` status `ready` deltaP `39.2463` edge `1.1131` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0855` n `50` status `ready` deltaP `36.1667` edge `0.8243` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.0755` n `50` status `ready` deltaP `16.1875` edge `0.736` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9085` n `50` status `ready` deltaP `17.5427` edge `0.5291` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.8225` n `68` status `ready` deltaP `27.5021` edge `0.4837` maxDD `-4.2137`
- `market_context_high->crypto_alt_4h` score `4.7801` n `50` status `ready` deltaP `15.5793` edge `0.4238` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.4638` n `87` status `ready` deltaP `13.3954` edge `0.3337` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.2649` n `50` status `ready` deltaP `16.0903` edge `0.4975` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9009` n `50` status `ready` deltaP `32.689` edge `0.0373` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8333` n `50` status `ready` deltaP `13.7006` edge `0.1898` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8055` n `50` status `ready` deltaP `13.1557` edge `0.2124` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.0897` n `87` status `ready` deltaP `21.2766` edge `0.1019` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.2599` n `68` status `ready` deltaP `21.395` edge `0.1313` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9307` n `50` status `ready` deltaP `14.7917` edge `0.0778` maxDD `-1.2338`
- `news_risk_high->metal_24h` score `0.8927` n `68` status `ready` deltaP `7.0874` edge `0.1946` maxDD `-2.192`
- `news_risk_high->index_24h` score `0.7358` n `68` status `ready` deltaP `12.4388` edge `0.0262` maxDD `-0.4916`
- `news_risk_high->crypto_alt_1h` score `0.6932` n `99` status `ready` deltaP `6.7517` edge `0.069` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
