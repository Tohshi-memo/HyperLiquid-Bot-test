# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T08:22:24.277327+00:00`
- Price records: `672`
- Market context records: `4915`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_1h` score `15.471` n `107` status `ready` deltaP `9.8858` edge `1.2651` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.2707` n `107` status `ready` deltaP `25.4559` edge `0.7376` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.7025` n `107` status `ready` deltaP `21.7902` edge `0.5485` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.506` n `107` status `ready` deltaP `18.6417` edge `0.5403` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.4838` n `89` status `ready` deltaP `23.7515` edge `0.3329` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2925` n `107` status `ready` deltaP `9.8458` edge `0.1083` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9174` n `107` status `ready` deltaP `12.4444` edge `0.1728` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5334` n `107` status `ready` deltaP `6.528` edge `0.1287` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.4536` n `107` status `ready` deltaP `9.6008` edge `0.0404` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.3747` n `107` status `ready` deltaP `7.1227` edge `0.1028` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.3402` n `107` status `ready` deltaP `5.739` edge `0.0627` maxDD `-2.5875`
- `market_context_high->commodity_1h` score `-0.1499` n `107` status `ready` deltaP `4.5092` edge `0.0167` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2035` n `107` status `ready` deltaP `1.3697` edge `0.0319` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.548` n `107` status `ready` deltaP `-0.88` edge `0.0111` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7292` n `107` status `ready` deltaP `7.7246` edge `0.0064` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.8025` n `107` status `ready` deltaP `-1.4019` edge `0.0035` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-0.8655` n `107` status `ready` deltaP `-7.4543` edge `0.0` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.7135` n `89` status `ready` deltaP `-4.9743` edge `-0.0086` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.6617` n `89` status `ready` deltaP `15.9605` edge `0.016` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.7513` n `89` status `ready` deltaP `-8.0076` edge `-0.1472` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
