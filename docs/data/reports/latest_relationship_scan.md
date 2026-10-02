# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T03:07:31.715444+00:00`
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

- `market_context_high->unknown_1h` score `338.8332` n `50` status `ready` deltaP `9.5269` edge `28.1775` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0151` n `50` status `ready` deltaP `8.9939` edge `23.9413` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.8187` n `74` status `ready` deltaP `38.6167` edge `1.2484` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0531` n `50` status `ready` deltaP `36.1667` edge `0.8216` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.5476` n `50` status `ready` deltaP `15.3194` edge `0.6978` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9987` n `50` status `ready` deltaP `17.6951` edge `0.5356` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7669` n `50` status `ready` deltaP `15.5793` edge `0.4227` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5526` n `87` status `ready` deltaP `13.3954` edge `0.3411` maxDD `-6.4152`
- `news_risk_high->equity_24h` score `3.5058` n `74` status `ready` deltaP `22.1049` edge `0.452` maxDD `-6.3257`
- `market_context_high->equity_24h` score `3.39` n `50` status `ready` deltaP `17.1319` edge `0.5066` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `2.9352` n `50` status `ready` deltaP `14.2994` edge `0.1943` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8997` n `50` status `ready` deltaP `32.689` edge `0.0372` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8139` n `50` status `ready` deltaP `13.1557` edge `0.2131` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3723` n `87` status `ready` deltaP `22.2736` edge `0.1188` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.4968` n `74` status `ready` deltaP `24.3759` edge `0.1418` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_24h` score `1.3451` n `74` status `ready` deltaP `10.9235` edge `0.415` maxDD `-15.8971`
- `news_risk_high->metal_24h` score `1.2307` n `74` status `ready` deltaP `11.4114` edge `0.2091` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.0488` n `74` status `ready` deltaP `15.062` edge `0.0348` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9237` n `50` status `ready` deltaP `14.7917` edge `0.0769` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
