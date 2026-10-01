# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T09:52:30.525808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6886`

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

- `market_context_high->unknown_1h` score `324.2788` n `50` status `ready` deltaP `7.1317` edge `26.9806` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9756` n `50` status `ready` deltaP `6.8598` edge `23.3689` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.1695` n `124` status `ready` deltaP `29.8107` edge `1.503` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.9302` n `48` status `ready` deltaP `32.9861` edge `0.6659` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.6153` n `50` status `ready` deltaP `18.1524` edge `0.5006` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.0264` n `124` status `ready` deltaP `22.9782` edge `0.5839` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.3683` n `124` status `ready` deltaP `29.1454` edge `0.2186` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.2464` n `124` status `ready` deltaP `21.7629` edge `0.7147` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.5689` n `50` status `ready` deltaP `13.4451` edge `0.3371` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.3213` n `48` status `ready` deltaP `15.4514` edge `0.509` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.0981` n `124` status `ready` deltaP `12.7999` edge `0.3735` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.957` n `50` status `ready` deltaP `33.4512` edge `0.0369` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.826` n `50` status `ready` deltaP `14.2994` edge `0.1852` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.6265` n `124` status `ready` deltaP `24.7928` edge `0.1014` maxDD `-0.4916`
- `market_context_high->crypto_alt_24h` score `2.5542` n `48` status `ready` deltaP `8.5069` edge `0.3271` maxDD `-11.6768`
- `market_context_high->crypto_alt_1h` score `2.4984` n `50` status `ready` deltaP `12.1078` edge `0.1938` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.2921` n `124` status `ready` deltaP `26.9041` edge `0.2419` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4448` n `50` status `ready` deltaP `20.3413` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.6959` n `131` status `ready` deltaP `7.0268` edge `0.0648` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.6902` n `48` status `ready` deltaP `15.9723` edge `0.0838` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
