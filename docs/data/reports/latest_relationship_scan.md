# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T05:22:28.250173+00:00`
- Price records: `672`
- Market context records: `8589`
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

- `news_risk_high->unknown_24h` score `4749.9285` n `64` status `ready` deltaP `36.4583` edge `395.6264` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8852` n `64` status `ready` deltaP `20.9604` edge `0.4104` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1506` n `64` status `ready` deltaP `18.0259` edge `0.0781` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8092` n `64` status `ready` deltaP `17.0004` edge `0.0851` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.574` n `62` status `ready` deltaP `11.5312` edge `0.15` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `0.9713` n `64` status `ready` deltaP `5.9832` edge `0.1622` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.4322` n `64` status `ready` deltaP `11.128` edge `0.1204` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4227` n `64` status `ready` deltaP `7.9622` edge `0.0538` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3618` n `64` status `ready` deltaP `7.064` edge `0.0505` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.0862` n `64` status `ready` deltaP `12.0808` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0815` n `64` status `ready` deltaP `5.1366` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.041` n `64` status `ready` deltaP `4.2197` edge `0.0088` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0158` n `64` status `ready` deltaP `2.6296` edge `0.0321` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.082` n `62` status `ready` deltaP `8.9054` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1215` n `64` status `ready` deltaP `3.4057` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2832` n `62` status `ready` deltaP `2.062` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3223` n `62` status `ready` deltaP `4.0081` edge `-0.0055` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.554` n `62` status `ready` deltaP `-3.0761` edge `0.0122` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7201` n `62` status `ready` deltaP `1.2459` edge `-0.0154` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9625` n `62` status `ready` deltaP `-2.8443` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
