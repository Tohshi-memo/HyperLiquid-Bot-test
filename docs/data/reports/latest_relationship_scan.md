# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T01:57:00.961748+00:00`
- Price records: `672`
- Market context records: `2412`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9202`

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

- `news_risk_high->crypto_alt_24h` score `20.2832` n `43` status `ready` deltaP `46.5641` edge `1.4387` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2789` n `43` status `ready` deltaP `49.4105` edge `1.2378` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.2023` n `43` status `ready` deltaP `29.7925` edge `1.0997` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9084` n `43` status `ready` deltaP `18.8993` edge `0.8411` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.2103` n `43` status `ready` deltaP `27.9877` edge `0.5202` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5548` n `107` status `ready` deltaP `22.3585` edge `0.355` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3267` n `43` status `ready` deltaP `12.0559` edge `0.4054` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.784` n `130` status `ready` deltaP `22.9597` edge `0.4266` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.342` n `130` status `ready` deltaP `21.3649` edge `0.4873` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6139` n `43` status `ready` deltaP `37.924` edge `0.0668` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.2764` n `43` status `ready` deltaP `30.1758` edge `0.286` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.9265` n `107` status `ready` deltaP `12.6833` edge `0.6799` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.423` n `130` status `ready` deltaP `12.432` edge `0.18` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.1646` n `43` status `ready` deltaP `27.4319` edge `0.0159` maxDD `-0.1382`
- `market_context_high->index_24h` score `1.9507` n `107` status `ready` deltaP `11.4908` edge `0.1235` maxDD `-1.0036`
- `news_risk_high->unknown_4h` score `1.7939` n `43` status `ready` deltaP `15.9919` edge `0.1152` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.3643` n `130` status `ready` deltaP `12.3906` edge `0.1505` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1085` n `43` status `ready` deltaP `20.2966` edge `0.004` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0785` n `130` status `ready` deltaP `9.4219` edge `0.1458` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5415` n `130` status `ready` deltaP `12.2256` edge `0.0462` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
