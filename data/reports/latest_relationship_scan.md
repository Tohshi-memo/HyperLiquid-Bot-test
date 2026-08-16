# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T05:22:26.874457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `184.5252` n `88` status `ready` deltaP `-21.9257` edge `24.0716` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.5163` n `36` status `ready` deltaP `23.0213` edge `0.9275` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.612` n `36` status `ready` deltaP `38.7195` edge `0.3762` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3035` n `88` status `ready` deltaP `40.3616` edge `0.3453` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.6805` n `36` status `ready` deltaP `30.6759` edge `0.1022` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0937` n `102` status `ready` deltaP `18.7171` edge `0.0968` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8511` n `36` status `ready` deltaP `21.2906` edge `0.0255` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7011` n `36` status `ready` deltaP `7.8344` edge `0.1214` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.2503` n `103` status `ready` deltaP `5.1087` edge `0.0264` maxDD `-0.5016`
- `market_context_high->fx_1h` score `0.0843` n `103` status `ready` deltaP `5.4852` edge `0.0024` maxDD `-0.2527`
- `market_context_high->fx_4h` score `0.0318` n `102` status `ready` deltaP `8.151` edge `0.0102` maxDD `-0.504`
- `news_risk_high->fx_4h` score `0.0137` n `36` status `ready` deltaP `4.5562` edge `-0.0067` maxDD `-0.0863`
- `news_risk_high->index_1h` score `-0.0671` n `36` status `ready` deltaP `0.4658` edge `0.0139` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2027` n `36` status `ready` deltaP `0.9814` edge `-0.0016` maxDD `-0.1414`
- `news_risk_high->metal_1h` score `-0.6994` n `36` status `ready` deltaP `-7.8011` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->metal_1h` score `-0.7153` n `103` status `ready` deltaP `-1.7601` edge `-0.0084` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.9221` n `103` status `ready` deltaP `-9.4587` edge `-0.003` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.0961` n `36` status `ready` deltaP `-5.9215` edge `-0.0211` maxDD `-0.7946`
- `market_context_high->index_4h` score `-1.276` n `102` status `ready` deltaP `-11.0623` edge `-0.0086` maxDD `-0.8328`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
