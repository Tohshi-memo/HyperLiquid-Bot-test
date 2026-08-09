# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T04:22:23.440237+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.4824` n `103` status `ready` deltaP `4.5729` edge `0.5657` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6851` n `103` status `ready` deltaP `13.2535` edge `0.193` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4269` n `131` status `ready` deltaP `15.195` edge `0.0849` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9352` n `140` status `ready` deltaP `11.6595` edge `0.0345` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8097` n `103` status `ready` deltaP `21.4013` edge `0.0478` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.529` n `103` status `ready` deltaP `9.1002` edge `0.1603` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3081` n `140` status `ready` deltaP `4.136` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3395` n `131` status `ready` deltaP `7.4008` edge `-0.0023` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6441` n `140` status `ready` deltaP `-3.9136` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6768` n `131` status `ready` deltaP `-2.0481` edge `-0.0126` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.8459` n `140` status `ready` deltaP `-3.7297` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9405` n `140` status `ready` deltaP `0.1325` edge `0.0036` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0445` n `131` status `ready` deltaP `-2.1947` edge `-0.0184` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0767` n `140` status `ready` deltaP `-11.3216` edge `-0.0334` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6037` n `131` status `ready` deltaP `-1.5825` edge `-0.0727` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2899` n `140` status `ready` deltaP `-11.5312` edge `-0.0652` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.3883` n `103` status `ready` deltaP `6.2197` edge `-0.0744` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.2121` n `131` status `ready` deltaP `-9.684` edge `-0.1208` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5178` n `103` status `ready` deltaP `-12.4461` edge `-0.1492` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.2669` n `140` status `ready` deltaP `-5.864` edge `-0.6051` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
