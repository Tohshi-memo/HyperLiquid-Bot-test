# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T12:52:30.722177+00:00`
- Price records: `672`
- Market context records: `5041`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `market_context_high->unknown_1h` score `12.2296` n `100` status `ready` deltaP `4.0539` edge `1.0422` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0837` n `93` status `ready` deltaP `22.3642` edge `0.7101` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4877` n `93` status `ready` deltaP `16.6421` edge `0.5048` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3322` n `93` status `ready` deltaP `14.331` edge `0.4882` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2014` n `93` status `ready` deltaP `12.7819` edge `0.1228` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.7895` n `100` status `ready` deltaP `7.0419` edge `0.1106` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.7885` n `100` status `ready` deltaP `8.0479` edge `0.0694` maxDD `-2.5875`
- `market_context_high->metal_1h` score `0.3674` n `100` status `ready` deltaP `6.6407` edge `0.036` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.3655` n `93` status `ready` deltaP `2.2063` edge `0.1703` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.2075` n `100` status `ready` deltaP `5.3473` edge `0.0932` maxDD `-5.5126`
- `market_context_high->fx_24h` score `0.002` n `74` status `ready` deltaP `10.2525` edge `0.0081` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2324` n `93` status `ready` deltaP `2.6472` edge `0.0391` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3026` n `100` status `ready` deltaP `1.7964` edge `0.0152` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4005` n `100` status `ready` deltaP `1.5988` edge `0.0121` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7633` n `93` status `ready` deltaP `4.1552` edge `-0.0003` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0252` n `93` status `ready` deltaP `-4.5256` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.4938` n `100` status `ready` deltaP `-8.7545` edge `-0.0051` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.5977` n `74` status `ready` deltaP `6.7708` edge `0.0391` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.7332` n `74` status `ready` deltaP `-0.4552` edge `-0.0929` maxDD `-27.5371`
- `market_context_high->crypto_major_24h` score `-6.0623` n `74` status `ready` deltaP `14.8086` edge `0.4036` maxDD `-90.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
