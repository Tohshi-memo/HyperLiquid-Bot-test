# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T08:52:29.498849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7888`

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

- `market_context_high->unknown_4h` score `39.8459` n `107` status `ready` deltaP `-1.1811` edge `3.3619` maxDD `-1.016`
- `market_context_high->unknown_1h` score `8.0724` n `114` status `ready` deltaP `4.3334` edge `0.6927` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `2.3482` n `43` status `ready` deltaP `16.8524` edge `0.3695` maxDD `-11.7971`
- `market_context_high->commodity_24h` score `0.9193` n `43` status `ready` deltaP `18.2049` edge `0.0874` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.9115` n `43` status `ready` deltaP `8.624` edge `0.1244` maxDD `-5.8084`
- `market_context_high->fx_4h` score `-0.0043` n `107` status `ready` deltaP `7.5593` edge `0.0089` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0728` n `114` status `ready` deltaP `3.4011` edge `0.0029` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5098` n `114` status `ready` deltaP `-0.2127` edge `0.009` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.5951` n `114` status `ready` deltaP `5.0688` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.637` n `114` status `ready` deltaP `-1.6914` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-0.6801` n `43` status `ready` deltaP `2.3498` edge `0.0065` maxDD `-1.0823`
- `market_context_high->commodity_4h` score `-0.8145` n `107` status `ready` deltaP `-2.0444` edge `0.0321` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.374` n `114` status `ready` deltaP `1.7124` edge `-0.0295` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8003` n `107` status `ready` deltaP `5.9679` edge `-0.0188` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0749` n `107` status `ready` deltaP `-6.2671` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.9189` n `43` status `ready` deltaP `-6.9161` edge `-0.0174` maxDD `-6.7121`
- `market_context_high->crypto_alt_1h` score `-3.0722` n `114` status `ready` deltaP `-1.9698` edge `-0.0555` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7648` n `114` status `ready` deltaP `-0.0447` edge `-0.0861` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.4072` n `43` status `ready` deltaP `-21.6086` edge `-0.1764` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-9.4302` n `107` status `ready` deltaP `-10.8075` edge `-0.2141` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
