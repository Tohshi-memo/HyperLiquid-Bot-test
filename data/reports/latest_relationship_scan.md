# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T04:52:27.158850+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `366.2205` n `50` status `ready` deltaP `11.3234` edge `30.4478` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.474` n `50` status `ready` deltaP `10.9756` edge `24.383` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.4004` n `50` status `ready` deltaP `23.3056` edge `0.965` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.5794` n `70` status `ready` deltaP `33.7351` edge `0.7052` maxDD `-2.8784`
- `news_risk_high->crypto_alt_24h` score `9.2788` n `70` status `ready` deltaP `17.877` edge `0.8499` maxDD `-11.3342`
- `market_context_high->crypto_major_24h` score `9.0526` n `50` status `ready` deltaP `31.3056` edge `0.6873` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `8.0039` n `90` status `ready` deltaP `30.8502` edge `0.4931` maxDD `-0.8755`
- `news_risk_high->crypto_alt_4h` score `7.7428` n `90` status `ready` deltaP `31.8971` edge `0.567` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2685` n `50` status `ready` deltaP `16.628` edge `0.5652` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8755` n `50` status `ready` deltaP `16.3415` edge `0.5096` maxDD `-7.6465`
- `news_risk_high->crypto_major_24h` score `4.2948` n `70` status `ready` deltaP `12.1627` edge `0.5076` maxDD `-14.1297`
- `news_risk_high->index_24h` score `3.6844` n `70` status `ready` deltaP `31.7857` edge `0.111` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.4624` n `90` status `ready` deltaP `27.5846` edge `0.1659` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1726` n `50` status `ready` deltaP `14.2036` edge `0.236` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9713` n `50` status `ready` deltaP `13.2515` edge `0.2043` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7531` n `50` status `ready` deltaP `30.7073` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.3023` n `90` status `ready` deltaP `11.4737` edge `0.1509` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.8647` n `90` status `ready` deltaP `8.2036` edge `0.1526` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4112` n `50` status `ready` deltaP `19.8922` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_4h` score `1.2721` n `90` status `ready` deltaP `12.2426` edge `0.0868` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
