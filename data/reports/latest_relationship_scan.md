# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T19:37:28.480011+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4155`

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

- `news_risk_high->equity_4h` score `2.058` n `92` status `ready` deltaP `15.8272` edge `0.2489` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.9445` n `92` status `ready` deltaP `15.2372` edge `0.0249` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.6528` n `92` status `ready` deltaP `6.5608` edge `0.0949` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3644` n `92` status `ready` deltaP `12.5163` edge `0.0086` maxDD `-0.2931`
- `news_risk_high->metal_1h` score `-0.2444` n `92` status `ready` deltaP `0.9763` edge `-0.0021` maxDD `-0.5256`
- `news_risk_high->crypto_major_4h` score `-0.2703` n `92` status `ready` deltaP `3.0687` edge `0.1135` maxDD `-9.1553`
- `news_risk_high->crypto_alt_1h` score `-0.3769` n `92` status `ready` deltaP `4.12` edge `0.047` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.3811` n `92` status `ready` deltaP `1.0737` edge `-0.0016` maxDD `-0.353`
- `news_risk_high->fx_1h` score `-0.4121` n `92` status `ready` deltaP `-1.868` edge `-0.0004` maxDD `-0.1984`
- `news_risk_high->index_24h` score `-0.4508` n `92` status `ready` deltaP `0.5275` edge `0.1424` maxDD `-6.6786`
- `news_risk_high->equity_24h` score `-0.4841` n `92` status `ready` deltaP `27.9858` edge `0.91` maxDD `-86.0244`
- `news_risk_high->crypto_major_1h` score `-0.6002` n `92` status `ready` deltaP `-1.0154` edge `0.0237` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-0.9215` n `92` status `ready` deltaP `0.2717` edge `-0.0294` maxDD `-1.5773`
- `news_risk_high->crypto_alt_4h` score `-0.9703` n `92` status `ready` deltaP `-0.4573` edge `0.1423` maxDD `-14.0916`
- `news_risk_high->fx_24h` score `-1.142` n `92` status `ready` deltaP `-9.5264` edge `0.0175` maxDD `-0.2659`
- `news_risk_high->metal_24h` score `-2.8875` n `92` status `ready` deltaP `4.3214` edge `-0.2094` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2357` n `92` status `ready` deltaP `-18.9274` edge `-0.0137` maxDD `-2.7141`
- `news_risk_high->commodity_4h` score `-4.4039` n `92` status `ready` deltaP `-26.7563` edge `-0.0084` maxDD `-5.7508`
- `news_risk_high->crypto_major_24h` score `-6.5099` n `92` status `ready` deltaP `-16.7527` edge `0.1274` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.4187` n `92` status `ready` deltaP `-25.3202` edge `-0.0136` maxDD `-30.8658`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
