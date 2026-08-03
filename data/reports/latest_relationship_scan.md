# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T03:52:24.154885+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3406.6215` n `47` status `ready` deltaP `21.8713` edge `283.7814` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.8495` n `40` status `ready` deltaP `51.4583` edge `0.8508` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1318` n `40` status `ready` deltaP `51.3194` edge `0.5983` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.8018` n `47` status `ready` deltaP `4.7029` edge `0.2785` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.1853` n `47` status `ready` deltaP `11.3908` edge `0.0609` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3658` n `47` status `ready` deltaP `7.5646` edge `0.0339` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3395` n `47` status `ready` deltaP `5.0338` edge `0.0946` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.2941` n `47` status `ready` deltaP `8.5074` edge `0.0161` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.1394` n `47` status `ready` deltaP `5.9498` edge `0.0102` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0692` n `47` status `ready` deltaP `5.0516` edge `0.0075` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `0.0216` n `47` status `ready` deltaP `4.5388` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->equity_1h` score `0.017` n `47` status `ready` deltaP `3.2552` edge `0.062` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.0123` n `47` status `ready` deltaP `13.7228` edge `-0.0048` maxDD `-1.8531`
- `market_context_high->fx_1h` score `-0.024` n `47` status `ready` deltaP `6.6664` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->commodity_1h` score `-0.1165` n `47` status `ready` deltaP `7.5646` edge `-0.016` maxDD `-1.6161`
- `market_context_high->crypto_alt_4h` score `-0.218` n `47` status `ready` deltaP `2.2963` edge `0.0473` maxDD `-4.9116`
- `news_risk_high->fx_4h` score `-0.277` n `47` status `ready` deltaP `5.2121` edge `0.0255` maxDD `-0.6604`
- `news_risk_high->crypto_alt_1h` score `-0.3809` n `47` status `ready` deltaP `2.5608` edge `0.0023` maxDD `-3.1233`
- `news_risk_high->crypto_major_1h` score `-0.5355` n `47` status `ready` deltaP `2.8602` edge `-0.0157` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.7007` n `40` status `ready` deltaP `0.6597` edge `0.0352` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
