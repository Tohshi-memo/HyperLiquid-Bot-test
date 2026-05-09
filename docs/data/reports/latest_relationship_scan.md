# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T06:37:17.143686+00:00`
- Price records: `672`
- Market context records: `838`
- Flow alert records: `2354`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1278`

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

- `market_context_high->crypto_major_24h` score `11.9678` n `154` status `ready` deltaP `28.621` edge `0.8399` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.019` n `154` status `ready` deltaP `7.1631` edge `0.3753` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4686` n `33` status `ready` deltaP `9.5806` edge `0.2617` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4686` n `33` status `ready` deltaP `9.5806` edge `0.2617` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.53` n `33` status `ready` deltaP `14.4217` edge `0.1235` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.53` n `33` status `ready` deltaP `14.4217` edge `0.1235` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.4257` n `33` status `ready` deltaP `18.4405` edge `0.1164` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4257` n `33` status `ready` deltaP `18.4405` edge `0.1164` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.0706` n `33` status `ready` deltaP `18.3481` edge `0.0707` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.0706` n `33` status `ready` deltaP `18.3481` edge `0.0707` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0632` n `33` status `ready` deltaP `12.5114` edge `0.0282` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0632` n `33` status `ready` deltaP `12.5114` edge `0.0282` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8294` n `33` status `ready` deltaP `5.363` edge `0.1537` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8294` n `33` status `ready` deltaP `5.363` edge `0.1537` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3218` n `33` status `ready` deltaP `8.4377` edge `0.0226` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3218` n `33` status `ready` deltaP `8.4377` edge `0.0226` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2174` n `33` status `ready` deltaP `7.4987` edge `0.0014` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2174` n `33` status `ready` deltaP `7.4987` edge `0.0014` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1993` n `33` status `ready` deltaP `3.983` edge `-0.0217` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1993` n `33` status `ready` deltaP `3.983` edge `-0.0217` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
