# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T16:37:14.986171+00:00`
- Price records: `672`
- Market context records: `1647`
- Flow alert records: `6652`
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

- `market_context_high->metal_24h` score `9.3079` n `170` status `ready` deltaP `27.474` edge `0.8351` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `3.8516` n `185` status `ready` deltaP `21.2226` edge `0.4459` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.5985` n `170` status `ready` deltaP `19.481` edge `0.3078` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.1723` n `185` status `ready` deltaP `16.9822` edge `0.3387` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.6643` n `185` status `ready` deltaP `11.5866` edge `0.1709` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.418` n `170` status `ready` deltaP `18.5121` edge `0.4846` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.1835` n `195` status `ready` deltaP `5.0983` edge `0.0919` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.1735` n `170` status `ready` deltaP `24.2907` edge `0.7111` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `-0.0867` n `170` status `ready` deltaP `24.9135` edge `1.0076` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.2858` n `195` status `ready` deltaP `1.4258` edge `0.0347` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4602` n `185` status `ready` deltaP `-0.0009` edge `0.0499` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4656` n `195` status `ready` deltaP `0.9958` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.5043` n `170` status `ready` deltaP `6.2976` edge `0.0209` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5243` n `195` status `ready` deltaP `-1.5223` edge `0.0061` maxDD `-1.7205`
- `market_context_high->crypto_major_1h` score `-0.5511` n `195` status `ready` deltaP `1.251` edge `0.0484` maxDD `-5.5244`
- `market_context_high->commodity_1h` score `-0.8677` n `195` status `ready` deltaP `1.3361` edge `-0.007` maxDD `-6.7191`
- `market_context_high->metal_1h` score `-0.8822` n `195` status `ready` deltaP `2.4262` edge `0.0043` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3648` n `185` status `ready` deltaP `-10.318` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4717` n `185` status `ready` deltaP `7.3266` edge `0.0977` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.0145` n `185` status `ready` deltaP `10.4118` edge `-0.0935` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
