# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T20:37:16.441762+00:00`
- Price records: `672`
- Market context records: `1973`
- Flow alert records: `7573`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.399` n `234` status `ready` deltaP `22.7173` edge `0.5796` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.789` n `234` status `ready` deltaP `26.1987` edge `0.5157` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4407` n `234` status `ready` deltaP `13.4381` edge `0.3162` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2668` n `234` status `ready` deltaP `14.3632` edge `0.2026` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.5445` n `199` status `ready` deltaP `16.7627` edge `0.549` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.3771` n `199` status `ready` deltaP `15.0693` edge `0.2569` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.9728` n `234` status `ready` deltaP `9.1023` edge `0.119` maxDD `-3.2225`
- `market_context_high->equity_24h` score `0.8317` n `199` status `ready` deltaP `13.7477` edge `0.4675` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7644` n `234` status `ready` deltaP `7.9457` edge `0.1221` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4153` n `199` status `ready` deltaP `4.1922` edge `0.1295` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1559` n `234` status `ready` deltaP `7.678` edge `0.0707` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0766` n `234` status `ready` deltaP `5.0988` edge `0.039` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.194` n `199` status `ready` deltaP `10.446` edge `0.0191` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.2539` n `199` status `ready` deltaP `18.2893` edge `0.7155` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.6113` n `234` status `ready` deltaP `0.3353` edge `0.01` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1198` n `234` status `ready` deltaP `-7.6871` edge `-0.0035` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3072` n `234` status `ready` deltaP `3.0977` edge `0.004` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4856` n `234` status `ready` deltaP `0.8087` edge `-0.034` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8627` n `234` status `ready` deltaP `2.3082` edge `0.0016` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
