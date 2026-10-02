# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T12:07:33.890291+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `341.8714` n `50` status `ready` deltaP `10.8743` edge `28.4217` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `291.3571` n `50` status `ready` deltaP `10.8232` edge `24.2076` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5394` n `73` status `ready` deltaP `39.795` edge `1.0506` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `10.121` n `73` status `ready` deltaP `35.01` edge `0.6585` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.9955` n `50` status `ready` deltaP `34.2569` edge `0.7462` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0357` n `50` status `ready` deltaP `16.5347` edge `0.8137` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.7055` n `50` status `ready` deltaP `16.4756` edge `0.5193` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7077` n `50` status `ready` deltaP `14.3598` edge `0.4259` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3611` n `109` status `ready` deltaP `18.6717` edge `0.3733` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9889` n `50` status `ready` deltaP `14.2036` edge `0.2207` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9455` n `50` status `ready` deltaP `32.8415` edge `0.04` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9232` n `50` status `ready` deltaP `14.0` edge `0.1953` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.4052` n `50` status `ready` deltaP `11.2292` edge `0.4197` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.3937` n `109` status `ready` deltaP `22.7959` edge `0.1171` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.1619` n `73` status `ready` deltaP `8.4213` edge `0.5364` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.5035` n `50` status `ready` deltaP `20.9401` edge `0.0121` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.253` n `73` status `ready` deltaP `12.1409` edge `0.2071` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.9608` n `109` status `ready` deltaP `12.6958` edge `0.2695` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8819` n `50` status `ready` deltaP `14.6181` edge `0.0727` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8298` n `116` status `ready` deltaP `5.1002` edge `0.0914` maxDD `-2.4998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
