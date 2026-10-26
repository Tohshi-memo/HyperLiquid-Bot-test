# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T05:37:26.411590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7254`

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

- `market_context_high->unknown_4h` score `25.1852` n `115` status `ready` deltaP `-2.8646` edge `2.1514` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.4807` n `109` status `ready` deltaP `26.7233` edge `0.1505` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1799` n `109` status `ready` deltaP `22.4547` edge `0.0306` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0004` n `127` status `ready` deltaP `5.0792` edge `0.0019` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0798` n `115` status `ready` deltaP `6.8093` edge `0.0078` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.3149` n `127` status `ready` deltaP `-0.0165` edge `0.0098` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3269` n `127` status `ready` deltaP `5.711` edge `-0.0008` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5665` n `115` status `ready` deltaP `0.9544` edge `0.0439` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5899` n `127` status `ready` deltaP `-0.9206` edge `-0.0043` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.6795` n `109` status `ready` deltaP `10.8467` edge `-0.0312` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3159` n `127` status `ready` deltaP `2.7559` edge `-0.029` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.3368` n `115` status `ready` deltaP `2.8394` edge `-0.0193` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1264` n `115` status `ready` deltaP `-7.3463` edge `-0.0362` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3519` n `127` status `ready` deltaP `0.2381` edge `-0.0745` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.4542` n `127` status `ready` deltaP `-1.6031` edge `-0.0555` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6832` n `109` status `ready` deltaP `-2.2936` edge `-0.1398` maxDD `-27.2921`
- `market_context_high->commodity_24h` score `-6.0503` n `109` status `ready` deltaP `-17.7911` edge `-0.1443` maxDD `-21.6882`
- `market_context_high->crypto_major_4h` score `-6.6165` n `115` status `ready` deltaP `-12.7784` edge `-0.2591` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-7.4225` n `109` status `ready` deltaP `-5.0459` edge `-0.3771` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-9.1767` n `115` status `ready` deltaP `-9.5149` edge `-0.3869` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
