# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T09:07:27.373757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `news_risk_high->unknown_24h` score `52.0376` n `54` status `ready` deltaP `16.0301` edge `4.2656` maxDD `-1.5469`
- `news_risk_high->crypto_alt_24h` score `26.9204` n `54` status `ready` deltaP `39.4097` edge `2.1413` maxDD `-10.853`
- `market_context_high->unknown_24h` score `8.2239` n `118` status `ready` deltaP `16.6578` edge `0.6475` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2371` n `80` status `ready` deltaP `10.6707` edge `0.5076` maxDD `-1.7183`
- `news_risk_high->crypto_major_24h` score `5.0003` n `54` status `ready` deltaP `21.875` edge `0.4498` maxDD `-12.3153`
- `market_context_high->metal_24h` score `3.7106` n `118` status `ready` deltaP `30.6202` edge `0.207` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `3.2065` n `54` status `ready` deltaP `24.4792` edge `0.4036` maxDD `-9.7902`
- `news_risk_high->unknown_1h` score `2.656` n `80` status `ready` deltaP `5.524` edge `0.2202` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.6023` n `118` status `ready` deltaP `19.569` edge `0.1271` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.3169` n `80` status `ready` deltaP `33.9024` edge `0.022` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `2.0647` n `54` status `ready` deltaP `38.3101` edge `0.0562` maxDD `-2.4188`
- `news_risk_high->index_24h` score `1.6748` n `54` status `ready` deltaP `20.8912` edge `0.0306` maxDD `-0.7583`
- `market_context_high->unknown_1h` score `1.2588` n `119` status `ready` deltaP `9.4526` edge `0.0869` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6501` n `80` status `ready` deltaP `13.1437` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.482` n `80` status `ready` deltaP `13.2485` edge `0.0055` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1646` n `118` status `ready` deltaP `9.1076` edge `0.0099` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3477` n `119` status `ready` deltaP `4.4042` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->commodity_4h` score `-0.5632` n `80` status `ready` deltaP `7.6524` edge `0.0109` maxDD `-2.0635`
- `news_risk_high->index_4h` score `-0.5697` n `80` status `ready` deltaP `1.1585` edge `-0.0166` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
