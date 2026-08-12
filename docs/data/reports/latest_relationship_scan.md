# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T14:37:31.712563+00:00`
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

- `risk_on_high->crypto_major_24h` score `2.9281` n `32` status `ready` deltaP `19.9653` edge `0.3579` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.9281` n `32` status `ready` deltaP `19.9653` edge `0.3579` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.3285` n `32` status `ready` deltaP `15.7774` edge `0.1071` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3285` n `32` status `ready` deltaP `15.7774` edge `0.1071` maxDD `-0.1258`
- `risk_on_high->equity_24h` score `2.1288` n `32` status `ready` deltaP `5.9028` edge `0.4115` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `2.1288` n `32` status `ready` deltaP `5.9028` edge `0.4115` maxDD `-11.2348`
- `risk_on_high->commodity_24h` score `2.0182` n `32` status `ready` deltaP `18.4028` edge `0.0455` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.0182` n `32` status `ready` deltaP `18.4028` edge `0.0455` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.805` n `32` status `ready` deltaP `20.1389` edge `0.0346` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.805` n `32` status `ready` deltaP `20.1389` edge `0.0346` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.4815` n `32` status `ready` deltaP `5.1647` edge `0.1209` maxDD `-0.5496`
- `risk_on_high->index_24h` score `1.4431` n `32` status `ready` deltaP `13.0208` edge `0.0639` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.4431` n `32` status `ready` deltaP `13.0208` edge `0.0639` maxDD `-0.4355`
- `risk_on_high->commodity_1h` score `1.1604` n `32` status `ready` deltaP `12.6123` edge `0.0359` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1604` n `32` status `ready` deltaP `12.6123` edge `0.0359` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9889` n `32` status `ready` deltaP `11.3567` edge `0.0208` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9889` n `32` status `ready` deltaP `11.3567` edge `0.0208` maxDD `-0.1285`
- `news_risk_high->index_1h` score `0.7629` n `32` status `ready` deltaP `9.6557` edge `0.0218` maxDD `-0.141`
- `market_context_high->commodity_1h` score `0.7249` n `178` status `ready` deltaP `10.1544` edge `0.0249` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.5491` n `178` status `ready` deltaP `9.0007` edge `0.0496` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
