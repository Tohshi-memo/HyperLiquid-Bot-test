# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T21:52:27.980310+00:00`
- Price records: `672`
- Market context records: `8555`
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

- `news_risk_high->unknown_24h` score `5192.5154` n `60` status `ready` deltaP `41.25` edge `432.4767` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6117` n `64` status `ready` deltaP `20.0457` edge `0.3937` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9707` n `64` status `ready` deltaP `16.1966` edge `0.0753` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.956` n `62` status `ready` deltaP `13.6654` edge `0.1676` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7337` n `64` status `ready` deltaP `16.2519` edge `0.0838` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0296` n `64` status `ready` deltaP `6.7454` edge `0.1646` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6804` n `64` status `ready` deltaP `13.2622` edge `0.138` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4726` n `64` status `ready` deltaP `8.4113` edge `0.0572` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3438` n `64` status `ready` deltaP `6.7646` edge `0.0502` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0893` n `64` status `ready` deltaP `5.2863` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0239` n `64` status `ready` deltaP `3.9203` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0148` n `64` status `ready` deltaP `11.0137` edge `0.0211` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0411` n `64` status `ready` deltaP `1.7149` edge `0.0309` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.0976` n `64` status `ready` deltaP `3.7051` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.183` n `62` status `ready` deltaP `7.8383` edge `0.0121` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2755` n `62` status `ready` deltaP `2.2117` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3107` n `62` status `ready` deltaP `4.1578` edge `-0.005` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5042` n `62` status `ready` deltaP `-2.627` edge `0.0156` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7465` n `62` status `ready` deltaP `0.9465` edge `-0.0156` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9386` n `62` status `ready` deltaP `-2.5449` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
