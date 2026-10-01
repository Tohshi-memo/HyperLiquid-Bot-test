# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T06:52:32.628173+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6722`

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

- `market_context_high->unknown_1h` score `324.7971` n `50` status `ready` deltaP `7.2814` edge `27.0228` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.116` n `50` status `ready` deltaP `6.8598` edge `23.3806` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3589` n `125` status `ready` deltaP `29.1292` edge `1.44` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.3519` n `36` status `ready` deltaP `28.4723` edge `0.6478` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.6017` n `50` status `ready` deltaP `17.8476` edge `0.5015` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.7866` n `125` status `ready` deltaP `23.0111` edge `0.5637` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.1614` n `125` status `ready` deltaP `27.8646` edge `0.2099` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.1457` n `125` status `ready` deltaP `22.3167` edge `0.6981` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.0161` n `36` status `ready` deltaP `11.2848` edge `0.4304` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `3.4557` n `50` status `ready` deltaP `13.1402` edge `0.3297` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9435` n `50` status `ready` deltaP `14.7485` edge `0.192` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9216` n `50` status `ready` deltaP `32.9939` edge `0.037` maxDD `-0.0791`
- `news_risk_high->crypto_alt_4h` score `2.7761` n `125` status `ready` deltaP `11.9402` edge `0.3524` maxDD `-10.7193`
- `market_context_high->crypto_alt_1h` score `2.6027` n `50` status `ready` deltaP `12.5569` edge `0.1995` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5729` n `125` status `ready` deltaP `24.5875` edge `0.0983` maxDD `-0.4916`
- `market_context_high->equity_24h` score `2.2909` n `36` status `ready` deltaP `6.9444` edge `0.4336` maxDD `-11.8957`
- `news_risk_high->metal_24h` score `2.126` n `125` status `ready` deltaP `25.1792` edge `0.2321` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4424` n `50` status `ready` deltaP `20.3413` edge `0.011` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7816` n `125` status `ready` deltaP `7.5581` edge `0.0684` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.6142` n `125` status `ready` deltaP `7.3569` edge `0.0932` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
