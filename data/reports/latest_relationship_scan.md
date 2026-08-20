# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-20T16:37:31.645567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10819`

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

- `market_context_high->equity_4h` score `0.6296` n `105` status `ready` deltaP `7.6365` edge `0.1645` maxDD `-8.3685`
- `market_context_high->equity_1h` score `0.5079` n `105` status `ready` deltaP `9.6179` edge `0.0597` maxDD `-3.1861`
- `market_context_high->index_1h` score `0.3419` n `105` status `ready` deltaP `10.5575` edge `0.0068` maxDD `-0.5622`
- `market_context_high->metal_4h` score `0.0852` n `105` status `ready` deltaP `10.9509` edge `-0.0045` maxDD `-1.273`
- `market_context_high->fx_4h` score `0.0131` n `105` status `ready` deltaP `6.8757` edge `0.0061` maxDD `-0.3539`
- `market_context_high->commodity_24h` score `-0.1037` n `96` status `ready` deltaP `4.3403` edge `0.1411` maxDD `-4.666`
- `market_context_high->metal_1h` score `-0.167` n `105` status `ready` deltaP `3.5372` edge `0.0012` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.2263` n `105` status `ready` deltaP `0.4762` edge `0.0037` maxDD `-0.2043`
- `market_context_high->index_4h` score `-0.238` n `105` status `ready` deltaP `6.3429` edge `0.0196` maxDD `-1.7252`
- `market_context_high->unknown_1h` score `-0.4253` n `105` status `ready` deltaP `7.0317` edge `-0.0596` maxDD `-0.4843`
- `market_context_high->crypto_alt_1h` score `-0.5158` n `105` status `ready` deltaP `1.2504` edge `0.0057` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.7014` n `105` status `ready` deltaP `1.3872` edge `-0.0147` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.7103` n `105` status `ready` deltaP `-2.1951` edge `0.0086` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7837` n `105` status `ready` deltaP `-6.477` edge `-0.0007` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.3696` n `105` status `ready` deltaP `4.4338` edge `-0.0167` maxDD `-5.4926`
- `market_context_high->crypto_major_4h` score `-1.6167` n `105` status `ready` deltaP `6.8351` edge `-0.0782` maxDD `-3.1677`
- `market_context_high->unknown_24h` score `-1.7853` n `96` status `ready` deltaP `17.7083` edge `-0.2162` maxDD `-1.0505`
- `market_context_high->index_24h` score `-3.5838` n `96` status `ready` deltaP `1.2152` edge `-0.0508` maxDD `-18.3411`
- `market_context_high->fx_24h` score `-3.7934` n `96` status `ready` deltaP `-21.1805` edge `-0.0166` maxDD `-1.9981`
- `market_context_high->metal_24h` score `-4.951` n `96` status `ready` deltaP `-21.0069` edge `-0.1639` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
