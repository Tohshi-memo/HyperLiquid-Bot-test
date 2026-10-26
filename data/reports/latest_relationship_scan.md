# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T03:37:27.206108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.3051` n `113` status `ready` deltaP `-2.1207` edge `2.3231` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.1751` n `101` status `ready` deltaP `22.872` edge `0.137` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.0832` n `101` status `ready` deltaP `20.8642` edge `0.0288` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0645` n `113` status `ready` deltaP `7.0014` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1398` n `119` status `ready` deltaP `2.4581` edge `0.0015` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.3412` n `119` status `ready` deltaP `5.6018` edge `-0.0019` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3935` n `119` status `ready` deltaP `-1.4681` edge `0.0094` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5723` n `113` status `ready` deltaP `0.9632` edge `0.0431` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.7234` n `119` status `ready` deltaP `-3.2167` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.8038` n `101` status `ready` deltaP `9.7909` edge `-0.0401` maxDD `-4.925`
- `market_context_high->metal_4h` score `-2.0474` n `113` status `ready` deltaP `3.0893` edge `-0.0202` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1506` n `113` status `ready` deltaP `-7.7676` edge `-0.0365` maxDD `-4.3282`
- `market_context_high->crypto_major_1h` score `-2.203` n `119` status `ready` deltaP `2.1587` edge `-0.0399` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-2.7657` n `101` status `ready` deltaP `0.0962` edge `-0.0692` maxDD `-17.215`
- `market_context_high->crypto_alt_1h` score `-3.7017` n `119` status `ready` deltaP `-2.2946` edge `-0.0683` maxDD `-12.3238`
- `market_context_high->equity_1h` score `-3.931` n `119` status `ready` deltaP `-1.4203` edge `-0.0895` maxDD `-12.2891`
- `market_context_high->commodity_24h` score `-4.9478` n `101` status `ready` deltaP `-15.1024` edge `-0.1144` maxDD `-16.8733`
- `market_context_high->equity_24h` score `-7.4141` n `101` status `ready` deltaP `-2.874` edge `-0.403` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1024` n `113` status `ready` deltaP `-12.7428` edge `-0.2571` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-10.9577` n `101` status `ready` deltaP `-10.8137` edge `-0.418` maxDD `-63.5126`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
