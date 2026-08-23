# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T14:07:25.944641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.1415` n `51` status `ready` deltaP `25.4782` edge `1.0132` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.8151` n `33` status `ready` deltaP `-9.227` edge `0.7237` maxDD `-1.5896`
- `risk_on_and_context->unknown_1h` score `4.8151` n `33` status `ready` deltaP `-9.227` edge `0.7237` maxDD `-1.5896`
- `news_risk_high->unknown_1h` score `3.4384` n `51` status `ready` deltaP `18.5804` edge `0.1931` maxDD `-0.7683`
- `news_risk_high->fx_4h` score `2.9425` n `51` status `ready` deltaP `34.8816` edge `0.0261` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.7058` n `51` status `ready` deltaP `23.2694` edge `0.1474` maxDD `-2.164`
- `risk_on_high->metal_4h` score `2.2888` n `33` status `ready` deltaP `30.4093` edge `-0.0032` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.2888` n `33` status `ready` deltaP `30.4093` edge `-0.0032` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.587` n `33` status `ready` deltaP `-1.686` edge `0.2577` maxDD `-0.773`
- `risk_on_and_context->equity_4h` score `1.587` n `33` status `ready` deltaP `-1.686` edge `0.2577` maxDD `-0.773`
- `market_context_high->crypto_alt_4h` score `1.2555` n `128` status `ready` deltaP `9.2607` edge `0.1897` maxDD `-7.0785`
- `market_context_high->unknown_1h` score `1.168` n `128` status `ready` deltaP `6.54` edge `0.0986` maxDD `-1.5896`
- `news_risk_high->fx_1h` score `1.1631` n `51` status `ready` deltaP `16.0972` edge `0.0066` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7091` n `51` status `ready` deltaP `16.0972` edge `0.02` maxDD `-0.9128`
- `risk_on_high->fx_4h` score `0.6992` n `33` status `ready` deltaP `16.3433` edge `0.0039` maxDD `-0.1905`
- `risk_on_and_context->fx_4h` score `0.6992` n `33` status `ready` deltaP `16.3433` edge `0.0039` maxDD `-0.1905`
- `market_context_high->unknown_4h` score `0.6802` n `128` status `ready` deltaP `21.189` edge `-0.0674` maxDD `-0.3741`
- `market_context_high->commodity_24h` score `0.5629` n `112` status `ready` deltaP `-0.9921` edge `0.101` maxDD `-0.7984`
- `news_risk_high->index_4h` score `0.5362` n `51` status `ready` deltaP `9.7381` edge `0.0195` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.3995` n `33` status `ready` deltaP `8.4904` edge `0.0426` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
