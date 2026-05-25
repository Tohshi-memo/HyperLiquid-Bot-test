# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T13:37:17.391838+00:00`
- Price records: `672`
- Market context records: `1846`
- Flow alert records: `7215`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.6992` n `196` status `ready` deltaP `22.0103` edge `0.526` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.1481` n `178` status `ready` deltaP `24.2919` edge `0.593` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.1339` n `196` status `ready` deltaP `25.4947` edge `0.4658` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.5405` n `196` status `ready` deltaP `18.2803` edge `0.4589` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.1074` n `178` status `ready` deltaP `15.9586` edge `0.2754` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.7087` n `178` status `ready` deltaP `14.56` edge `0.6607` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.4712` n `196` status `ready` deltaP `14.9981` edge `0.2154` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.134` n `178` status `ready` deltaP `12.9369` edge `0.4981` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.6187` n `196` status `ready` deltaP `11.0037` edge `0.0871` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3456` n `199` status `ready` deltaP `5.2975` edge `0.0921` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2534` n `178` status `ready` deltaP `19.3801` edge `0.7505` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1622` n `199` status `ready` deltaP `5.1583` edge `0.0905` maxDD `-4.9097`
- `market_context_high->fx_24h` score `-0.0209` n `178` status `ready` deltaP `12.1294` edge `0.0223` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0448` n `199` status `ready` deltaP `4.8371` edge `0.0434` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.3898` n `199` status `ready` deltaP `3.8862` edge `0.0368` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.525` n `199` status `ready` deltaP `6.1317` edge `0.0254` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5886` n `196` status `ready` deltaP `12.5902` edge `0.1362` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.599` n `199` status `ready` deltaP `-0.006` edge `0.0133` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7469` n `199` status `ready` deltaP `-4.6994` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0507` n `196` status `ready` deltaP `-5.8922` edge `-0.0066` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
