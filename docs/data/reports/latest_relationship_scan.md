# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T10:52:31.354513+00:00`
- Price records: `672`
- Market context records: `5973`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.2189` n `30` status `ready` deltaP `66.1458` edge `0.1606` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.9444` n `30` status `ready` deltaP `36.1459` edge `0.1916` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9306` n `30` status `ready` deltaP `40.7622` edge `0.0604` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1627` n `30` status `ready` deltaP `26.0279` edge `0.0206` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4333` n `234` status `ready` deltaP `9.0721` edge `0.1684` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8247` n `30` status `ready` deltaP `10.0399` edge `0.0855` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1608` n `30` status `ready` deltaP `5.02` edge `0.0333` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0258` n `30` status `ready` deltaP `8.5416` edge `0.0269` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3806` n `30` status `ready` deltaP `1.986` edge `-0.0254` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4381` n `242` status `ready` deltaP `3.5817` edge `0.0328` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4888` n `242` status `ready` deltaP `2.3717` edge `0.0014` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5091` n `242` status `ready` deltaP `-1.5811` edge `0.001` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6775` n `242` status `ready` deltaP `-0.6112` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.709` n `242` status `ready` deltaP `-0.5629` edge `0.0042` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.8706` n `212` status `ready` deltaP `21.2002` edge `0.3104` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0906` n `30` status `ready` deltaP `-10.1497` edge `-0.0207` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1074` n `234` status `ready` deltaP `1.0723` edge `0.0196` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1123` n `242` status `ready` deltaP `2.0785` edge `0.0203` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1458` n `242` status `ready` deltaP `1.6591` edge `0.0173` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4378` n `234` status `ready` deltaP `-1.3199` edge `-0.0042` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
