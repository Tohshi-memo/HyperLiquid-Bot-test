# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T15:21:51.233693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->crypto_alt_24h` score `12.1869` n `39` status `ready` deltaP `52.5508` edge `0.6826` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.4845` n `39` status `ready` deltaP `53.6458` edge `0.5994` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.1348` n `31` status `ready` deltaP `-7.2777` edge `0.2115` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9583` n `31` status `ready` deltaP `20.1371` edge `0.0098` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9437` n `31` status `ready` deltaP `12.192` edge `0.0626` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.3804` n `46` status `ready` deltaP `5.6402` edge `0.0958` maxDD `-2.7703`
- `news_risk_high->commodity_4h` score `0.3083` n `31` status `ready` deltaP `13.7047` edge `-0.0156` maxDD `-1.6728`
- `market_context_high->commodity_1h` score `0.3028` n `46` status `ready` deltaP `6.743` edge `0.0313` maxDD `-1.3282`
- `news_risk_high->index_4h` score `0.1462` n `31` status `ready` deltaP `-0.3688` edge `0.0527` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1383` n `31` status `ready` deltaP `4.8928` edge `0.0354` maxDD `-0.356`
- `market_context_high->fx_1h` score `0.0539` n `46` status `ready` deltaP `7.5696` edge `-0.0088` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0478` n `31` status `ready` deltaP `2.8926` edge `-0.0056` maxDD `-0.5845`
- `market_context_high->fx_4h` score `-0.0634` n `46` status `ready` deltaP `12.9573` edge `-0.006` maxDD `-1.8531`
- `news_risk_high->crypto_alt_1h` score `-0.1003` n `31` status `ready` deltaP `10.3921` edge `-0.0181` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2521` n `31` status `ready` deltaP `-0.565` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5732` n `31` status `ready` deltaP `-2.2117` edge `-0.0011` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.5931` n `39` status `ready` deltaP `1.1084` edge `0.0396` maxDD `-2.3798`
- `news_risk_high->metal_4h` score `-0.9379` n `31` status `ready` deltaP `-4.2289` edge `-0.0154` maxDD `-0.7654`
- `news_risk_high->crypto_major_1h` score `-0.9429` n `31` status `ready` deltaP `2.2117` edge `-0.0636` maxDD `-3.762`
- `news_risk_high->index_24h` score `-1.1579` n `31` status `ready` deltaP `7.4429` edge `-0.1056` maxDD `-3.7303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
