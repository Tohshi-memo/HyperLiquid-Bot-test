# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T05:37:29.779953+00:00`
- Price records: `672`
- Market context records: `6056`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11127`

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

- `news_risk_high->fx_24h` score `8.0928` n `30` status `ready` deltaP `72.5694` edge `0.1906` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2807` n `30` status `ready` deltaP `44.2683` edge `0.0662` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2969` n `30` status `ready` deltaP `27.5249` edge `0.0218` maxDD `-0.1113`
- `news_risk_high->crypto_alt_24h` score `2.1283` n `30` status `ready` deltaP `27.3611` edge `0.0097` maxDD `-0.5131`
- `news_risk_high->commodity_24h` score `1.8255` n `30` status `ready` deltaP `23.125` edge `0.0185` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.2875` n `206` status `ready` deltaP `7.727` edge `0.1475` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.99` n `30` status `ready` deltaP `11.2375` edge `0.0987` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3697` n `30` status `ready` deltaP `6.2176` edge `0.0521` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1008` n `30` status `ready` deltaP `9.2361` edge `0.0385` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4991` n `206` status `ready` deltaP `2.2324` edge `0.001` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5354` n `206` status `ready` deltaP `0.3081` edge `-0.001` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.5356` n `30` status `ready` deltaP `-0.2595` edge `-0.0303` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7386` n `206` status `ready` deltaP `-2.2818` edge `-0.0017` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8277` n `206` status `ready` deltaP `4.7003` edge `0.0393` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8368` n `206` status `ready` deltaP `4.4053` edge `0.0386` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.0257` n `206` status `ready` deltaP `0.891` edge `0.0159` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0322` n `30` status `ready` deltaP `-9.2515` edge `-0.0192` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0697` n `206` status `ready` deltaP `0.6308` edge `0.0195` maxDD `-4.3608`
- `market_context_high->commodity_4h` score `-1.1968` n `206` status `ready` deltaP `-3.8835` edge `-0.0206` maxDD `-2.5555`
- `market_context_high->metal_4h` score `-1.2108` n `206` status `ready` deltaP `2.9615` edge `-0.0019` maxDD `-3.4996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
