# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T05:37:33.064774+00:00`
- Price records: `672`
- Market context records: `8590`
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

- `news_risk_high->unknown_24h` score `4749.8114` n `64` status `ready` deltaP `36.2847` edge `395.6178` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.884` n `64` status `ready` deltaP `20.9604` edge `0.4103` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1506` n `64` status `ready` deltaP `18.0259` edge `0.0781` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8104` n `64` status `ready` deltaP `17.0004` edge `0.0852` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5487` n `62` status `ready` deltaP `11.3788` edge `0.1489` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `0.9658` n `64` status `ready` deltaP `5.9832` edge `0.1615` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.4157` n `64` status `ready` deltaP `10.9756` edge `0.1193` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4118` n `64` status `ready` deltaP `7.8125` edge `0.0534` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3586` n `64` status `ready` deltaP `7.064` edge `0.0501` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.0862` n `64` status `ready` deltaP `12.0808` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0729` n `64` status `ready` deltaP `4.9869` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0418` n `64` status `ready` deltaP `4.2197` edge `0.0089` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0158` n `64` status `ready` deltaP `2.6296` edge `0.0321` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.082` n `62` status `ready` deltaP `8.9054` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1335` n `64` status `ready` deltaP `3.256` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2918` n `62` status `ready` deltaP `1.9123` edge `0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3216` n `62` status `ready` deltaP `4.0081` edge `-0.0054` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5649` n `62` status `ready` deltaP `-3.2258` edge `0.0118` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7189` n `62` status `ready` deltaP `1.2459` edge `-0.0153` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9745` n `62` status `ready` deltaP `-2.994` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
