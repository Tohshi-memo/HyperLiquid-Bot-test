# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T04:07:26.564059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6630`

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

- `market_context_high->unknown_1h` score `339.4644` n `50` status `ready` deltaP `9.5269` edge `28.2301` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0655` n `50` status `ready` deltaP `8.9939` edge `23.9455` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.7579` n `70` status `ready` deltaP `39.1568` edge `1.1564` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.1011` n `50` status `ready` deltaP `36.1667` edge `0.8256` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.938` n `50` status `ready` deltaP `16.0139` edge `0.7257` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9385` n `50` status `ready` deltaP `17.5427` edge `0.5316` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7705` n `50` status `ready` deltaP `15.5793` edge `0.423` maxDD `-7.6792`
- `news_risk_high->equity_24h` score `4.1104` n `70` status `ready` deltaP `25.5804` edge `0.4722` maxDD `-4.9276`
- `news_risk_high->crypto_alt_4h` score `3.525` n `87` status `ready` deltaP `13.3954` edge `0.3388` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.3063` n `50` status `ready` deltaP `16.4375` edge `0.5005` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.8985` n `50` status `ready` deltaP `32.689` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8944` n `50` status `ready` deltaP `14.0` edge `0.1929` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8642` n `50` status `ready` deltaP `13.4551` edge `0.2153` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.2811` n `87` status `ready` deltaP `22.2736` edge `0.1112` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.3403` n `70` status `ready` deltaP `22.4454` edge `0.1346` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.0182` n `70` status `ready` deltaP `8.631` edge `0.2004` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9284` n `50` status `ready` deltaP `14.7917` edge `0.0775` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.8469` n `70` status `ready` deltaP `13.3631` edge `0.0293` maxDD `-0.4916`
- `news_risk_high->crypto_major_24h` score `0.7922` n `70` status `ready` deltaP `8.4524` edge `0.3606` maxDD `-15.8971`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
