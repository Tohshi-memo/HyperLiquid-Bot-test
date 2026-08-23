# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T05:37:29.601765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `17.1833` n `44` status `ready` deltaP `28.5061` edge `1.2419` maxDD `0.0`
- `risk_on_high->unknown_1h` score `5.6487` n `31` status `ready` deltaP `-6.8379` edge `0.8082` maxDD `-1.4071`
- `risk_on_and_context->unknown_1h` score `5.6487` n `31` status `ready` deltaP `-6.8379` edge `0.8082` maxDD `-1.4071`
- `news_risk_high->equity_4h` score `5.0536` n `44` status `ready` deltaP `36.6547` edge `0.2042` maxDD `-0.5276`
- `news_risk_high->unknown_1h` score `3.827` n `51` status `ready` deltaP `20.6763` edge `0.2115` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2443` n `44` status `ready` deltaP `38.6086` edge `0.0264` maxDD `-0.0746`
- `news_risk_high->index_4h` score `1.4754` n `44` status `ready` deltaP `20.4684` edge `0.0251` maxDD `-0.0884`
- `news_risk_high->metal_4h` score `1.2745` n `44` status `ready` deltaP `19.6507` edge `-0.0032` maxDD `-0.0611`
- `news_risk_high->fx_1h` score `1.1966` n `51` status `ready` deltaP `16.5463` edge `0.0064` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1033` n `135` status `ready` deltaP `4.9901` edge `0.0971` maxDD `-1.4071`
- `news_risk_high->equity_1h` score `0.8368` n `51` status `ready` deltaP `18.193` edge `0.0225` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.7646` n `130` status `ready` deltaP `21.583` edge `-0.063` maxDD `-0.3736`
- `risk_on_high->fx_1h` score `0.6906` n `31` status `ready` deltaP `10.4742` edge `0.0049` maxDD `-0.041`
- `risk_on_and_context->fx_1h` score `0.6906` n `31` status `ready` deltaP `10.4742` edge `0.0049` maxDD `-0.041`
- `news_risk_high->index_1h` score `0.2076` n `51` status `ready` deltaP `8.8235` edge `0.0031` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1859` n `51` status `ready` deltaP `8.5388` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1806` n `130` status `ready` deltaP `8.5037` edge `0.0086` maxDD `-0.3527`
- `risk_on_high->equity_1h` score `0.072` n `31` status `ready` deltaP `-0.7823` edge `0.0501` maxDD `-0.8526`
- `risk_on_and_context->equity_1h` score `0.072` n `31` status `ready` deltaP `-0.7823` edge `0.0501` maxDD `-0.8526`
- `risk_on_high->index_1h` score `0.0132` n `31` status `ready` deltaP `1.6129` edge `0.0087` maxDD `-0.0875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
