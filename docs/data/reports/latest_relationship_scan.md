# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T05:37:24.458516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4882`

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

- `market_context_high->unknown_1h` score `340.8468` n `50` status `ready` deltaP `9.5269` edge `28.3453` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0091` n `50` status `ready` deltaP `8.9939` edge `23.9408` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.9` n `64` status `ready` deltaP `39.0625` edge `1.0022` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0699` n `50` status `ready` deltaP `36.1667` edge `0.823` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.3179` n `50` status `ready` deltaP `16.1875` edge `0.7562` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `7.9267` n `64` status `ready` deltaP `31.7708` edge `0.5139` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `6.8413` n `50` status `ready` deltaP `17.5427` edge `0.5235` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7669` n `50` status `ready` deltaP `15.5793` edge `0.4227` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5514` n `87` status `ready` deltaP `13.3954` edge `0.341` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.1944` n `50` status `ready` deltaP `15.3958` edge `0.4931` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9033` n `50` status `ready` deltaP `32.689` edge `0.0375` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.7793` n `50` status `ready` deltaP `13.5509` edge `0.1863` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7742` n `50` status `ready` deltaP `13.3054` edge `0.2088` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `1.9517` n `87` status `ready` deltaP `21.2766` edge `0.0904` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.169` n `64` status `ready` deltaP `20.4861` edge `0.1257` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9656` n `50` status `ready` deltaP `15.3125` edge `0.0788` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8739` n `99` status `ready` deltaP `5.8913` edge `0.0898` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.6108` n `64` status `ready` deltaP `3.6458` edge `0.1814` maxDD `-2.192`
- `news_risk_high->fx_24h` score `0.4972` n `64` status `ready` deltaP `11.8056` edge `0.0178` maxDD `-0.4059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
