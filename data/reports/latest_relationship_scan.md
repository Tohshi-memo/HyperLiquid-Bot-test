# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T00:07:27.428501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12438`

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

- `news_risk_high->unknown_1h` score `438.034` n `82` status `ready` deltaP `-5.6996` edge `36.583` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.0206` n `82` status `ready` deltaP `36.8923` edge `1.3879` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3472` n `82` status `ready` deltaP `38.0236` edge `1.4225` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.4242` n `82` status `ready` deltaP `31.0639` edge `0.8396` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.5901` n `82` status `ready` deltaP `54.836` edge `0.2846` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.5598` n `56` status `ready` deltaP `39.8276` edge `0.1978` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.0368` n `82` status `ready` deltaP `29.2431` edge `0.2702` maxDD `-0.6334`
- `market_context_high->fx_24h` score `2.2797` n `56` status `ready` deltaP `46.564` edge `0.0377` maxDD `-1.1356`
- `risk_on_high->commodity_4h` score `1.8929` n `51` status `ready` deltaP `26.1029` edge `0.0187` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8929` n `51` status `ready` deltaP `26.1029` edge `0.0187` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5471` n `125` status `ready` deltaP `21.35` edge `0.0284` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.4853` n `82` status `ready` deltaP `13.5671` edge `0.0346` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.4147` n `137` status `ready` deltaP `9.1438` edge `0.0113` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.1809` n `52` status `ready` deltaP `6.4487` edge `0.0073` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.141` n `125` status `ready` deltaP `8.4012` edge `0.0097` maxDD `-0.1435`
- `risk_on_high->metal_1h` score `0.0532` n `52` status `ready` deltaP `4.9171` edge `0.0046` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.0532` n `52` status `ready` deltaP `4.9171` edge `0.0046` maxDD `-0.1115`
- `risk_on_high->fx_1h` score `-0.0696` n `52` status `ready` deltaP `2.0958` edge `0.0025` maxDD `-0.0318`
- `risk_on_and_context->fx_1h` score `-0.0696` n `52` status `ready` deltaP `2.0958` edge `0.0025` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
