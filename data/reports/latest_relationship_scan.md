# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T17:22:40.442244+00:00`
- Price records: `672`
- Market context records: `4011`
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

- `risk_on_high->unknown_4h` score `147.0615` n `40` status `ready` deltaP `-4.296` edge `12.4654` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.0615` n `40` status `ready` deltaP `-4.296` edge `12.4654` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.6838` n `135` status `ready` deltaP `-3.3982` edge `4.4825` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.6204` n `146` status `ready` deltaP `2.5876` edge `2.7434` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `7.6854` n `40` status `ready` deltaP `40.208` edge `0.3724` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.6854` n `40` status `ready` deltaP `40.208` edge `0.3724` maxDD `0.0`
- `market_context_high->index_24h` score `3.7038` n `135` status `ready` deltaP `26.4214` edge `0.181` maxDD `-3.2125`
- `risk_on_high->equity_4h` score `3.6458` n `40` status `ready` deltaP `36.9216` edge `0.0624` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6458` n `40` status `ready` deltaP `36.9216` edge `0.0624` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.903` n `135` status `ready` deltaP `14.5979` edge `0.2635` maxDD `-6.5125`
- `risk_on_high->index_24h` score `1.8542` n `40` status `ready` deltaP `27.9029` edge `-0.0315` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.8542` n `40` status `ready` deltaP `27.9029` edge `-0.0315` maxDD `0.0`
- `market_context_high->equity_4h` score `1.8336` n `146` status `ready` deltaP `19.5586` edge `0.1505` maxDD `-6.9137`
- `market_context_high->equity_24h` score `1.3922` n `135` status `ready` deltaP `16.5043` edge `0.3058` maxDD `-14.318`
- `market_context_high->equity_1h` score `1.2357` n `149` status `ready` deltaP `8.5862` edge `0.1017` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.1659` n `40` status `ready` deltaP `19.532` edge `0.0335` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1659` n `40` status `ready` deltaP `19.532` edge `0.0335` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `1.004` n `40` status `ready` deltaP `4.2028` edge `0.2838` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.004` n `40` status `ready` deltaP `4.2028` edge `0.2838` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9647` n `149` status `ready` deltaP `9.8712` edge `0.0688` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
