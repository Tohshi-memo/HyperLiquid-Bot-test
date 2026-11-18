# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T20:52:33.391860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2292`

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

- `market_context_high->unknown_24h` score `1367.9505` n `98` status `ready` deltaP `4.1667` edge `113.9681` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.4115` n `98` status `ready` deltaP `39.594` edge `1.7825` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.4798` n `98` status `ready` deltaP `24.4402` edge `1.5212` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3224` n `98` status `ready` deltaP `1.5795` edge `0.0083` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4177` n `98` status `ready` deltaP `15.3557` edge `0.1853` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5826` n `98` status `ready` deltaP `11.6196` edge `0.0047` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.6016` n `98` status `ready` deltaP `1.1822` edge `0.196` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.8775` n `98` status `ready` deltaP `-2.1753` edge `0.0007` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9458` n `98` status `ready` deltaP `-1.7733` edge `0.2488` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1323` n `98` status `ready` deltaP `-1.5092` edge `0.0152` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3544` n `98` status `ready` deltaP `-8.5971` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9018` n `98` status `ready` deltaP `0.2597` edge `0.0265` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5162` n `98` status `ready` deltaP `-8.6921` edge `-0.0174` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8636` n `98` status `ready` deltaP `1.4573` edge `-0.0306` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9426` n `98` status `ready` deltaP `-15.9721` edge `-0.034` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.5072` n `98` status `ready` deltaP `-24.2347` edge `-0.0098` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.754` n `98` status `ready` deltaP `-18.8138` edge `-0.0065` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.3852` n `98` status `ready` deltaP `-23.9049` edge `-0.11` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.087` n `98` status `ready` deltaP `-16.2486` edge `-0.1067` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.9113` n `98` status `ready` deltaP `-14.1239` edge `-0.2164` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
