# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T17:07:33.382575+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4220`

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

- `market_context_high->unknown_1h` score `368.8088` n `50` status `ready` deltaP `12.0719` edge `30.6585` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.5848` n `50` status `ready` deltaP `12.5` edge `24.7154` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2491` n `50` status `ready` deltaP `29.9792` edge `1.1579` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8219` n `50` status `ready` deltaP `37.6326` edge `0.8759` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6672` n `62` status `ready` deltaP `29.9575` edge `0.7377` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.557` n `68` status `ready` deltaP `38.4864` edge `0.6435` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.701` n `68` status `ready` deltaP `27.8336` edge `0.5906` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.1571` n `50` status `ready` deltaP `16.7805` edge `0.5549` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9843` n `50` status `ready` deltaP `16.9512` edge `0.5146` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6155` n `62` status `ready` deltaP `33.8095` edge `0.1751` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9203` n `68` status `ready` deltaP `27.8784` edge `0.2021` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2506` n `50` status `ready` deltaP `14.3533` edge `0.2415` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.102` n `68` status `ready` deltaP `34.0657` edge `0.0576` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.969` n `68` status `ready` deltaP `13.5083` edge `0.1929` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9042` n `50` status `ready` deltaP `12.8024` edge `0.2017` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3381` n `68` status `ready` deltaP `19.6826` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0462` n `68` status `ready` deltaP `25.2466` edge `0.0172` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5953` n `68` status `ready` deltaP `5.7062` edge `0.1468` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5825` n `50` status `ready` deltaP `21.988` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
