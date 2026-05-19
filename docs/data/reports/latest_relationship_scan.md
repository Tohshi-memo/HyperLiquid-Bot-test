# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T20:37:20.413576+00:00`
- Price records: `672`
- Market context records: `1254`
- Flow alert records: `5517`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.0411` n `128` status `ready` deltaP `41.927` edge `1.3371` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.4367` n `128` status `ready` deltaP `2.9514` edge `0.8501` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `7.9974` n `128` status `ready` deltaP `5.221` edge `0.7533` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7125` n `128` status `ready` deltaP `22.6562` edge `0.6933` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1807` n `128` status `ready` deltaP `23.9583` edge `0.2973` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.3104` n `128` status `ready` deltaP `17.5495` edge `0.2252` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.3011` n `128` status `ready` deltaP `22.3958` edge `0.5066` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `3.1799` n `128` status `ready` deltaP `-9.2014` edge `0.4745` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.0922` n `128` status `ready` deltaP `1.5625` edge `0.4369` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5083` n `128` status `ready` deltaP `13.7385` edge `0.1024` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7835` n `128` status `ready` deltaP `10.7972` edge `0.025` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7452` n `128` status `ready` deltaP `6.8066` edge `0.0536` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.3783` n `128` status `ready` deltaP `16.3682` edge `0.0655` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.3732` n `128` status `ready` deltaP `11.7655` edge `0.0137` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.2224` n `128` status `ready` deltaP `4.948` edge `0.032` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.0093` n `128` status `ready` deltaP `6.917` edge `0.1472` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1432` n `128` status `ready` deltaP `5.3004` edge `-0.0017` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2713` n `128` status `ready` deltaP `1.0947` edge `0.0422` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4105` n `128` status `ready` deltaP `2.3765` edge `0.0081` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6365` n `128` status `ready` deltaP `8.0983` edge `0.1609` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
