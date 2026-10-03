# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T17:22:33.250833+00:00`
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

- `market_context_high->unknown_1h` score `368.9636` n `50` status `ready` deltaP `12.2216` edge `30.6704` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.9606` n `50` status `ready` deltaP `12.6524` edge `24.7457` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2335` n `50` status `ready` deltaP `29.9792` edge `1.1566` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8021` n `50` status `ready` deltaP `37.4593` edge `0.8754` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.666` n `62` status `ready` deltaP `29.9575` edge `0.7376` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.5196` n `68` status `ready` deltaP `38.3339` edge `0.6414` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6372` n `68` status `ready` deltaP `27.6812` edge `0.5863` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.1197` n `50` status `ready` deltaP `16.628` edge `0.5528` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9205` n `50` status `ready` deltaP `16.7988` edge `0.5103` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6005` n `62` status `ready` deltaP `33.6362` edge `0.175` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9045` n `68` status `ready` deltaP `27.7259` edge `0.2018` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2266` n `50` status `ready` deltaP `14.2036` edge `0.2405` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0886` n `68` status `ready` deltaP `33.9132` edge `0.0575` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9474` n `68` status `ready` deltaP `13.3586` edge `0.1921` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8826` n `50` status `ready` deltaP `12.6527` edge `0.2009` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3381` n `68` status `ready` deltaP `19.6826` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0342` n `68` status `ready` deltaP `25.0969` edge `0.0172` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.5713` n `68` status `ready` deltaP `5.5565` edge `0.1458` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
