# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T06:52:28.410412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5903`

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

- `news_risk_high->unknown_24h` score `538.9701` n `35` status `ready` deltaP `18.9533` edge `44.8299` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.0887` n `40` status `ready` deltaP `51.4583` edge `0.7874` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0214` n `40` status `ready` deltaP `51.3194` edge `0.5891` maxDD `-0.6889`
- `news_risk_high->commodity_1h` score `1.007` n `35` status `ready` deltaP `20.6672` edge `0.0125` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.6209` n `35` status `ready` deltaP `-9.1246` edge `0.2168` maxDD `-3.4427`
- `market_context_high->commodity_1h` score `0.3471` n `47` status `ready` deltaP `7.4149` edge `0.0325` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3021` n `47` status `ready` deltaP `5.0338` edge `0.0898` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.1808` n `35` status `ready` deltaP `-0.4007` edge `0.0558` maxDD `-0.3783`
- `news_risk_high->fx_24h` score `0.1782` n `35` status `ready` deltaP `8.874` edge `0.0445` maxDD `-2.1049`
- `news_risk_high->commodity_4h` score `0.1133` n `35` status `ready` deltaP `10.3833` edge `-0.0097` maxDD `-1.6728`
- `market_context_high->fx_4h` score `0.0183` n `47` status `ready` deltaP `13.7228` edge `-0.0043` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.0157` n `47` status `ready` deltaP `7.4149` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.0978` n `35` status `ready` deltaP `8.3405` edge `-0.0041` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.197` n `35` status `ready` deltaP `1.9295` edge `0.0308` maxDD `-0.514`
- `market_context_high->crypto_alt_4h` score `-0.2353` n `47` status `ready` deltaP `2.1439` edge `0.0461` maxDD `-4.9116`
- `news_risk_high->index_1h` score `-0.2887` n `35` status `ready` deltaP `-0.2181` edge `-0.0028` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.3476` n `35` status `ready` deltaP `-2.1899` edge `0.0015` maxDD `-0.1843`
- `news_risk_high->metal_1h` score `-0.4369` n `35` status `ready` deltaP `-2.6262` edge `-0.0065` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.6815` n `40` status `ready` deltaP `0.6597` edge `0.0368` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.8906` n `35` status `ready` deltaP `0.6672` edge `-0.0466` maxDD `-3.762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
