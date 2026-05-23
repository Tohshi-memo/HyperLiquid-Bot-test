# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T16:29:26.873296+00:00`
- Price records: `672`
- Market context records: `1646`
- Flow alert records: `6650`
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

- `market_context_high->metal_24h` score `9.3822` n `171` status `ready` deltaP `27.3973` edge `0.8418` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `3.7424` n `185` status `ready` deltaP `21.2226` edge `0.4368` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.5668` n `171` status `ready` deltaP `19.4146` edge `0.3056` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.1003` n `185` status `ready` deltaP `16.9822` edge `0.3327` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.6367` n `185` status `ready` deltaP `11.5866` edge `0.1686` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3646` n `171` status `ready` deltaP `18.4595` edge `0.4805` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.1544` n `171` status `ready` deltaP `24.2174` edge `0.71` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1505` n `195` status `ready` deltaP `4.7349` edge `0.0901` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `-0.167` n `171` status `ready` deltaP `24.8093` edge `1.0016` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.3086` n `195` status `ready` deltaP `1.0624` edge `0.0342` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4656` n `195` status `ready` deltaP `0.9958` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4665` n `185` status `ready` deltaP `-0.0009` edge `0.0491` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.4917` n `171` status `ready` deltaP `6.3801` edge `0.0214` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5023` n `195` status `ready` deltaP `-1.159` edge `0.0065` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.5793` n `195` status `ready` deltaP `0.8877` edge `0.0472` maxDD `-5.5244`
- `market_context_high->commodity_1h` score `-0.8367` n `195` status `ready` deltaP `1.6994` edge `-0.0063` maxDD `-6.6507`
- `market_context_high->metal_1h` score `-0.8633` n `195` status `ready` deltaP `2.7895` edge `0.0043` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3866` n `185` status `ready` deltaP `-10.7063` edge `-0.0135` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4729` n `185` status `ready` deltaP `7.3266` edge `0.0976` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.126` n `185` status `ready` deltaP `10.0234` edge `-0.1002` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
