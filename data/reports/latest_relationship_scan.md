# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T08:37:30.706735+00:00`
- Price records: `672`
- Market context records: `5964`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `7.0531` n `30` status `ready` deltaP `64.5833` edge `0.1572` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.2278` n `30` status `ready` deltaP `37.7084` edge `0.2048` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.843` n `30` status `ready` deltaP `39.8476` edge `0.0592` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.122` n `30` status `ready` deltaP `25.5788` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4821` n `232` status `ready` deltaP `9.4723` edge `0.1698` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8497` n `30` status `ready` deltaP `10.3393` edge `0.0867` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2122` n `30` status `ready` deltaP `5.4691` edge `0.0369` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1449` n `30` status `ready` deltaP `7.1527` edge `0.0209` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.3357` n `213` status `ready` deltaP `21.6574` edge `0.3202` maxDD `-31.2762`
- `market_context_high->equity_1h` score `-0.3926` n `242` status `ready` deltaP `4.1867` edge `0.0346` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3939` n `30` status `ready` deltaP `1.8363` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4672` n `242` status `ready` deltaP `2.6352` edge `0.0024` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5707` n `242` status `ready` deltaP `-2.5573` edge `-0.0004` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6511` n `242` status `ready` deltaP `0.4912` edge `0.0046` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6736` n `242` status `ready` deltaP `-0.6471` edge `-0.0007` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.1256` n `30` status `ready` deltaP `-10.7485` edge `-0.0212` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1475` n `242` status `ready` deltaP `1.5515` edge `0.0193` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1517` n `242` status `ready` deltaP `1.695` edge `0.0163` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4795` n `232` status `ready` deltaP `-1.6874` edge `-0.0071` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.567` n `232` status `ready` deltaP `-1.9607` edge `-0.0246` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
