# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T18:37:27.074501+00:00`
- Price records: `672`
- Market context records: `7591`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14550`

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

- `market_context_high->commodity_24h` score `0.2068` n `145` status `ready` deltaP `14.5019` edge `0.0789` maxDD `-7.0012`
- `market_context_high->unknown_24h` score `0.0848` n `146` status `ready` deltaP `11.4155` edge `0.1046` maxDD `-6.9198`
- `market_context_high->commodity_4h` score `0.0231` n `152` status `ready` deltaP `8.3897` edge `0.022` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0053` n `152` status `ready` deltaP `5.6346` edge `0.0106` maxDD `-0.9072`
- `market_context_high->commodity_1h` score `-0.2331` n `152` status `ready` deltaP `5.2493` edge `0.0028` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.3479` n `145` status `ready` deltaP `9.2803` edge `0.0179` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `-0.4814` n `152` status `ready` deltaP `0.2994` edge `0.0109` maxDD `-3.6359`
- `market_context_high->crypto_major_1h` score `-0.4965` n `152` status `ready` deltaP `6.1298` edge `0.0107` maxDD `-5.5504`
- `market_context_high->metal_1h` score `-0.6291` n `152` status `ready` deltaP `1.4694` edge `0.0141` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6581` n `152` status `ready` deltaP `8.9188` edge `0.0288` maxDD `-3.4775`
- `market_context_high->equity_1h` score `-0.6697` n `152` status `ready` deltaP `5.4272` edge `0.0475` maxDD `-8.8965`
- `market_context_high->fx_1h` score `-0.7072` n `152` status `ready` deltaP `-1.0945` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->unknown_1h` score `-0.9442` n `152` status `ready` deltaP `0.2403` edge `-0.0603` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.2225` n `152` status `ready` deltaP `1.1634` edge `0.0453` maxDD `-10.1158`
- `market_context_high->equity_24h` score `-1.4593` n `145` status `ready` deltaP `16.9771` edge `0.4862` maxDD `-56.5842`
- `market_context_high->crypto_major_4h` score `-1.4999` n `152` status `ready` deltaP `6.9319` edge `0.0539` maxDD `-16.3928`
- `market_context_high->metal_4h` score `-1.7099` n `152` status `ready` deltaP `-2.0138` edge `0.0424` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.7745` n `152` status `ready` deltaP `1.7886` edge `0.1973` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.397` n `152` status `ready` deltaP `-4.1828` edge `-0.0034` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.5497` n `152` status `ready` deltaP `11.5132` edge `-0.187` maxDD `-4.6641`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
