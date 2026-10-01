# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T14:52:28.459875+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6894`

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

- `market_context_high->unknown_1h` score `333.731` n `50` status `ready` deltaP `7.8802` edge `27.7633` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `283.2172` n `50` status `ready` deltaP `6.8598` edge `23.5557` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3643` n `114` status `ready` deltaP `33.1414` edge `1.4137` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.7325` n `50` status `ready` deltaP `31.4792` edge `0.7428` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3011` n `50` status `ready` deltaP `19.5244` edge `0.5486` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9946` n `50` status `ready` deltaP `16.3415` edge `0.4366` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.8666` n `114` status `ready` deltaP `21.409` edge `0.5782` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.1357` n `50` status `ready` deltaP `8.8958` edge `0.4563` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.8845` n `50` status `ready` deltaP `18.3472` edge `0.5619` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4363` n `127` status `ready` deltaP `26.7837` edge `0.1774` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `3.1701` n `114` status `ready` deltaP `22.277` edge `0.4928` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.1068` n `50` status `ready` deltaP `35.128` edge `0.0382` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0167` n `50` status `ready` deltaP `14.7485` edge `0.1981` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9386` n `50` status `ready` deltaP `13.6048` edge `0.2205` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4531` n `114` status `ready` deltaP `23.931` edge `0.0927` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2769` n `114` status `ready` deltaP `26.6721` edge `0.2415` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5226` n `50` status `ready` deltaP `21.2395` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8436` n `127` status `ready` deltaP `8.4233` edge `0.0678` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7722` n `50` status `ready` deltaP `13.2292` edge `0.0679` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5398` n `50` status `ready` deltaP `14.4306` edge `0.0748` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
