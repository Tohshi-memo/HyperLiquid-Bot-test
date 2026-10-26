# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T06:22:31.553070+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `22.8962` n `118` status `ready` deltaP `-2.8576` edge `1.9606` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.5773` n `112` status `ready` deltaP `28.0258` edge `0.1542` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.213` n `112` status `ready` deltaP `22.9415` edge `0.0316` maxDD `-1.2451`
- `market_context_high->fx_1h` score `0.0741` n `130` status `ready` deltaP `5.9834` edge `0.0021` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0381` n `118` status `ready` deltaP `7.2861` edge `0.0081` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3364` n `130` status `ready` deltaP `-0.4284` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3909` n `130` status `ready` deltaP `4.6614` edge `-0.002` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.6401` n `118` status `ready` deltaP `-0.2196` edge `0.0423` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6561` n `130` status `ready` deltaP `-2.029` edge `-0.0054` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6836` n `112` status `ready` deltaP `10.3175` edge `-0.0282` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.2441` n `118` status `ready` deltaP `4.2322` edge `-0.0167` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3423` n `130` status `ready` deltaP `2.158` edge `-0.0284` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1423` n `118` status `ready` deltaP `-7.7124` edge `-0.0358` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.385` n `130` status `ready` deltaP `-0.2326` edge `-0.0756` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4771` n `130` status `ready` deltaP `-1.983` edge `-0.0559` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.9622` n `112` status `ready` deltaP `-3.0506` edge `-0.1419` maxDD `-28.5819`
- `market_context_high->commodity_24h` score `-6.4455` n `112` status `ready` deltaP `-18.7004` edge `-0.1543` maxDD `-23.4568`
- `market_context_high->crypto_major_4h` score `-6.4605` n `118` status `ready` deltaP `-11.5776` edge `-0.2471` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-7.4346` n `112` status `ready` deltaP `-5.7292` edge `-0.3616` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.0591` n `118` status `ready` deltaP `-9.0534` edge `-0.3749` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
