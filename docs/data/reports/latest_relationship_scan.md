# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T17:16:28.909811+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11818`

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

- `market_context_high->equity_4h` score `0.6866` n `105` status `ready` deltaP `8.0938` edge `0.1662` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5343` n `105` status `ready` deltaP `9.7676` edge `0.0609` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.355` n `105` status `ready` deltaP `10.7072` edge `0.0069` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.0466` n `105` status `ready` deltaP `10.4936` edge `-0.0064` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0131` n `105` status `ready` deltaP `6.8757` edge `0.0061` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.09` n `96` status `ready` deltaP `4.5139` edge `0.1417` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1526` n `105` status `ready` deltaP `3.6869` edge `0.0014` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2263` n `105` status `ready` deltaP `0.4762` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2388` n `105` status `ready` deltaP `6.3429` edge `0.0195` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4673` n `105` status `ready` deltaP `7.0317` edge `-0.0631` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5555` n `105` status `ready` deltaP `0.951` edge `0.0026` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7134` n `105` status `ready` deltaP `-2.1951` edge `0.0082` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7537` n `105` status `ready` deltaP `1.2375` edge `-0.0204` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.7837` n `105` status `ready` deltaP `-6.477` edge `-0.0007` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4718` n `105` status `ready` deltaP `4.2814` edge `-0.0242` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.7691` n `105` status `ready` deltaP `6.8351` edge `-0.0909` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.9761` n `96` status `ready` deltaP `17.7083` edge `-0.2321` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.596` n `96` status `ready` deltaP `1.0416` edge `-0.0512` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7994` n `96` status `ready` deltaP `-21.1805` edge `-0.0171` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9549` n `96` status `ready` deltaP `-21.0069` edge `-0.1644` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
