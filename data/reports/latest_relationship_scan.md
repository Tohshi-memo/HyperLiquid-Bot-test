# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T10:22:26.712849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.145` n `50` status `ready` deltaP `11.024` edge `30.4435` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2792` n `50` status `ready` deltaP `12.0244` edge `24.4431` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.075` n `50` status `ready` deltaP `27.0329` edge `1.0797` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `10.4654` n `50` status `ready` deltaP `34.6863` edge `0.7825` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.431` n `69` status `ready` deltaP `38.7863` edge `0.631` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.0902` n `69` status `ready` deltaP `28.8499` edge `0.697` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.8198` n `69` status `ready` deltaP `29.409` edge `0.59` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4639` n `50` status `ready` deltaP `18.3805` edge `0.5698` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3126` n `50` status `ready` deltaP `18.2496` edge `0.5333` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.3195` n `69` status `ready` deltaP `32.9139` edge `0.1564` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9908` n `69` status `ready` deltaP `28.6547` edge `0.2028` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3633` n `50` status `ready` deltaP `15.4012` edge `0.2439` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.059` n `69` status `ready` deltaP `14.918` edge `0.191` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0334` n `69` status `ready` deltaP `33.5385` edge `0.0554` maxDD `-0.4296`
- `market_context_high->crypto_major_1h` score `3.0133` n `50` status `ready` deltaP `13.7006` edge `0.2048` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0005` n `50` status `ready` deltaP `33.6651` edge `0.0391` maxDD `-0.0791`
- `news_risk_high->metal_4h` score `2.2601` n `69` status `ready` deltaP `18.8737` edge `0.1041` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.537` n `69` status `ready` deltaP `5.9229` edge `0.1405` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4735` n `50` status `ready` deltaP `20.6407` edge `0.0116` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.4085` n `69` status `ready` deltaP `13.0739` edge `0.0664` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
