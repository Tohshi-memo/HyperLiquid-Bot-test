# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T09:29:04.723356+00:00`
- Price records: `672`
- Market context records: `1617`
- Flow alert records: `6562`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `11.4928` n `188` status `ready` deltaP `26.9909` edge `0.9589` maxDD `-9.1552`
- `market_context_high->index_24h` score `3.4344` n `188` status `ready` deltaP `19.1452` edge `0.2797` maxDD `-5.3574`
- `market_context_high->crypto_major_24h` score `1.766` n `188` status `ready` deltaP `23.1604` edge `0.6385` maxDD `-46.6586`
- `market_context_high->equity_24h` score `1.7448` n `188` status `ready` deltaP `17.712` edge `0.4184` maxDD `-26.6196`
- `market_context_high->equity_4h` score `1.3526` n `192` status `ready` deltaP `11.2296` edge `0.1473` maxDD `-5.0894`
- `market_context_high->crypto_alt_24h` score `1.0596` n `188` status `ready` deltaP `23.2602` edge `0.8224` maxDD `-66.7999`
- `market_context_high->crypto_alt_4h` score `0.3852` n `192` status `ready` deltaP `13.3257` edge `0.2925` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.2271` n `192` status `ready` deltaP `9.375` edge `0.2375` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2537` n `188` status `ready` deltaP `7.7201` edge `0.0323` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3239` n `192` status `ready` deltaP `0.2152` edge `0.0594` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.4923` n `192` status `ready` deltaP `1.2195` edge `0.0317` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6741` n `192` status `ready` deltaP `0.4647` edge `0.0039` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8221` n `192` status `ready` deltaP `-0.3119` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.8721` n `192` status `ready` deltaP `0.2287` edge `0.0347` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.9097` n `192` status `ready` deltaP `-1.4908` edge `0.029` maxDD `-6.1883`
- `market_context_high->commodity_1h` score `-1.0917` n `192` status `ready` deltaP `-0.0062` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1728` n `192` status `ready` deltaP `4.5971` edge `0.0052` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3956` n `192` status `ready` deltaP `-10.7597` edge `-0.0143` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4161` n `192` status `ready` deltaP `8.7271` edge `0.093` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.1936` n `192` status `ready` deltaP `-13.9863` edge `-0.1099` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
