# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T12:37:25.001506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `132.2478` n `80` status `ready` deltaP `3.8415` edge `11.0219` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `109.2964` n `92` status `ready` deltaP `-1.5621` edge `9.1599` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.3749` n `46` status `ready` deltaP `28.3515` edge `0.8862` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.9188` n `46` status `ready` deltaP `34.7901` edge `0.7432` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.6737` n `65` status `ready` deltaP `38.0394` edge `0.6562` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.3385` n `63` status `ready` deltaP `25.5952` edge `0.6176` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.2411` n `65` status `ready` deltaP `23.75` edge `0.5795` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.102` n `80` status `ready` deltaP `25.7317` edge `0.4073` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.2184` n `63` status `ready` deltaP `28.8194` edge `0.1594` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8558` n `65` status `ready` deltaP `26.2171` edge `0.2078` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1026` n `65` status `ready` deltaP `33.743` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9616` n `65` status `ready` deltaP `12.7107` edge `0.1976` maxDD `-1.5096`
- `market_context_high->crypto_alt_4h` score `2.6494` n `80` status `ready` deltaP `8.75` edge `0.3122` maxDD `-7.6465`
- `market_context_high->equity_24h` score `2.6396` n `46` status `ready` deltaP `5.8574` edge `0.2806` maxDD `-6.3081`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4335` n `92` status `ready` deltaP `17.2091` edge `0.1331` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0854` n `65` status `ready` deltaP `25.6172` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5978` n `65` status `ready` deltaP `5.3178` edge `0.1496` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.1207` n `92` status `ready` deltaP `16.9357` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
