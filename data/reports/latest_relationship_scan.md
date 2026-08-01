# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T02:22:30.802010+00:00`
- Price records: `672`
- Market context records: `8576`
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

- `news_risk_high->unknown_24h` score `4751.3708` n `64` status `ready` deltaP `38.5417` edge `395.7327` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9778` n `64` status `ready` deltaP `22.0274` edge `0.411` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1774` n `64` status `ready` deltaP `18.3308` edge `0.0783` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.892` n `62` status `ready` deltaP `13.3605` edge `0.1643` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7637` n `64` status `ready` deltaP `16.5513` edge `0.0843` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1162` n `64` status `ready` deltaP `7.6601` edge `0.1696` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6388` n `64` status `ready` deltaP `12.9573` edge `0.1347` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4189` n `64` status `ready` deltaP `7.8125` edge `0.0543` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3547` n `64` status `ready` deltaP `6.9143` edge `0.0506` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0901` n `64` status `ready` deltaP `5.2863` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0594` n `64` status `ready` deltaP `11.7759` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0075` n `64` status `ready` deltaP `3.6209` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0349` n `64` status `ready` deltaP `1.7149` edge `0.0317` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.1088` n `62` status `ready` deltaP `8.6005` edge `0.0132` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1335` n `64` status `ready` deltaP `3.256` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2747` n `62` status `ready` deltaP `2.2117` edge `0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3114` n `62` status `ready` deltaP `4.1578` edge `-0.0051` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5579` n `62` status `ready` deltaP `-3.2258` edge `0.0127` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7716` n `62` status `ready` deltaP `0.6471` edge `-0.0157` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9745` n `62` status `ready` deltaP `-2.994` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
