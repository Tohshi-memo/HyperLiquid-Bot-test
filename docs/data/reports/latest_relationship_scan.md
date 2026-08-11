# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T23:37:28.382475+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11856`

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

- `risk_on_high->commodity_4h` score `2.3159` n `32` status `ready` deltaP `16.2348` edge `0.103` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3159` n `32` status `ready` deltaP `16.2348` edge `0.103` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.0969` n `32` status `ready` deltaP `12.0135` edge `0.0346` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0969` n `32` status `ready` deltaP `12.0135` edge `0.0346` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0374` n `32` status `ready` deltaP `11.814` edge `0.0218` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0374` n `32` status `ready` deltaP `11.814` edge `0.0218` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6901` n `180` status `ready` deltaP `9.9302` edge `0.0235` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5824` n `180` status `ready` deltaP `9.7765` edge `0.0472` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.402` n `32` status `ready` deltaP `11.6018` edge `0.0117` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.402` n `32` status `ready` deltaP `11.6018` edge `0.0117` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1885` n `32` status `ready` deltaP `5.3518` edge `0.0028` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1885` n `32` status `ready` deltaP `5.3518` edge `0.0028` maxDD `-0.1547`
- `market_context_high->commodity_24h` score `0.14` n `153` status `ready` deltaP `7.8442` edge `0.0397` maxDD `-2.4263`
- `market_context_high->fx_1h` score `-0.0819` n `180` status `ready` deltaP `4.6574` edge `0.0008` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0952` n `180` status `ready` deltaP `6.189` edge `0.007` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.2291` n `32` status `ready` deltaP `1.4482` edge `0.0192` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.2291` n `32` status `ready` deltaP `1.4482` edge `0.0192` maxDD `-0.6579`
- `market_context_high->fx_24h` score `-0.5214` n `153` status `ready` deltaP `8.0832` edge `0.0166` maxDD `-1.6539`
- `risk_on_high->equity_1h` score `-0.6079` n `32` status `ready` deltaP `-3.0127` edge `-0.0035` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6079` n `32` status `ready` deltaP `-3.0127` edge `-0.0035` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
