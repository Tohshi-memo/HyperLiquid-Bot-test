# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T00:52:32.109154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.7588` n `34` status `ready` deltaP `0.9951` edge `0.6794` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.7588` n `34` status `ready` deltaP `0.9951` edge `0.6794` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `5.2296` n `74` status `ready` deltaP `18.3428` edge `0.4343` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.692` n `74` status `ready` deltaP `16.9844` edge `0.1111` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.3215` n `34` status `ready` deltaP `17.8443` edge `0.0047` maxDD `-0.0827`
- `risk_on_and_context->fx_4h` score `1.3215` n `34` status `ready` deltaP `17.8443` edge `0.0047` maxDD `-0.0827`
- `market_context_high->index_24h` score `1.0937` n `74` status `ready` deltaP `17.7127` edge `-0.0226` maxDD `-0.0141`
- `risk_on_high->crypto_major_1h` score `0.7903` n `34` status `ready` deltaP `9.8186` edge `0.031` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.7903` n `34` status `ready` deltaP `9.8186` edge `0.031` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.7409` n `34` status `ready` deltaP `13.2529` edge `0.0109` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7409` n `34` status `ready` deltaP `13.2529` edge `0.0109` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.529` n `34` status `ready` deltaP `10.9545` edge `0.0254` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.529` n `34` status `ready` deltaP `10.9545` edge `0.0254` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.4174` n `116` status `ready` deltaP `10.5919` edge `0.0492` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.3597` n `34` status `ready` deltaP `2.6812` edge `0.075` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3597` n `34` status `ready` deltaP `2.6812` edge `0.075` maxDD `-1.3651`
- `risk_on_high->fx_1h` score `0.2286` n `34` status `ready` deltaP `6.9303` edge `0.0049` maxDD `-0.0771`
- `risk_on_and_context->fx_1h` score `0.2286` n `34` status `ready` deltaP `6.9303` edge `0.0049` maxDD `-0.0771`
- `market_context_high->commodity_24h` score `0.2126` n `74` status `ready` deltaP `13.2208` edge `0.1129` maxDD `-4.666`
- `market_context_high->index_1h` score `0.2108` n `116` status `ready` deltaP `8.1819` edge `0.005` maxDD `-0.3584`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
