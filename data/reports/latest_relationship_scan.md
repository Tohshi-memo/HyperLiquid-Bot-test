# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T00:07:16.098311+00:00`
- Price records: `672`
- Market context records: `1893`
- Flow alert records: `7348`
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

- `market_context_high->crypto_alt_4h` score `7.2039` n `199` status `ready` deltaP `22.8137` edge `0.5627` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8095` n `199` status `ready` deltaP `27.7148` edge `0.5073` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3433` n `199` status `ready` deltaP `18.1104` edge `0.4436` maxDD `-9.8581`
- `market_context_high->metal_24h` score `2.7482` n `183` status `ready` deltaP `17.808` edge `0.3529` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3226` n `199` status `ready` deltaP `14.4296` edge `0.2068` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6584` n `183` status `ready` deltaP `12.8756` edge `0.5844` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.6334` n `183` status `ready` deltaP `10.3427` edge `0.19` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6081` n `199` status `ready` deltaP `7.0939` edge `0.102` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4087` n `199` status `ready` deltaP `9.7882` edge `0.0777` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.372` n `199` status `ready` deltaP `6.3559` edge `0.1` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.3108` n `183` status `ready` deltaP `15.5254` edge `0.0273` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0688` n `199` status `ready` deltaP `5.1365` edge `0.0394` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.1089` n `183` status `ready` deltaP `9.2356` edge `0.4192` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.3654` n `183` status `ready` deltaP `17.8848` edge `0.7089` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4767` n `199` status `ready` deltaP `6.8802` edge `0.0266` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5013` n `199` status `ready` deltaP `3.2874` edge `0.0315` maxDD `-3.6151`
- `market_context_high->index_1h` score `-0.6385` n `199` status `ready` deltaP `-0.1557` edge `0.011` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6978` n `199` status `ready` deltaP `-3.9509` edge `0.0001` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.7072` n `199` status `ready` deltaP `11.9331` edge `0.1307` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.9592` n `199` status `ready` deltaP `-4.734` edge `-0.0026` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
