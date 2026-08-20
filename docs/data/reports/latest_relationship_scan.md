# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T18:52:43.443566+00:00`
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

- `market_context_high->equity_4h` score `0.7554` n `105` status `ready` deltaP `8.3987` edge `0.1699` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5858` n `105` status `ready` deltaP `10.2167` edge `0.0622` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.397` n `105` status `ready` deltaP `11.1563` edge `0.0074` maxDD `-0.5622`
- `market_context_high->fx_4h` score `0.0116` n `105` status `ready` deltaP `6.8757` edge `0.0059` maxDD `-0.3539`
- `market_context_high->metal_4h` score `-0.0235` n `105` status `ready` deltaP `9.579` edge `-0.0093` maxDD `-1.273`
- `market_context_high->commodity_24h` score `-0.0833` n `96` status `ready` deltaP `4.6875` edge `0.1414` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.1706` n `105` status `ready` deltaP `3.5372` edge `0.0009` maxDD `-0.4291`
- `market_context_high->index_4h` score `-0.2254` n `105` status `ready` deltaP `6.4954` edge `0.0202` maxDD `-1.7252`
- `market_context_high->fx_1h` score `-0.2263` n `105` status `ready` deltaP `0.4762` edge `0.0037` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.5095` n `105` status `ready` deltaP `1.2504` edge `0.0065` maxDD `-2.413`
- `market_context_high->unknown_1h` score `-0.5189` n `105` status `ready` deltaP `6.882` edge `-0.0664` maxDD `-0.4843`
- `market_context_high->crypto_major_1h` score `-0.6757` n `105` status `ready` deltaP `1.6866` edge `-0.0134` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7458` n `105` status `ready` deltaP `-2.6524` edge `0.0071` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8421` n `105` status `ready` deltaP `-7.3752` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5786` n `105` status `ready` deltaP `4.2814` edge `-0.0331` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.9827` n `105` status `ready` deltaP `6.8351` edge `-0.1087` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-2.4256` n `96` status `ready` deltaP `17.5347` edge `-0.2684` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.603` n `96` status `ready` deltaP `1.0416` edge `-0.0521` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.8162` n `96` status `ready` deltaP `-21.1805` edge `-0.0185` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.9697` n `96` status `ready` deltaP `-21.0069` edge `-0.1663` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
