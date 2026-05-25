# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T09:22:16.656976+00:00`
- Price records: `672`
- Market context records: `1829`
- Flow alert records: `7163`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9085` n `192` status `ready` deltaP `22.7515` edge `0.5385` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.7206` n `178` status `ready` deltaP `26.7225` edge `0.6245` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4535` n `192` status `ready` deltaP `26.3847` edge `0.4865` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.3938` n `30` status `ready` deltaP `28.6484` edge `0.4073` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.4321` n `192` status `ready` deltaP `17.0604` edge `0.458` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.5818` n `178` status `ready` deltaP `17.8683` edge `0.3022` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2314` n `30` status `ready` deltaP `24.5709` edge `0.1372` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9867` n `192` status `ready` deltaP `16.8064` edge `0.2463` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7183` n `178` status `ready` deltaP `14.56` edge `0.6615` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.2101` n `178` status `ready` deltaP `15.8883` edge `0.5681` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9011` n `30` status `ready` deltaP `21.6362` edge `-0.0015` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8182` n `192` status `ready` deltaP `12.0427` edge `0.0968` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4266` n `196` status `ready` deltaP `6.1897` edge `0.0929` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3014` n `196` status `ready` deltaP `6.373` edge `0.094` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.1677` n `30` status `ready` deltaP `7.9979` edge `0.0405` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `0.0033` n `178` status `ready` deltaP `18.3384` edge `0.7366` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.0232` n `196` status `ready` deltaP `4.8821` edge `0.0449` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1219` n `178` status `ready` deltaP `11.7822` edge `0.0162` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.466` n `30` status `ready` deltaP `16.2575` edge `-0.1209` maxDD `-2.1115`
- `news_risk_high->fx_1h` score `-0.5302` n `30` status `ready` deltaP `-6.1776` edge `-0.0006` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
