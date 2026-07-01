# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T13:22:37.378378+00:00`
- Price records: `672`
- Market context records: `5355`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11494`

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

- `market_context_high->unknown_24h` score `13.821` n `164` status `ready` deltaP `18.8262` edge `1.0394` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.3058` n `164` status `ready` deltaP `21.8369` edge `0.7506` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.3195` n `164` status `ready` deltaP `17.4966` edge `0.8062` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.5555` n `194` status `ready` deltaP `13.3361` edge `0.3533` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.1966` n `194` status `ready` deltaP `10.0547` edge `0.2801` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6546` n `194` status `ready` deltaP `9.7875` edge `0.2365` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.78` n `164` status `ready` deltaP `23.9541` edge `0.1038` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.1529` n `164` status `ready` deltaP `9.6715` edge `0.0378` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0374` n `200` status `ready` deltaP `5.9611` edge `0.0599` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.0941` n `200` status `ready` deltaP `3.991` edge `0.0901` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.1161` n `200` status `ready` deltaP `4.6048` edge `0.01` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `-0.1441` n `200` status `ready` deltaP `1.2964` edge `0.0755` maxDD `-5.0257`
- `market_context_high->index_4h` score `-0.4165` n `194` status `ready` deltaP `5.6119` edge `0.0251` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4515` n `200` status `ready` deltaP `-1.1467` edge `-0.0013` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.4942` n `200` status `ready` deltaP `0.3982` edge `0.0015` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6921` n `194` status `ready` deltaP `1.6784` edge `0.003` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.1881` n `194` status `ready` deltaP `8.0604` edge `-0.0345` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5684` n `200` status `ready` deltaP `-4.3473` edge `-0.0084` maxDD `-3.4655`
- `market_context_high->metal_4h` score `-2.695` n `194` status `ready` deltaP `-8.139` edge `-0.0388` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.8144` n `164` status `ready` deltaP `11.5473` edge `0.3037` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
