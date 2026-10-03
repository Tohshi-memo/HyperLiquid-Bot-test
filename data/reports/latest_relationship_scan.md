# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T07:22:33.293153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4826`

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

- `market_context_high->unknown_1h` score `366.1978` n `50` status `ready` deltaP `11.024` edge `30.4479` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.7838` n `50` status `ready` deltaP `12.0427` edge `24.4017` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.0421` n `50` status `ready` deltaP `25.0417` edge `1.0069` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.8818` n `70` status `ready` deltaP `33.7351` edge `0.7304` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.5609` n `50` status `ready` deltaP `32.6944` edge `0.7204` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.3502` n `80` status `ready` deltaP `36.5854` edge `0.5556` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5808` n `80` status `ready` deltaP `30.3963` edge `0.5635` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3255` n `50` status `ready` deltaP `17.0854` edge `0.5669` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.0019` n `50` status `ready` deltaP `16.6463` edge `0.5181` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.1352` n `70` status `ready` deltaP `33.0407` edge `0.1402` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9058` n `80` status `ready` deltaP `30.4573` edge `0.1837` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.265` n `50` status `ready` deltaP `14.8024` edge `0.2397` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9689` n `50` status `ready` deltaP `13.2515` edge `0.2041` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8799` n `50` status `ready` deltaP `32.2317` edge `0.0386` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.7333` n `80` status `ready` deltaP `14.2515` edge `0.1683` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1046` n `80` status `ready` deltaP `18.3841` edge `0.0944` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.7082` n `80` status `ready` deltaP `7.5524` edge `0.1439` maxDD `-2.4854`
- `news_risk_high->index_4h` score `1.6364` n `80` status `ready` deltaP `21.25` edge `0.0459` maxDD `-0.4296`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `market_context_high->fx_24h` score `1.3302` n `50` status `ready` deltaP `25.7153` edge `0.1009` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
