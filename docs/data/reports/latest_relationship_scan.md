# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T14:22:23.044632+00:00`
- Price records: `672`
- Market context records: `1946`
- Flow alert records: `7497`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0977` n `231` status `ready` deltaP `22.0108` edge `0.5592` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5118` n `231` status `ready` deltaP `25.5679` edge `0.4968` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.5308` n `231` status `ready` deltaP `14.1436` edge `0.319` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9514` n `231` status `ready` deltaP `13.7655` edge `0.1803` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7948` n `199` status `ready` deltaP `15.2216` edge `0.4968` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.721` n `234` status `ready` deltaP `7.755` edge `0.107` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5449` n `234` status `ready` deltaP `7.0475` edge `0.1098` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2186` n `199` status `ready` deltaP `11.9871` edge `0.1809` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1369` n `199` status `ready` deltaP `4.1922` edge `0.1063` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1243` n `231` status `ready` deltaP `8.364` edge `0.0635` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2014` n `234` status `ready` deltaP `4.6497` edge `0.0316` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2711` n `199` status `ready` deltaP `9.9323` edge `0.0161` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5861` n `234` status `ready` deltaP `0.7844` edge `0.0091` maxDD `-1.7205`
- `market_context_high->equity_24h` score `-0.6352` n `199` status `ready` deltaP `9.4669` edge `0.3738` maxDD `-33.1875`
- `market_context_high->fx_1h` score `-0.6498` n `234` status `ready` deltaP `-3.0132` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0294` n `231` status `ready` deltaP `-6.1272` edge `-0.0023` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1692` n `234` status `ready` deltaP `3.5468` edge `0.0125` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4843` n `234` status `ready` deltaP `0.5093` edge `-0.0319` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.7207` n `231` status `ready` deltaP `7.049` edge `0.0788` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.9804` n `234` status `ready` deltaP `0.9609` edge `-0.0045` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
