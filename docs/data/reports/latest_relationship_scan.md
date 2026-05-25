# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T14:07:20.182519+00:00`
- Price records: `672`
- Market context records: `1848`
- Flow alert records: `7222`
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

- `market_context_high->crypto_alt_4h` score `6.6484` n `196` status `ready` deltaP `21.7054` edge `0.5238` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0807` n `196` status `ready` deltaP `25.1898` edge `0.4634` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.9968` n `178` status `ready` deltaP `23.9447` edge `0.5827` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.5043` n `196` status `ready` deltaP `18.1278` edge `0.4569` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.0221` n `178` status `ready` deltaP `15.6114` edge `0.2706` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.6859` n `178` status `ready` deltaP `14.56` edge `0.6588` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.3736` n `196` status `ready` deltaP `14.6932` edge `0.2093` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.9983` n `178` status `ready` deltaP `12.5897` edge `0.4891` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.5583` n `196` status `ready` deltaP `10.6988` edge `0.0841` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2977` n `199` status `ready` deltaP `4.9981` edge `0.0901` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2371` n `178` status `ready` deltaP `19.2065` edge `0.7503` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1131` n `199` status `ready` deltaP `4.8589` edge `0.0884` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.0165` n `178` status `ready` deltaP `12.4766` edge `0.0231` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1035` n `199` status `ready` deltaP `4.6874` edge `0.0395` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4221` n `199` status `ready` deltaP `3.7365` edge `0.0351` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5452` n `199` status `ready` deltaP `5.982` edge `0.0238` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5946` n `196` status `ready` deltaP `12.5902` edge `0.1357` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6421` n `199` status `ready` deltaP `-0.3054` edge `0.0117` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7305` n `199` status `ready` deltaP `-4.4` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.046` n `196` status `ready` deltaP `-5.8922` edge `-0.006` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
