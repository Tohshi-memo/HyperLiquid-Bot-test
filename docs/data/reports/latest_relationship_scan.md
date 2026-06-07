# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T12:07:27.754052+00:00`
- Price records: `672`
- Market context records: `3176`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8856`

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

- `market_context_high->commodity_24h` score `13.9363` n `101` status `ready` deltaP `47.2171` edge `0.8894` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.1932` n `101` status `ready` deltaP `20.2643` edge `0.9298` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.4134` n `101` status `ready` deltaP `14.0643` edge `2.3671` maxDD `-71.142`
- `market_context_high->index_24h` score `6.175` n `101` status `ready` deltaP `29.2216` edge `0.8523` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.3701` n `101` status `ready` deltaP `12.629` edge `1.3177` maxDD `-53.663`
- `market_context_high->commodity_4h` score `3.1258` n `134` status `ready` deltaP `19.8125` edge `0.1742` maxDD `-1.9973`
- `market_context_high->fx_24h` score `0.7373` n `101` status `ready` deltaP `12.1803` edge `0.003` maxDD `-0.4876`
- `market_context_high->unknown_4h` score `0.4194` n `134` status `ready` deltaP `11.0506` edge `0.1835` maxDD `-14.7778`
- `market_context_high->commodity_1h` score `0.3266` n `139` status `ready` deltaP `5.666` edge `0.0317` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3605` n `139` status `ready` deltaP `5.9945` edge `0.0201` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.376` n `139` status `ready` deltaP `6.323` edge `0.1226` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.8994` n `134` status `ready` deltaP `15.9287` edge `0.0694` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.0051` n `139` status `ready` deltaP `3.47` edge `0.0743` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.2385` n `139` status `ready` deltaP `4.4059` edge `0.016` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3378` n `134` status `ready` deltaP `-11.4352` edge `-0.0068` maxDD `-1.4115`
- `market_context_high->fx_1h` score `-1.587` n `139` status `ready` deltaP `-8.7559` edge `-0.0052` maxDD `-0.8278`
- `market_context_high->metal_1h` score `-2.0443` n `139` status `ready` deltaP `-3.4787` edge `-0.0078` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.2266` n `134` status `ready` deltaP `17.5078` edge `0.4023` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.0038` n `139` status `ready` deltaP `3.2127` edge `-0.0691` maxDD `-14.2111`
- `market_context_high->crypto_major_4h` score `-3.6702` n `134` status `ready` deltaP `10.4455` edge `0.2522` maxDD `-54.3896`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
