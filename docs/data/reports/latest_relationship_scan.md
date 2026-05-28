# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T05:22:17.652712+00:00`
- Price records: `672`
- Market context records: `2111`
- Flow alert records: `7973`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9160`

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

- `market_context_high->crypto_alt_4h` score `11.8976` n `170` status `ready` deltaP `33.6155` edge `0.861` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.1102` n `170` status `ready` deltaP `39.1715` edge `0.7177` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.9812` n `170` status `ready` deltaP `24.5319` edge `0.4098` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.4614` n `170` status `ready` deltaP `23.0757` edge `0.3274` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.6553` n `170` status `ready` deltaP `19.2198` edge `0.1615` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5901` n `169` status `ready` deltaP `12.1169` edge `0.2579` maxDD `-4.1604`
- `market_context_high->metal_4h` score `2.5793` n `170` status `ready` deltaP `18.5383` edge `0.2301` maxDD `-4.7664`
- `market_context_high->crypto_major_1h` score `2.3079` n `170` status `ready` deltaP `15.6358` edge `0.1867` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.173` n `170` status `ready` deltaP `12.5026` edge `0.2091` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.9568` n `169` status `ready` deltaP `23.6706` edge `0.5373` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.8409` n `169` status `ready` deltaP `23.4075` edge `0.4872` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8502` n `170` status `ready` deltaP `10.3329` edge `0.0808` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.7355` n `169` status `ready` deltaP `21.0264` edge `0.7797` maxDD `-62.3533`
- `market_context_high->metal_1h` score `0.4734` n `170` status `ready` deltaP `8.1173` edge `0.0524` maxDD `-2.3654`
- `market_context_high->index_1h` score `0.1255` n `170` status `ready` deltaP `5.5196` edge `0.0327` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.0758` n `169` status `ready` deltaP `14.7878` edge `0.031` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.1863` n `170` status `ready` deltaP `4.2357` edge `0.0282` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.2163` n `169` status `ready` deltaP `11.5486` edge `0.2951` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.5816` n `170` status `ready` deltaP `-1.9038` edge `0.0009` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.1176` n `170` status `ready` deltaP `-7.7761` edge `-0.0033` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
