# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T00:22:25.960705+00:00`
- Price records: `672`
- Market context records: `8567`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `5076.3981` n `61` status `ready` deltaP `39.6232` edge `422.8111` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8602` n `64` status `ready` deltaP `21.1128` edge `0.4073` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1214` n `64` status `ready` deltaP `17.721` edge `0.0777` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.037` n `62` status `ready` deltaP `14.1227` edge `0.1713` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7613` n `64` status `ready` deltaP `16.5513` edge `0.0841` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1422` n `64` status `ready` deltaP `7.9649` edge `0.1709` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7331` n `64` status `ready` deltaP `13.7195` edge `0.1417` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4835` n `64` status `ready` deltaP `8.561` edge `0.0576` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.4054` n `64` status `ready` deltaP `7.6628` edge `0.0521` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0994` n `64` status `ready` deltaP `5.436` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.074` n `64` status `ready` deltaP `11.9284` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0255` n `64` status `ready` deltaP `3.9203` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0349` n `64` status `ready` deltaP `1.7149` edge `0.0317` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0942` n `62` status `ready` deltaP `8.753` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.0964` n `64` status `ready` deltaP `3.7051` edge `0.0076` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2653` n `62` status `ready` deltaP `2.3614` edge `0.0005` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3403` n `62` status `ready` deltaP `3.7087` edge `-0.0058` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4933` n `62` status `ready` deltaP `-2.4773` edge `0.016` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7441` n `62` status `ready` deltaP `0.9465` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9374` n `62` status `ready` deltaP `-2.5449` edge `-0.0117` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
