# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T01:22:36.574360+00:00`
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

- `market_context_high->unknown_1h` score `338.6532` n `50` status `ready` deltaP `9.5269` edge `28.1625` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.6767` n `50` status `ready` deltaP `8.9939` edge `23.9131` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.1703` n `81` status `ready` deltaP `38.1559` edge `1.3641` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.9276` n `50` status `ready` deltaP `35.9931` edge `0.8123` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2017` n `50` status `ready` deltaP `18.7622` edge `0.5454` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `7.0433` n `50` status `ready` deltaP `14.625` edge `0.6604` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.9308` n `50` status `ready` deltaP `16.189` edge `0.4323` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5554` n `50` status `ready` deltaP `18.3472` edge `0.5197` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.2436` n `81` status `ready` deltaP `14.4869` edge `0.4891` maxDD `-15.8971`
- `news_risk_high->crypto_alt_4h` score `3.083` n `94` status `ready` deltaP `12.1464` edge `0.3103` maxDD `-6.4152`
- `market_context_high->crypto_major_1h` score `3.0719` n `50` status `ready` deltaP `15.0479` edge `0.2007` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9626` n `50` status `ready` deltaP `13.7545` edge `0.2215` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9045` n `50` status `ready` deltaP `32.689` edge `0.0376` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.7027` n `94` status `ready` deltaP `24.0042` edge `0.1348` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `2.6088` n `81` status `ready` deltaP `17.0139` edge `0.428` maxDD `-8.5571`
- `news_risk_high->commodity_24h` score `1.7137` n `81` status `ready` deltaP `27.1219` edge `0.1513` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.4852` n `81` status `ready` deltaP `15.4513` edge `0.2148` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->index_24h` score `1.3624` n `81` status `ready` deltaP `17.6312` edge `0.0438` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9206` n `50` status `ready` deltaP `14.7917` edge `0.0765` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
