# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T11:07:32.163591+00:00`
- Price records: `672`
- Market context records: `5872`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10178`

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

- `news_risk_high->fx_4h` score `3.7449` n `30` status `ready` deltaP `39.0854` edge `0.0561` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.037` n `30` status `ready` deltaP `24.6806` edge `0.0191` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.339` n `236` status `ready` deltaP `7.6504` edge `0.1706` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9041` n `30` status `ready` deltaP `11.8363` edge `0.0837` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2629` n `30` status `ready` deltaP `5.4691` edge `0.0434` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.424` n `240` status `ready` deltaP `-0.736` edge `-0.0006` maxDD `-0.5751`
- `market_context_high->equity_1h` score `-0.4277` n `240` status `ready` deltaP `4.748` edge `0.0334` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4305` n `30` status `ready` deltaP `1.5369` edge `-0.0288` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4543` n `240` status `ready` deltaP `3.6203` edge `0.0051` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.5468` n `240` status `ready` deltaP `-1.6218` edge `-0.0022` maxDD `-1.9006`
- `market_context_high->index_1h` score `-0.6106` n `240` status `ready` deltaP `0.4042` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7472` n `240` status `ready` deltaP `3.9197` edge `0.0437` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.8562` n `240` status `ready` deltaP `2.9691` edge `0.0423` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1913` n `236` status `ready` deltaP `0.2248` edge `0.0145` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2159` n `30` status `ready` deltaP `-12.0958` edge `-0.0238` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.8174` n `30` status `ready` deltaP `-13.8821` edge `-0.0529` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8374` n `228` status `ready` deltaP `4.8794` edge `0.0137` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.9373` n `236` status `ready` deltaP `-7.2705` edge `-0.005` maxDD `-2.2593`
- `market_context_high->crypto_major_4h` score `-2.1838` n `236` status `ready` deltaP `9.4434` edge `0.1923` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.2347` n `236` status `ready` deltaP `-0.2946` edge `-0.0129` maxDD `-6.3754`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
