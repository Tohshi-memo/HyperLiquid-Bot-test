# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T17:37:28.516580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4238`

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

- `market_context_high->unknown_1h` score `369.0152` n `50` status `ready` deltaP `12.2216` edge `30.6747` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.9944` n `50` status `ready` deltaP `12.8049` edge `24.7475` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2076` n `50` status `ready` deltaP `29.8059` edge `1.1556` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.7822` n `50` status `ready` deltaP `37.286` edge `0.8749` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.666` n `62` status `ready` deltaP `29.9575` edge `0.7376` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4882` n `68` status `ready` deltaP `38.1815` edge `0.6398` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5854` n `68` status `ready` deltaP `27.5287` edge `0.583` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0883` n `50` status `ready` deltaP `16.4756` edge `0.5512` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8687` n `50` status `ready` deltaP `16.6463` edge `0.507` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5854` n `62` status `ready` deltaP `33.4629` edge `0.1749` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8899` n `68` status `ready` deltaP `27.5735` edge `0.2016` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2087` n `50` status `ready` deltaP `14.0539` edge `0.24` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0752` n `68` status `ready` deltaP `33.7608` edge `0.0574` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9283` n `68` status `ready` deltaP `13.2089` edge `0.1915` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8635` n `50` status `ready` deltaP `12.503` edge `0.2003` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3502` n `68` status `ready` deltaP `19.835` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0222` n `68` status `ready` deltaP `24.9472` edge `0.0172` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6064` n `50` status `ready` deltaP `22.2874` edge `0.0117` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.5533` n `68` status `ready` deltaP `5.4068` edge `0.1453` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
