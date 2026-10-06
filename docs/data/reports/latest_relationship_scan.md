# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T22:37:26.678343+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1420.4896` n `117` status `ready` deltaP `11.3782` edge `118.3363` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.5155` n `117` status `ready` deltaP `-0.6632` edge `2.4346` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3084` n `62` status `ready` deltaP `34.0087` edge `0.5693` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.397` n `62` status `ready` deltaP `19.7335` edge `0.4526` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1513` n `62` status `ready` deltaP `22.3958` edge `0.1133` maxDD `0.0`
- `news_risk_high->index_4h` score `2.713` n `62` status `ready` deltaP `30.478` edge `0.0491` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5636` n `117` status `ready` deltaP `13.8681` edge `0.2176` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.3291` n `62` status `ready` deltaP `5.5276` edge `0.1672` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9156` n `62` status `ready` deltaP `7.1808` edge `0.1473` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8618` n `62` status `ready` deltaP `23.6769` edge `0.0123` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7164` n `62` status `ready` deltaP `17.0142` edge `0.0894` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2269` n `62` status `ready` deltaP `17.7419` edge `0.0806` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0209` n `62` status `ready` deltaP `29.6259` edge `0.09` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.9324` n `117` status `ready` deltaP `19.9604` edge `0.0203` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7675` n `62` status `ready` deltaP `2.7091` edge `0.0978` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7384` n `117` status `ready` deltaP `12.6926` edge `0.0053` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5898` n `117` status `ready` deltaP `12.6381` edge `0.0349` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3847` n `117` status `ready` deltaP `8.762` edge `0.0133` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.2721` n `117` status `ready` deltaP `-1.1791` edge `0.2029` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `0.0083` n `62` status `ready` deltaP `5.5534` edge `0.0055` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
