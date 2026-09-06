# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T17:37:27.416512+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10135`

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

- `risk_on_high->unknown_24h` score `174.3833` n `105` status `ready` deltaP `25.2679` edge `14.3734` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `174.3833` n `105` status `ready` deltaP `25.2679` edge `14.3734` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `16.9623` n `105` status `ready` deltaP `30.6746` edge `1.395` maxDD `-11.2108`
- `risk_on_and_context->crypto_major_24h` score `16.9623` n `105` status `ready` deltaP `30.6746` edge `1.395` maxDD `-11.2108`
- `risk_on_high->crypto_alt_24h` score `7.9817` n `105` status `ready` deltaP `18.874` edge `0.7412` maxDD `-11.4838`
- `risk_on_and_context->crypto_alt_24h` score `7.9817` n `105` status `ready` deltaP `18.874` edge `0.7412` maxDD `-11.4838`
- `market_context_high->equity_24h` score `4.97` n `196` status `ready` deltaP `19.3878` edge `0.3824` maxDD `-4.1323`
- `market_context_high->crypto_alt_24h` score `4.7162` n `196` status `ready` deltaP `17.8536` edge `0.5012` maxDD `-12.8433`
- `risk_on_high->equity_24h` score `3.3557` n `105` status `ready` deltaP `14.5238` edge `0.2803` maxDD `-4.1323`
- `risk_on_and_context->equity_24h` score `3.3557` n `105` status `ready` deltaP `14.5238` edge `0.2803` maxDD `-4.1323`
- `market_context_high->index_24h` score `0.7546` n `196` status `ready` deltaP `16.9111` edge `0.0839` maxDD `-3.3673`
- `risk_on_high->index_24h` score `0.5615` n `105` status `ready` deltaP `13.4077` edge `0.0598` maxDD `-2.8579`
- `risk_on_and_context->index_24h` score `0.5615` n `105` status `ready` deltaP `13.4077` edge `0.0598` maxDD `-2.8579`
- `risk_on_high->index_1h` score `-0.0935` n `129` status `ready` deltaP `5.4182` edge `-0.0034` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0935` n `129` status `ready` deltaP `5.4182` edge `-0.0034` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.2086` n `129` status `ready` deltaP `3.2261` edge `0.0628` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2086` n `129` status `ready` deltaP `3.2261` edge `0.0628` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.3006` n `129` status `ready` deltaP `5.2314` edge `-0.0029` maxDD `-1.6408`
- `risk_on_and_context->metal_1h` score `-0.3006` n `129` status `ready` deltaP `5.2314` edge `-0.0029` maxDD `-1.6408`
- `risk_on_high->equity_1h` score `-0.3612` n `129` status `ready` deltaP `8.1071` edge `-0.0133` maxDD `-2.6312`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
