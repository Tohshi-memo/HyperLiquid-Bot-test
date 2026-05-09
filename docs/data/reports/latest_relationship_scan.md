# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T04:22:14.222273+00:00`
- Price records: `672`
- Market context records: `828`
- Flow alert records: `2326`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `12.1457` n `150` status `ready` deltaP `29.6459` edge `0.8479` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `4.9276` n `150` status `ready` deltaP `7.1458` edge `0.3678` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.436` n `33` status `ready` deltaP `9.4281` edge `0.26` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.436` n `33` status `ready` deltaP `9.4281` edge `0.26` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.6382` n `33` status `ready` deltaP `15.4887` edge `0.1254` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.6382` n `33` status `ready` deltaP `15.4887` edge `0.1254` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.4087` n `33` status `ready` deltaP `18.2881` edge `0.116` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4087` n `33` status `ready` deltaP `18.2881` edge `0.116` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.0428` n `33` status `ready` deltaP `18.1957` edge `0.0694` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.0428` n `33` status `ready` deltaP `18.1957` edge `0.0694` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.062` n `33` status `ready` deltaP `12.5114` edge `0.0281` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.062` n `33` status `ready` deltaP `12.5114` edge `0.0281` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8514` n `33` status `ready` deltaP `5.5155` edge `0.1555` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8514` n `33` status `ready` deltaP `5.5155` edge `0.1555` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3569` n `33` status `ready` deltaP `9.0365` edge `0.0231` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3569` n `33` status `ready` deltaP `9.0365` edge `0.0231` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2548` n `33` status `ready` deltaP `8.0975` edge `0.0022` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2548` n `33` status `ready` deltaP `8.0975` edge `0.0022` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1822` n `33` status `ready` deltaP `4.2824` edge `-0.0215` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1822` n `33` status `ready` deltaP `4.2824` edge `-0.0215` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
