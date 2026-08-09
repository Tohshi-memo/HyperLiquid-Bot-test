# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T04:37:27.074140+00:00`
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

- `market_context_high->equity_24h` score `3.5028` n `103` status `ready` deltaP `4.5729` edge `0.5674` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6899` n `103` status `ready` deltaP `13.2535` edge `0.1934` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4233` n `132` status `ready` deltaP `15.2855` edge `0.084` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9196` n `140` status `ready` deltaP `11.5098` edge `0.0342` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.809` n `103` status `ready` deltaP `21.4013` edge `0.0477` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5322` n `103` status `ready` deltaP `9.1002` edge `0.1607` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3093` n `140` status `ready` deltaP `4.136` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3244` n `132` status `ready` deltaP `7.5896` edge `-0.0023` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6441` n `140` status `ready` deltaP `-3.9136` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6903` n `132` status `ready` deltaP `-2.3235` edge `-0.0125` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.8459` n `140` status `ready` deltaP `-3.7297` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9525` n `140` status `ready` deltaP `-0.0172` edge `0.0036` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0611` n `132` status `ready` deltaP `-2.4991` edge `-0.0185` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0959` n `140` status `ready` deltaP `-11.4713` edge `-0.034` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.629` n `132` status `ready` deltaP `-1.8986` edge `-0.0727` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3031` n `140` status `ready` deltaP `-11.6809` edge `-0.0653` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.3631` n `103` status `ready` deltaP `6.2197` edge `-0.0723` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.1285` n `132` status `ready` deltaP `-9.2849` edge `-0.1165` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5298` n `103` status `ready` deltaP `-12.4461` edge `-0.1502` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.2561` n `140` status `ready` deltaP `-5.864` edge `-0.6042` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
