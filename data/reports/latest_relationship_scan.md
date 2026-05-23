# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T17:07:19.297524+00:00`
- Price records: `672`
- Market context records: `1649`
- Flow alert records: `6658`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.3134` n `169` status `ready` deltaP `27.7227` edge `0.8339` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `3.9653` n `185` status `ready` deltaP `21.4587` edge `0.4538` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.6571` n `169` status `ready` deltaP `19.7191` edge `0.3111` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.2718` n `185` status `ready` deltaP `17.3705` edge `0.3444` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.6835` n `185` status `ready` deltaP `11.5866` edge `0.1725` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5116` n `169` status `ready` deltaP `18.7363` edge `0.4909` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.3445` n `195` status `ready` deltaP `5.3816` edge `0.0952` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.2927` n `169` status `ready` deltaP `24.5357` edge `0.7194` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.1047` n `169` status `ready` deltaP `25.1899` edge `1.0217` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.2919` n `195` status `ready` deltaP `1.3397` edge `0.0345` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4579` n `185` status `ready` deltaP `-0.0009` edge `0.0502` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4808` n `195` status `ready` deltaP `0.7025` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.5122` n `169` status `ready` deltaP `6.214` edge `0.0208` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5211` n `195` status `ready` deltaP `-1.4601` edge `0.0061` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.5245` n `195` status `ready` deltaP `1.5369` edge `0.0499` maxDD `-5.5244`
- `market_context_high->commodity_1h` score `-0.8631` n `195` status `ready` deltaP `1.4095` edge `-0.0069` maxDD `-6.7191`
- `market_context_high->metal_1h` score `-0.8674` n `195` status `ready` deltaP `2.7123` edge `0.0043` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.4693` n `185` status `ready` deltaP `7.3266` edge `0.0979` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-2.0876` n `185` status `ready` deltaP `-10.1658` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-2.9212` n `185` status `ready` deltaP `10.6479` edge `-0.0873` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
