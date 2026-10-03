# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T05:07:27.000632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `366.2013` n `50` status `ready` deltaP `11.1737` edge `30.4472` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.4788` n `50` status `ready` deltaP `10.9756` edge `24.3834` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.4623` n `50` status `ready` deltaP `23.4792` edge `0.969` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.6094` n `70` status `ready` deltaP `33.7351` edge `0.7077` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0898` n `50` status `ready` deltaP `31.3056` edge `0.6904` maxDD `-9.3299`
- `news_risk_high->crypto_alt_24h` score `8.5456` n `70` status `ready` deltaP `16.6221` edge `0.8213` maxDD `-12.9319`
- `news_risk_high->crypto_major_4h` score `8.211` n `89` status `ready` deltaP `31.7741` edge `0.4993` maxDD `-0.8168`
- `news_risk_high->crypto_alt_4h` score `7.7227` n `89` status `ready` deltaP `31.7348` edge `0.5664` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2733` n `50` status `ready` deltaP `16.628` edge `0.5656` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.8875` n `50` status `ready` deltaP `16.3415` edge `0.5106` maxDD `-7.6465`
- `news_risk_high->index_24h` score `3.8196` n `70` status `ready` deltaP `33.0407` edge `0.1139` maxDD `-0.2696`
- `news_risk_high->crypto_major_24h` score `3.647` n `70` status `ready` deltaP `12.1627` edge `0.4853` maxDD `-16.3306`
- `news_risk_high->equity_4h` score `3.481` n `89` status `ready` deltaP `27.5624` edge `0.1676` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1714` n `50` status `ready` deltaP `14.2036` edge `0.2359` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9713` n `50` status `ready` deltaP `13.2515` edge `0.2043` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.4038` n `89` status `ready` deltaP `12.1728` edge `0.1547` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `1.9438` n `89` status `ready` deltaP `8.8778` edge `0.1547` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.41` n `50` status `ready` deltaP `19.8922` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_4h` score `1.37` n `89` status `ready` deltaP `12.7518` edge `0.0874` maxDD `-0.993`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
