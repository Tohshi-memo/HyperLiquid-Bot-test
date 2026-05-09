# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T04:07:14.122983+00:00`
- Price records: `672`
- Market context records: `827`
- Flow alert records: `2323`
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

- `market_context_high->crypto_major_24h` score `12.1041` n `149` status `ready` deltaP `29.7702` edge `0.8436` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `4.8217` n `149` status `ready` deltaP `7.1414` edge `0.359` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4348` n `33` status `ready` deltaP `9.4281` edge `0.2599` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4348` n `33` status `ready` deltaP `9.4281` edge `0.2599` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.6552` n `33` status `ready` deltaP `15.6412` edge `0.1258` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.6552` n `33` status `ready` deltaP `15.6412` edge `0.1258` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.4353` n `33` status `ready` deltaP `18.4405` edge `0.1172` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4353` n `33` status `ready` deltaP `18.4405` edge `0.1172` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.073` n `33` status `ready` deltaP `18.3481` edge `0.0709` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.073` n `33` status `ready` deltaP `18.3481` edge `0.0709` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0608` n `33` status `ready` deltaP `12.5114` edge `0.028` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0608` n `33` status `ready` deltaP `12.5114` edge `0.028` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8624` n `33` status `ready` deltaP `5.6679` edge `0.1559` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8624` n `33` status `ready` deltaP `5.6679` edge `0.1559` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3577` n `33` status `ready` deltaP `9.0365` edge `0.0232` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3577` n `33` status `ready` deltaP `9.0365` edge `0.0232` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2634` n `33` status `ready` deltaP `8.2472` edge `0.0023` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2634` n `33` status `ready` deltaP `8.2472` edge `0.0023` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1814` n `33` status `ready` deltaP `4.2824` edge `-0.0214` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1814` n `33` status `ready` deltaP `4.2824` edge `-0.0214` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
