# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T12:07:38.925035+00:00`
- Price records: `672`
- Market context records: `5979`
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

- `news_risk_high->fx_24h` score `7.3171` n `30` status `ready` deltaP `67.0139` edge `0.163` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.7933` n `30` status `ready` deltaP `35.2778` edge `0.1848` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0096` n `30` status `ready` deltaP `41.5244` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1388` n `30` status `ready` deltaP `25.7285` edge `0.0206` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2937` n `238` status `ready` deltaP `8.452` edge `0.1609` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7491` n `30` status `ready` deltaP `9.7405` edge `0.0778` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.0906` n `30` status `ready` deltaP `4.7206` edge `0.0263` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0293` n `30` status `ready` deltaP `9.0625` edge `0.0305` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4289` n `30` status `ready` deltaP `1.3872` edge `-0.0276` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4375` n `241` status `ready` deltaP `3.6686` edge `0.0323` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.4954` n `241` status `ready` deltaP `-1.4995` edge `0.0022` maxDD `-1.4578`
- `market_context_high->metal_1h` score `-0.5192` n `241` status `ready` deltaP `1.9958` edge `0.0` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.686` n `241` status `ready` deltaP `-0.7168` edge `-0.0007` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7045` n `241` status `ready` deltaP `-0.5069` edge `0.0044` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9566` n `213` status `ready` deltaP `21.271` edge `0.3111` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0976` n `30` status `ready` deltaP `-10.2994` edge `-0.0206` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1279` n `238` status `ready` deltaP `0.7698` edge `0.019` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1518` n `241` status `ready` deltaP `2.0089` edge `0.0157` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.188` n `241` status `ready` deltaP `1.5809` edge `0.0124` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4166` n `238` status `ready` deltaP `-1.0453` edge `-0.0044` maxDD `-6.2867`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
