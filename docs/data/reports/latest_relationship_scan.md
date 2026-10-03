# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T04:07:27.870120+00:00`
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

- `market_context_high->unknown_1h` score `365.7597` n `50` status `ready` deltaP `11.3234` edge `30.4094` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.3705` n `50` status `ready` deltaP `10.6707` edge `24.3764` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.2857` n `70` status `ready` deltaP `21.6418` edge `0.9218` maxDD `-6.7152`
- `market_context_high->crypto_alt_24h` score `11.2387` n `50` status `ready` deltaP `22.7847` edge `0.955` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.4918` n `70` status `ready` deltaP `33.7351` edge `0.6979` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.9494` n `50` status `ready` deltaP `31.3056` edge `0.6787` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.7627` n `93` status `ready` deltaP `31.9056` edge `0.5686` maxDD `-6.4195`
- `news_risk_high->crypto_major_4h` score `7.6057` n `93` status `ready` deltaP `29.1208` edge `0.4765` maxDD `-0.9466`
- `market_context_high->crypto_major_4h` score `7.2371` n `50` status `ready` deltaP `16.4756` edge `0.5636` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `6.1275` n `70` status `ready` deltaP `12.1627` edge `0.5701` maxDD `-7.9114`
- `market_context_high->crypto_alt_4h` score `5.7922` n `50` status `ready` deltaP `15.8841` edge `0.5057` maxDD `-7.6465`
- `news_risk_high->index_24h` score `3.4748` n `70` status `ready` deltaP `30.5307` edge `0.1019` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.4203` n `93` status `ready` deltaP `27.6291` edge `0.1621` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1439` n `50` status `ready` deltaP `14.0539` edge `0.2346` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9689` n `50` status `ready` deltaP `13.2515` edge `0.2041` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `1.8801` n `93` status `ready` deltaP `9.4666` edge `0.1416` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.7071` n `93` status `ready` deltaP `7.1937` edge `0.1462` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.4299` n `70` status `ready` deltaP `9.6329` edge `0.1803` maxDD `-3.3619`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
