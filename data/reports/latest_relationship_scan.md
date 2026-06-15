# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T17:37:44.847696+00:00`
- Price records: `672`
- Market context records: `4012`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `147.0133` n `40` status `ready` deltaP `-4.4482` edge `12.4624` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.0133` n `40` status `ready` deltaP `-4.4482` edge `12.4624` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.5619` n `135` status `ready` deltaP `-3.5715` edge `4.4735` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.5722` n `146` status `ready` deltaP `2.4354` edge `2.7404` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `7.524` n `40` status `ready` deltaP `40.0347` edge `0.3601` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.524` n `40` status `ready` deltaP `40.0347` edge `0.3601` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.6121` n `40` status `ready` deltaP `36.7694` edge `0.0606` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6121` n `40` status `ready` deltaP `36.7694` edge `0.0606` maxDD `-0.0446`
- `market_context_high->index_24h` score `3.612` n `135` status `ready` deltaP `26.2481` edge `0.1745` maxDD `-3.2125`
- `market_context_high->metal_24h` score `2.8051` n `135` status `ready` deltaP `14.4245` edge `0.2565` maxDD `-6.5125`
- `market_context_high->equity_4h` score `1.7999` n `146` status `ready` deltaP `19.4064` edge `0.1487` maxDD `-6.9137`
- `risk_on_high->index_24h` score `1.7624` n `40` status `ready` deltaP `27.7296` edge `-0.038` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.7624` n `40` status `ready` deltaP `27.7296` edge `-0.038` maxDD `0.0`
- `market_context_high->equity_1h` score `1.2393` n `149` status `ready` deltaP `8.5862` edge `0.102` maxDD `-2.144`
- `market_context_high->equity_24h` score `1.2308` n `135` status `ready` deltaP `16.331` edge `0.2935` maxDD `-14.318`
- `risk_on_high->crypto_major_4h` score `1.1719` n `40` status `ready` deltaP `19.532` edge `0.034` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1719` n `40` status `ready` deltaP `19.532` edge `0.034` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `1.0028` n `40` status `ready` deltaP `4.2028` edge `0.2837` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0028` n `40` status `ready` deltaP `4.2028` edge `0.2837` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9947` n `149` status `ready` deltaP `10.0209` edge `0.0703` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
