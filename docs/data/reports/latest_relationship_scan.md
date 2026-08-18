# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T06:37:24.785640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11645`

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

- `market_context_high->crypto_major_24h` score `2.4384` n `73` status `ready` deltaP `6.1181` edge `0.2832` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.9039` n `73` status `ready` deltaP `12.6469` edge `0.2149` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.8435` n `98` status `ready` deltaP `7.8609` edge `0.0483` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.5961` n `93` status `ready` deltaP `12.9836` edge `0.0207` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5244` n `98` status `ready` deltaP `11.3589` edge `0.0067` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.4979` n `98` status `ready` deltaP `9.7` edge `-0.0005` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.2892` n `93` status `ready` deltaP `8.081` edge `0.0853` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.1111` n `93` status `ready` deltaP `9.5971` edge `0.0907` maxDD `-5.9014`
- `market_context_high->unknown_24h` score `0.0116` n `73` status `ready` deltaP `13.3876` edge `-0.0682` maxDD `-0.2734`
- `market_context_high->metal_1h` score `-0.1666` n `98` status `ready` deltaP `2.7618` edge `0.0064` maxDD `-0.4291`
- `market_context_high->commodity_4h` score `-0.1926` n `93` status `ready` deltaP `6.3959` edge `0.0177` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.3104` n `93` status `ready` deltaP `1.6211` edge `0.0001` maxDD `-0.3894`
- `market_context_high->crypto_alt_1h` score `-0.3295` n `98` status `ready` deltaP `2.6121` edge `0.0205` maxDD `-2.413`
- `market_context_high->equity_4h` score `-0.3801` n `93` status `ready` deltaP `-0.0935` edge `0.0594` maxDD `-2.5696`
- `market_context_high->index_4h` score `-0.4195` n `93` status `ready` deltaP `2.3292` edge `0.0107` maxDD `-0.2281`
- `market_context_high->fx_1h` score `-0.4235` n `98` status `ready` deltaP `-2.884` edge `0.0011` maxDD `-0.2273`
- `market_context_high->crypto_major_1h` score `-0.5347` n `98` status `ready` deltaP `0.6935` edge `0.0113` maxDD `-2.7581`
- `market_context_high->metal_24h` score `-0.5371` n `73` status `ready` deltaP `1.2488` edge `0.0534` maxDD `-3.78`
- `market_context_high->commodity_1h` score `-0.9024` n `98` status `ready` deltaP `-7.2926` edge `-0.0058` maxDD `-1.5684`
- `market_context_high->index_24h` score `-2.4928` n `73` status `ready` deltaP `-6.2368` edge `-0.1233` maxDD `-5.7106`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
