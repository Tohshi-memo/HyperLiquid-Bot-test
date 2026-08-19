# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T03:10:02.398576+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.1715` n `92` status `ready` deltaP `6.8916` edge `0.2558` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.5695` n `96` status `ready` deltaP `13.0552` edge `0.0739` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.538` n `96` status `ready` deltaP `8.8668` edge `0.1579` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3338` n `92` status `ready` deltaP `15.8288` edge `0.2488` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1732` n `96` status `ready` deltaP `17.6321` edge `0.0378` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9645` n `96` status `ready` deltaP `11.3059` edge `0.1071` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.86` n `96` status `ready` deltaP `15.0137` edge `0.0103` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.4513` n `96` status `ready` deltaP `11.2805` edge `0.0894` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.3007` n `96` status `ready` deltaP `9.0569` edge `-0.0126` maxDD `-0.4843`
- `market_context_high->unknown_24h` score `0.1744` n `92` status `ready` deltaP `15.8138` edge `-0.064` maxDD `-0.485`
- `market_context_high->metal_1h` score `0.15` n `96` status `ready` deltaP `5.9693` edge `0.0114` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.039` n `96` status `ready` deltaP `6.4278` edge `0.0024` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0489` n `96` status `ready` deltaP `6.1229` edge `0.0206` maxDD `-0.5728`
- `market_context_high->crypto_alt_1h` score `-0.3053` n `96` status `ready` deltaP `3.5741` edge `0.0172` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.3377` n `96` status `ready` deltaP `-1.4721` edge `0.0024` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3853` n `96` status `ready` deltaP `2.6821` edge `0.0172` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.4778` n `96` status `ready` deltaP `2.2612` edge `0.0087` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8798` n `96` status `ready` deltaP `-7.5911` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.6924` n `92` status `ready` deltaP `-1.4719` edge `0.0812` maxDD `-9.4025`
- `market_context_high->fx_24h` score `-4.089` n `92` status `ready` deltaP `-24.5245` edge `-0.0259` maxDD `-1.4417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
