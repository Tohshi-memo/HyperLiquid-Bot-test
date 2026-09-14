# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T01:07:30.050327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11058`

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

- `news_risk_high->unknown_1h` score `442.2412` n `82` status `ready` deltaP `-5.6996` edge `36.9336` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `19.1178` n `82` status `ready` deltaP `36.8923` edge `1.396` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3424` n `82` status `ready` deltaP `38.0236` edge `1.4221` maxDD `-9.098`
- `news_risk_high->equity_24h` score `10.6558` n `82` status `ready` deltaP `31.7536` edge `0.8543` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.6825` n `82` status `ready` deltaP `55.5256` edge `0.2877` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `5.957` n `56` status `ready` deltaP `39.8276` edge `0.2309` maxDD `0.0`
- `risk_on_high->fx_24h` score `5.5922` n `32` status `ready` deltaP `62.3922` edge `0.0543` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.5922` n `32` status `ready` deltaP `62.3922` edge `0.0543` maxDD `-0.0054`
- `risk_on_high->commodity_24h` score `5.4326` n `32` status `ready` deltaP `39.8276` edge `0.1872` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4326` n `32` status `ready` deltaP `39.8276` edge `0.1872` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.1148` n `82` status `ready` deltaP `29.9327` edge `0.2721` maxDD `-0.6334`
- `market_context_high->fx_24h` score `2.9668` n `56` status `ready` deltaP `53.0172` edge `0.0553` maxDD `-0.2714`
- `risk_on_high->commodity_4h` score `1.8555` n `51` status `ready` deltaP `25.9505` edge `0.0166` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8555` n `51` status `ready` deltaP `25.9505` edge `0.0166` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7081` n `125` status `ready` deltaP `21.9976` edge `0.0375` maxDD `-0.345`
- `risk_on_high->crypto_alt_24h` score `1.0538` n `32` status `ready` deltaP `-2.2845` edge `0.271` maxDD `-9.7698`
- `risk_on_and_context->crypto_alt_24h` score `1.0538` n `32` status `ready` deltaP `-2.2845` edge `0.271` maxDD `-9.7698`
- `market_context_high->commodity_1h` score `0.6316` n `137` status `ready` deltaP `11.4647` edge `0.0139` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5176` n `82` status `ready` deltaP `14.0244` edge `0.0357` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.2516` n `125` status `ready` deltaP `10.3439` edge `0.0109` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
