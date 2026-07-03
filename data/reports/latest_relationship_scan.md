# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T07:22:30.672302+00:00`
- Price records: `672`
- Market context records: `5536`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11398`

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

- `market_context_high->equity_24h` score `4.0844` n `189` status `ready` deltaP `14.6495` edge `0.7506` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.4658` n `192` status `ready` deltaP `12.9192` edge `0.3486` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `2.2137` n `189` status `ready` deltaP `16.0797` edge `0.5313` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `1.9001` n `192` status `ready` deltaP `8.5238` edge `0.2656` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6262` n `192` status `ready` deltaP `9.2226` edge `0.2379` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5631` n `189` status `ready` deltaP `14.542` edge `0.0427` maxDD `-1.0847`
- `market_context_high->equity_1h` score `0.2388` n `192` status `ready` deltaP `7.3385` edge `0.0675` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0381` n `192` status `ready` deltaP `4.9744` edge `0.013` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2613` n `192` status `ready` deltaP `1.4066` edge `0.065` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.3364` n `192` status `ready` deltaP `3.2872` edge `0.0746` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3388` n `192` status `ready` deltaP `0.7423` edge `0.0005` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.6167` n `192` status `ready` deltaP `0.9637` edge `0.0097` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.8659` n `192` status `ready` deltaP `2.4518` edge `0.0049` maxDD `-1.4726`
- `market_context_high->index_4h` score `-1.345` n `192` status `ready` deltaP `3.5315` edge `0.0253` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.7449` n `192` status `ready` deltaP `-5.6574` edge `-0.0129` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.9527` n `189` status `ready` deltaP `12.9051` edge `0.0623` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.5408` n `192` status `ready` deltaP `-11.3313` edge `-0.0504` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.8282` n `192` status `ready` deltaP `-11.0518` edge `-0.0625` maxDD `-13.9606`
- `market_context_high->crypto_alt_24h` score `-7.2703` n `189` status `ready` deltaP `7.0437` edge `0.2169` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4117` n `189` status `ready` deltaP `-4.5387` edge `-0.1822` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
