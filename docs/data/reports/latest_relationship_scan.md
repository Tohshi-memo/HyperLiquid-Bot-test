# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T16:47:56.072931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->equity_4h` score `0.6442` n `105` status `ready` deltaP `7.7889` edge `0.1647` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5139` n `105` status `ready` deltaP `9.6179` edge `0.0602` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3419` n `105` status `ready` deltaP `10.5575` edge `0.0068` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.0726` n `105` status `ready` deltaP `10.7985` edge `-0.0051` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0131` n `105` status `ready` deltaP `6.8757` edge `0.0061` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1029` n `96` status `ready` deltaP `4.3403` edge `0.1412` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1538` n `105` status `ready` deltaP `3.6869` edge `0.0013` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2341` n `105` status `ready` deltaP `0.3265` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.2388` n `105` status `ready` deltaP `6.3429` edge `0.0195` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4085` n `105` status `ready` deltaP `7.1814` edge `-0.0592` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5329` n `105` status `ready` deltaP `1.1007` edge `0.0045` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.7119` n `105` status `ready` deltaP `-2.1951` edge `0.0084` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.7248` n `105` status `ready` deltaP `1.2375` edge `-0.0167` maxDD `-2.7581`
- `market_context_high->commodity_1h` score `-0.7837` n `105` status `ready` deltaP `-6.477` edge `-0.0007` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.4166` n `105` status `ready` deltaP `4.2814` edge `-0.0196` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.6731` n `105` status `ready` deltaP `6.8351` edge `-0.0829` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.8225` n `96` status `ready` deltaP `17.7083` edge `-0.2193` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5936` n `96` status `ready` deltaP `1.0416` edge `-0.0509` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7958` n `96` status `ready` deltaP `-21.1805` edge `-0.0168` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.951` n `96` status `ready` deltaP `-21.0069` edge `-0.1639` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
