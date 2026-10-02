# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T01:52:28.595954+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.7204` n `50` status `ready` deltaP `9.5269` edge `28.1681` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.8867` n `50` status `ready` deltaP `8.9939` edge `23.9306` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8499` n `79` status `ready` deltaP `38.4406` edge `1.3355` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.9931` n `50` status `ready` deltaP `36.1667` edge `0.8166` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.2115` n `50` status `ready` deltaP `14.9722` edge `0.6721` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `7.1485` n `50` status `ready` deltaP `18.4573` edge `0.543` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8752` n `50` status `ready` deltaP `15.8841` edge `0.4297` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5092` n `50` status `ready` deltaP `18.0` edge `0.5161` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.3198` n `92` status `ready` deltaP `13.2754` edge `0.3225` maxDD `-6.4152`
- `market_context_high->crypto_major_1h` score `3.0647` n `50` status `ready` deltaP `15.0479` edge `0.2001` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9338` n `50` status `ready` deltaP `13.6048` edge `0.2201` maxDD `-3.6387`
- `news_risk_high->crypto_major_24h` score `2.9303` n `79` status `ready` deltaP `13.6604` edge `0.4685` maxDD `-15.8971`
- `market_context_high->fx_4h` score `2.9009` n `50` status `ready` deltaP `32.689` edge `0.0373` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `2.8562` n `79` status `ready` deltaP `18.3544` edge `0.4344` maxDD `-7.9138`
- `news_risk_high->equity_4h` score `2.6418` n `92` status `ready` deltaP `23.648` edge `0.1321` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.6458` n `79` status `ready` deltaP `26.3405` edge `0.1478` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.4262` n `79` status `ready` deltaP `14.3922` edge `0.2143` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.2809` n `79` status `ready` deltaP `16.9436` edge `0.0416` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9214` n `50` status `ready` deltaP `14.7917` edge `0.0766` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
