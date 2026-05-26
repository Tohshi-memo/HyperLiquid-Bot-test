# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T00:22:18.913516+00:00`
- Price records: `672`
- Market context records: `1894`
- Flow alert records: `7351`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.2413` n `199` status `ready` deltaP `22.9662` edge `0.5648` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8349` n `199` status `ready` deltaP `27.8672` edge `0.5084` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3421` n `199` status `ready` deltaP `18.1104` edge `0.4435` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.693` n `183` status `ready` deltaP `17.808` edge `0.3483` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3298` n `199` status `ready` deltaP `14.4296` edge `0.2074` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6572` n `183` status `ready` deltaP `12.8756` edge `0.5843` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.6051` n `183` status `ready` deltaP `10.1691` edge `0.1888` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6345` n `199` status `ready` deltaP `7.2436` edge `0.1032` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4123` n `199` status `ready` deltaP `9.7882` edge `0.078` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.3972` n `199` status `ready` deltaP `6.5056` edge `0.1011` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.3108` n `183` status `ready` deltaP `15.5254` edge `0.0273` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0472` n `199` status `ready` deltaP `5.2862` edge `0.0402` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.1276` n `183` status `ready` deltaP `9.0619` edge `0.4188` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.3666` n `183` status `ready` deltaP `17.8848` edge `0.7088` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.472` n `199` status `ready` deltaP `6.8802` edge `0.0272` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.4845` n `199` status `ready` deltaP `3.4371` edge `0.0319` maxDD `-3.6151`
- `market_context_high->index_1h` score `-0.6349` n `199` status `ready` deltaP `-0.1557` edge `0.0113` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6885` n `199` status `ready` deltaP `-3.8012` edge `0.0003` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.7192` n `199` status `ready` deltaP `11.9331` edge `0.1297` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.9498` n `199` status `ready` deltaP `-4.5816` edge `-0.0024` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
