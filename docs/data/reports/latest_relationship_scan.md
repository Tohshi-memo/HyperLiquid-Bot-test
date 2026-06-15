# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T17:07:40.722121+00:00`
- Price records: `672`
- Market context records: `4010`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10540`

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

- `risk_on_high->unknown_4h` score `147.1121` n `40` status `ready` deltaP `-4.1438` edge `12.4686` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `147.1121` n `40` status `ready` deltaP `-4.1438` edge `12.4686` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.7949` n `135` status `ready` deltaP `-3.2249` edge `4.4906` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.671` n `146` status `ready` deltaP `2.7398` edge `2.7466` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `7.8721` n `40` status `ready` deltaP `40.3813` edge `0.3868` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `7.8721` n `40` status `ready` deltaP `40.3813` edge `0.3868` maxDD `0.0`
- `market_context_high->index_24h` score `3.8113` n `135` status `ready` deltaP `26.5948` edge `0.1888` maxDD `-3.2125`
- `risk_on_high->equity_4h` score `3.6916` n `40` status `ready` deltaP `37.0738` edge `0.0652` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6916` n `40` status `ready` deltaP `37.0738` edge `0.0652` maxDD `-0.0446`
- `market_context_high->metal_24h` score `3.0104` n `135` status `ready` deltaP `14.7712` edge `0.2713` maxDD `-6.5125`
- `risk_on_high->index_24h` score `1.9617` n `40` status `ready` deltaP `28.0763` edge `-0.0237` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.9617` n `40` status `ready` deltaP `28.0763` edge `-0.0237` maxDD `0.0`
- `market_context_high->equity_4h` score `1.8794` n `146` status `ready` deltaP `19.7108` edge `0.1533` maxDD `-6.9137`
- `market_context_high->equity_24h` score `1.5789` n `135` status `ready` deltaP `16.6776` edge `0.3202` maxDD `-14.318`
- `market_context_high->equity_1h` score `1.2485` n `149` status `ready` deltaP `8.6717` edge `0.1022` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `1.1695` n `40` status `ready` deltaP `19.532` edge `0.0338` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1695` n `40` status `ready` deltaP `19.532` edge `0.0338` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `1.0076` n `40` status `ready` deltaP `4.2028` edge `0.2841` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0076` n `40` status `ready` deltaP `4.2028` edge `0.2841` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.959` n `149` status `ready` deltaP `9.8003` edge `0.0688` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
