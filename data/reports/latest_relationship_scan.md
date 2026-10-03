# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T18:22:25.210678+00:00`
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

- `market_context_high->unknown_1h` score `368.9696` n `50` status `ready` deltaP `11.9222` edge `30.6729` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `300.3378` n `50` status `ready` deltaP `12.6524` edge `24.9438` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.1192` n `50` status `ready` deltaP `29.286` edge `1.1517` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.7527` n `50` status `ready` deltaP `37.1127` edge `0.8736` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.672` n `62` status `ready` deltaP `29.9575` edge `0.7381` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4085` n `68` status `ready` deltaP `37.7242` edge `0.6362` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4636` n `68` status `ready` deltaP `27.0714` edge `0.5759` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0086` n `50` status `ready` deltaP `16.0183` edge `0.5476` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.7469` n `50` status `ready` deltaP `16.189` edge `0.4999` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.583` n `62` status `ready` deltaP `33.4629` edge `0.1747` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8461` n `68` status `ready` deltaP `27.1162` edge `0.201` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1643` n `50` status `ready` deltaP `13.7545` edge `0.2383` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.0362` n `68` status `ready` deltaP `33.3035` edge `0.0572` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8839` n `68` status `ready` deltaP `12.9095` edge `0.1898` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8191` n `50` status `ready` deltaP `12.2036` edge `0.1986` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3868` n `68` status `ready` deltaP `20.2924` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9851` n `68` status `ready` deltaP `24.4981` edge `0.0171` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6196` n `50` status `ready` deltaP `22.4371` edge `0.0118` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.509` n `68` status `ready` deltaP `5.1074` edge `0.1436` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
