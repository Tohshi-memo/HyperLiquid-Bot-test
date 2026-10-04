# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T12:22:31.161741+00:00`
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

- `market_context_high->unknown_4h` score `136.3151` n `79` status `ready` deltaP `4.8124` edge `11.3502` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `112.2945` n `91` status `ready` deltaP `-1.7651` edge `9.4111` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `11.4836` n `46` status `ready` deltaP `28.5251` edge `0.8941` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.0071` n `46` status `ready` deltaP `34.9637` edge `0.7494` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.7063` n `65` status `ready` deltaP `38.1918` edge `0.6579` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `9.4714` n `62` status `ready` deltaP `25.6665` edge `0.6282` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.2471` n `65` status `ready` deltaP `23.75` edge `0.58` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.1528` n `79` status `ready` deltaP `25.6309` edge `0.4122` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.2718` n `62` status `ready` deltaP `28.9931` edge `0.1627` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8692` n `65` status `ready` deltaP `26.3696` edge `0.2079` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.1026` n `65` status `ready` deltaP `33.743` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9832` n `65` status `ready` deltaP `12.8604` edge `0.1984` maxDD `-1.5096`
- `market_context_high->crypto_alt_4h` score `2.8924` n `79` status `ready` deltaP `9.5728` edge `0.3228` maxDD `-7.6465`
- `market_context_high->equity_24h` score `2.7087` n `46` status `ready` deltaP `6.0311` edge `0.2852` maxDD `-6.3081`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.4425` n `91` status `ready` deltaP `17.0363` edge `0.135` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.7669` edge `0.018` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6254` n `65` status `ready` deltaP `5.4675` edge `0.1509` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.0882` n `91` status `ready` deltaP `16.5296` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
