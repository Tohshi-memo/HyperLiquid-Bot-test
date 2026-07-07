# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T09:07:26.884909+00:00`
- Price records: `672`
- Market context records: `5966`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11242`

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

- `news_risk_high->fx_24h` score `7.088` n `30` status `ready` deltaP `64.9306` edge `0.1578` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.1616` n `30` status `ready` deltaP `37.3611` edge `0.2016` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8442` n `30` status `ready` deltaP `39.8476` edge `0.0593` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.122` n `30` status `ready` deltaP `25.5788` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4987` n `234` status `ready` deltaP `9.4695` edge `0.1712` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.859` n `30` status `ready` deltaP `10.489` edge `0.0869` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2153` n `30` status `ready` deltaP `5.4691` edge `0.0373` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1167` n `30` status `ready` deltaP `7.5` edge `0.0222` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3915` n `30` status `ready` deltaP `1.8363` edge `-0.0258` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4013` n `244` status `ready` deltaP `4.0051` edge `0.0347` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.443` n `244` status `ready` deltaP `3.0112` edge `0.003` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.465` n `215` status `ready` deltaP `21.3364` edge `0.3141` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.5433` n `244` status `ready` deltaP `-2.1204` edge `0.0002` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6438` n `244` status `ready` deltaP `0.6307` edge `0.0046` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6717` n `244` status `ready` deltaP `-0.6234` edge `-0.0007` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.1178` n `30` status `ready` deltaP `-10.5988` edge `-0.0212` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1393` n `244` status `ready` deltaP `1.6639` edge `0.0196` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.156` n `244` status `ready` deltaP `1.6713` edge `0.0159` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4338` n `234` status `ready` deltaP `-1.1974` edge `-0.0045` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5577` n `234` status `ready` deltaP `-1.8566` edge `-0.0241` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
