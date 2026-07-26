# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T18:07:26.700023+00:00`
- Price records: `672`
- Market context records: `8010`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11822`

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

- `market_context_high->equity_24h` score `15.9014` n `90` status `ready` deltaP `25.8156` edge `1.2872` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.7708` n `90` status `ready` deltaP `35.8752` edge `0.4084` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1687` n `103` status `ready` deltaP `24.3812` edge `0.4408` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5839` n `103` status `ready` deltaP `23.9039` edge `0.1182` maxDD `-0.979`
- `market_context_high->index_4h` score `2.416` n `103` status `ready` deltaP `25.2781` edge `0.0688` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.3391` n `90` status `ready` deltaP `21.4423` edge `0.1966` maxDD `-6.2367`
- `market_context_high->index_24h` score `2.0639` n `90` status `ready` deltaP `12.513` edge `0.1556` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6736` n `103` status `ready` deltaP `14.2235` edge `0.1264` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2666` n `90` status `ready` deltaP `25.8386` edge `0.0361` maxDD `-2.8915`
- `market_context_high->index_1h` score `0.8678` n `103` status `ready` deltaP `14.1495` edge `0.021` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7166` n `103` status `ready` deltaP `10.2674` edge `0.0291` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6097` n `103` status `ready` deltaP `9.5876` edge `0.1587` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.5568` n `103` status `ready` deltaP `10.8653` edge `0.04` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.5547` n `103` status `ready` deltaP `6.0661` edge `0.1175` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0361` n `103` status `ready` deltaP `1.0086` edge `0.0319` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2292` n `103` status `ready` deltaP `0.936` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3389` n `103` status `ready` deltaP `6.304` edge `0.0045` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5496` n `103` status `ready` deltaP `-0.5616` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1913` n `103` status `ready` deltaP `0.2779` edge `-0.0044` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.933` n `103` status `ready` deltaP `7.0588` edge `-0.1658` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
