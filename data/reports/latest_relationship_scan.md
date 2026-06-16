# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T15:46:51.652272+00:00`
- Price records: `672`
- Market context records: `4105`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10552`

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

- `risk_on_high->unknown_4h` score `144.7909` n `40` status `ready` deltaP `-8.9634` edge `12.3073` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7909` n `40` status `ready` deltaP `-8.9634` edge `12.3073` maxDD `-10.864`
- `market_context_high->unknown_1h` score `44.9854` n `185` status `ready` deltaP `1.9575` edge `3.8935` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `35.6185` n `146` status `ready` deltaP `-8.4649` edge `3.4275` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.7477` n `177` status `ready` deltaP `-2.0566` edge `1.8683` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.5615` n `40` status `ready` deltaP `36.372` edge `-0.0243` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.5615` n `40` status `ready` deltaP `36.372` edge `-0.0243` maxDD `-0.0446`
- `risk_on_high->equity_1h` score `0.2216` n `40` status `ready` deltaP `10.7635` edge `-0.0142` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.2216` n `40` status `ready` deltaP `10.7635` edge `-0.0142` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1191` n `40` status `ready` deltaP `10.7012` edge `0.003` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1191` n `40` status `ready` deltaP `10.7012` edge `0.003` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0646` n `40` status `ready` deltaP `4.5509` edge `0.0009` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0646` n `40` status `ready` deltaP `4.5509` edge `0.0009` maxDD `-0.1704`
- `risk_on_high->crypto_major_4h` score `0.0183` n `40` status `ready` deltaP `16.7073` edge `-0.0433` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.0183` n `40` status `ready` deltaP `16.7073` edge `-0.0433` maxDD `-2.6576`
- `risk_on_high->crypto_major_1h` score `-0.0433` n `40` status `ready` deltaP `10.3593` edge `-0.0204` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0433` n `40` status `ready` deltaP `10.3593` edge `-0.0204` maxDD `-2.3372`
- `market_context_high->equity_4h` score `-0.172` n `177` status `ready` deltaP `11.7534` edge `0.0604` maxDD `-6.9137`
- `market_context_high->fx_1h` score `-0.3024` n `185` status `ready` deltaP `1.4428` edge `0.0001` maxDD `-0.546`
- `risk_on_high->commodity_24h` score `-0.3947` n `40` status `ready` deltaP `-2.5563` edge `0.2123` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
