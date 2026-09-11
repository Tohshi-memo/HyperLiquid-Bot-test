# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T22:22:27.179377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11335`

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

- `news_risk_high->unknown_1h` score `468.3667` n `75` status `ready` deltaP `-4.511` edge `39.1028` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.441` n `91` status `ready` deltaP `42.7694` edge `1.7746` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.441` n `91` status `ready` deltaP `42.7694` edge `1.7746` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.2046` n `34` status `ready` deltaP `49.52` edge `1.6103` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.5314` n `151` status `ready` deltaP `37.6679` edge `1.6259` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `13.1227` n `34` status `ready` deltaP `21.7933` edge `0.9929` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `9.7976` n `34` status `ready` deltaP `31.0968` edge `0.619` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.4347` n `91` status `ready` deltaP `36.9792` edge `0.5397` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4347` n `91` status `ready` deltaP `36.9792` edge `0.5397` maxDD `0.0`
- `market_context_high->equity_24h` score `9.1455` n `151` status `ready` deltaP `36.9792` edge `0.5156` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6489` n `91` status `ready` deltaP `42.5556` edge `0.4742` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6489` n `91` status `ready` deltaP `42.5556` edge `0.4742` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `7.8945` n `34` status `ready` deltaP `51.0417` edge `0.3176` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.691` n `91` status `ready` deltaP `25.021` edge `1.226` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.691` n `91` status `ready` deltaP `25.021` edge `1.226` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.6007` n `34` status `ready` deltaP `48.9787` edge `0.3162` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.6603` n `91` status `ready` deltaP `31.4393` edge `0.4313` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.6603` n `91` status `ready` deltaP `31.4393` edge `0.4313` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.3788` n `91` status `ready` deltaP `51.5644` edge `0.1087` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3788` n `91` status `ready` deltaP `51.5644` edge `0.1087` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
