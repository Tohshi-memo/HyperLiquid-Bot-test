# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T11:22:28.358104+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8298`

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

- `market_context_high->unknown_4h` score `18.4324` n `136` status `ready` deltaP `-1.085` edge `1.5768` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.592` n `113` status `ready` deltaP `28.4445` edge `0.1533` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1324` n `148` status `ready` deltaP `6.7568` edge `0.0018` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0648` n `136` status `ready` deltaP `8.5724` edge `0.0081` maxDD `-0.4545`
- `market_context_high->fx_24h` score `0.0412` n `113` status `ready` deltaP `19.9668` edge `0.0294` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.3192` n `148` status `ready` deltaP `5.7695` edge `-0.0002` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3268` n `148` status `ready` deltaP `1.6548` edge `0.0118` maxDD `-1.0053`
- `market_context_high->index_24h` score `-0.4681` n `113` status `ready` deltaP `11.4768` edge `-0.0083` maxDD `-4.925`
- `market_context_high->commodity_4h` score `-0.5478` n `136` status `ready` deltaP `4.7614` edge `0.0455` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6507` n `148` status `ready` deltaP `-2.1039` edge `-0.0042` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-1.143` n `136` status `ready` deltaP `5.1112` edge `-0.0096` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3359` n `148` status `ready` deltaP `1.3514` edge `-0.0222` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1329` n `136` status `ready` deltaP `-8.4917` edge `-0.0294` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.3999` n `148` status `ready` deltaP `-2.0351` edge `-0.0655` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-2.5013` n `148` status `ready` deltaP `-3.4674` edge `-0.0491` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.6015` n `113` status `ready` deltaP `-2.0726` edge `-0.0904` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-5.5743` n `136` status `ready` deltaP `-5.4251` edge `-0.1745` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.4438` n `113` status `ready` deltaP `-3.165` edge `-0.2475` maxDD `-36.6024`
- `market_context_high->commodity_24h` score `-6.4809` n `113` status `ready` deltaP `-18.8191` edge `-0.1465` maxDD `-24.0477`
- `market_context_high->equity_4h` score `-13.0623` n `136` status `ready` deltaP `-7.5233` edge `-0.3122` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
