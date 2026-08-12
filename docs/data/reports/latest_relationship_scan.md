# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T13:41:25.530884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->crypto_major_24h` score `2.9802` n `32` status `ready` deltaP `20.4861` edge `0.3611` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.9802` n `32` status `ready` deltaP `20.4861` edge `0.3611` maxDD `-6.2481`
- `risk_on_high->equity_24h` score `2.4254` n `32` status `ready` deltaP `6.5972` edge `0.4449` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `2.4254` n `32` status `ready` deltaP `6.5972` edge `0.4449` maxDD `-11.2348`
- `risk_on_high->commodity_4h` score `2.3431` n `32` status `ready` deltaP `15.9299` edge `0.1073` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3431` n `32` status `ready` deltaP `15.9299` edge `0.1073` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `2.1026` n `32` status `ready` deltaP `19.0972` edge `0.0479` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.1026` n `32` status `ready` deltaP `19.0972` edge `0.0479` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8062` n `32` status `ready` deltaP `20.1389` edge `0.0347` maxDD `-0.1418`
- `risk_on_high->index_24h` score `1.5563` n `32` status `ready` deltaP `13.7153` edge `0.0687` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.5563` n `32` status `ready` deltaP `13.7153` edge `0.0687` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.158` n `32` status `ready` deltaP `12.6123` edge `0.0357` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.158` n `32` status `ready` deltaP `12.6123` edge `0.0357` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0145` n `32` status `ready` deltaP `11.6616` edge `0.0209` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0145` n `32` status `ready` deltaP `11.6616` edge `0.0209` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.7225` n `178` status `ready` deltaP `10.1544` edge `0.0247` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5637` n `178` status `ready` deltaP `9.1532` edge `0.0498` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.2914` n `32` status `ready` deltaP `9.8054` edge `0.0095` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2914` n `32` status `ready` deltaP `9.8054` edge `0.0095` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
