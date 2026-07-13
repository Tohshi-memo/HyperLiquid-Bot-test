# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T16:22:30.228456+00:00`
- Price records: `672`
- Market context records: `6620`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_24h` score `3.1417` n `176` status `ready` deltaP `0.5426` edge `0.5245` maxDD `-12.3047`
- `market_context_high->unknown_1h` score `2.172` n `203` status `ready` deltaP `-6.0898` edge `0.3117` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.1927` n `176` status `ready` deltaP `7.8268` edge `0.1507` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1095` n `203` status `ready` deltaP `7.4666` edge `0.0305` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.2547` n `203` status `ready` deltaP `2.6363` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.4935` n `203` status `ready` deltaP `4.7041` edge `0.0206` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.5583` n `203` status `ready` deltaP `-0.5265` edge `0.0037` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6093` n `203` status `ready` deltaP `-0.6902` edge `-0.0052` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.872` n `203` status `ready` deltaP `10.0166` edge `0.0094` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0469` n `203` status `ready` deltaP `2.1541` edge `0.0011` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1928` n `203` status `ready` deltaP `-3.6562` edge `-0.0009` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.2538` n `203` status `ready` deltaP `-0.5497` edge `-0.0076` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.4043` n `203` status `ready` deltaP `-17.5583` edge `0.2406` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.5969` n `203` status `ready` deltaP `8.433` edge `0.0705` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.6075` n `203` status `ready` deltaP `2.403` edge `-0.0009` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-2.017` n `203` status `ready` deltaP `5.2782` edge `0.0464` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.0976` n `203` status `ready` deltaP `-0.612` edge `0.0212` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-4.2138` n `176` status `ready` deltaP `-1.8953` edge `0.0445` maxDD `-15.1011`
- `market_context_high->equity_4h` score `-4.6318` n `203` status `ready` deltaP `8.3736` edge `-0.0149` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.7282` n `176` status `ready` deltaP `-7.7284` edge `-0.0012` maxDD `-9.3038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
