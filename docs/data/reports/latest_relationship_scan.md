# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T14:37:26.732021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10825`

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

- `market_context_high->equity_24h` score `3.7882` n `103` status `ready` deltaP `4.2257` edge `0.5935` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3803` n `103` status `ready` deltaP `9.6076` edge `0.1919` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2372` n `143` status `ready` deltaP `15.5094` edge `0.067` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7893` n `143` status `ready` deltaP `10.8413` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7107` n `103` status `ready` deltaP `21.4013` edge `0.0351` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4198` n `103` status `ready` deltaP `6.6697` edge `0.1625` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3457` n `143` status `ready` deltaP `3.6965` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3832` n `143` status `ready` deltaP `-0.7945` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5053` n `143` status `ready` deltaP `5.523` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6737` n `143` status `ready` deltaP `-4.5883` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8294` n `143` status `ready` deltaP `-0.001` edge `-0.0086` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9229` n `143` status `ready` deltaP `-0.3371` edge `0.0082` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0074` n `143` status `ready` deltaP `-1.6608` edge `-0.0172` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9084` n `143` status `ready` deltaP `-10.1336` edge `-0.0273` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4467` n `143` status `ready` deltaP `-0.5042` edge `-0.0668` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2059` n `143` status `ready` deltaP `-11.1365` edge `-0.0607` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.7315` n `143` status `ready` deltaP `-7.6668` edge `-0.0942` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.0679` n `103` status `ready` deltaP `1.8794` edge `-0.1021` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.3708` n `103` status `ready` deltaP `-17.6544` edge `-0.2689` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7897` n `143` status `ready` deltaP `-5.7944` edge `-0.5658` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
