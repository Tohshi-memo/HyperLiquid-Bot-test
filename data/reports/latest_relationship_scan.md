# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T22:37:25.558211+00:00`
- Price records: `672`
- Market context records: `4979`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `11.5119` n `93` status `ready` deltaP `5.0431` edge `0.9758` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.7102` n `88` status `ready` deltaP `18.0571` edge `0.5571` maxDD `-6.7974`
- `market_context_high->crypto_alt_4h` score `5.8945` n `88` status `ready` deltaP `16.6852` edge `0.5152` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.793` n `80` status `ready` deltaP `28.0208` edge `0.3302` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `3.4498` n `88` status `ready` deltaP `25.5128` edge `0.1781` maxDD `-2.5231`
- `market_context_high->metal_4h` score `1.3754` n `88` status `ready` deltaP `12.5416` edge `0.1264` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8461` n `88` status `ready` deltaP `8.8691` edge `0.1875` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5681` n `88` status `ready` deltaP `7.3725` edge `0.0441` maxDD `-0.6727`
- `market_context_high->equity_1h` score `0.4283` n `93` status `ready` deltaP `5.5872` edge `0.075` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.2739` n `93` status `ready` deltaP `3.4769` edge `0.1147` maxDD `-5.5543`
- `market_context_high->crypto_alt_1h` score `0.1492` n `93` status `ready` deltaP `4.961` edge `0.0883` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0295` n `93` status `ready` deltaP `2.4016` edge `0.0361` maxDD `-1.3057`
- `market_context_high->fx_24h` score `-0.427` n `80` status `ready` deltaP `3.3681` edge `-0.001` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4573` n `93` status `ready` deltaP `0.1561` edge `0.0063` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4766` n `93` status `ready` deltaP `0.2382` edge `0.0126` maxDD `-0.6904`
- `market_context_high->fx_4h` score `-1.0145` n `88` status `ready` deltaP `-4.6979` edge `-0.0017` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.255` n `88` status `ready` deltaP `4.2267` edge `-0.0075` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.636` n `93` status `ready` deltaP `-10.7736` edge `-0.0046` maxDD `-0.4596`
- `market_context_high->commodity_24h` score `-3.4244` n `80` status `ready` deltaP `12.7431` edge `-0.0131` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.4555` n `80` status `ready` deltaP `-5.6597` edge `0.012` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
