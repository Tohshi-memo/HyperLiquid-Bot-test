# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T15:22:33.916315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `23.3763` n `134` status `ready` deltaP `-19.9294` edge `2.3263` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.943` n `32` status `ready` deltaP `19.5884` edge `0.1329` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.943` n `32` status `ready` deltaP `19.5884` edge `0.1329` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.3403` n `32` status `ready` deltaP `13.5105` edge `0.0449` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3403` n `32` status `ready` deltaP `13.5105` edge `0.0449` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0716` n `32` status `ready` deltaP `12.2713` edge `0.0216` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0716` n `32` status `ready` deltaP `12.2713` edge `0.0216` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9495` n `182` status `ready` deltaP `12.3425` edge `0.0683` maxDD `-2.7169`
- `market_context_high->commodity_24h` score `0.8259` n `134` status `ready` deltaP `9.9925` edge `0.0909` maxDD `-3.0953`
- `market_context_high->commodity_1h` score `0.8255` n `182` status `ready` deltaP `10.6946` edge `0.0312` maxDD `-0.6965`
- `market_context_high->fx_24h` score `0.2904` n `134` status `ready` deltaP `13.6643` edge `0.0269` maxDD `-1.4613`
- `risk_on_high->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2532` n `32` status `ready` deltaP `6.1003` edge `0.0032` maxDD `-0.1547`
- `risk_on_high->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2112` n `32` status `ready` deltaP `8.6078` edge `0.0072` maxDD `-0.3343`
- `market_context_high->fx_1h` score `-0.043` n `182` status `ready` deltaP `5.3448` edge `0.0012` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0795` n `182` status `ready` deltaP `6.5364` edge `0.0067` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.5116` n `32` status `ready` deltaP `-1.6006` edge `0.0033` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.5116` n `32` status `ready` deltaP `-1.6006` edge `0.0033` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.8191` n `32` status `ready` deltaP `-4.8091` edge `-0.0186` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
