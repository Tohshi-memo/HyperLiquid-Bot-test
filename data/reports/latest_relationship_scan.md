# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T04:52:30.010206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.3172` n `73` status `ready` deltaP `9.7078` edge `0.3325` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.5787` n `73` status `ready` deltaP `12.6469` edge `0.1732` maxDD `-4.666`
- `market_context_high->metal_4h` score `0.4303` n `100` status `ready` deltaP `11.3902` edge `0.0175` maxDD `-1.273`
- `market_context_high->metal_24h` score `0.2428` n `73` status `ready` deltaP `4.8384` edge `0.071` maxDD `-2.3083`
- `market_context_high->crypto_major_4h` score `0.2349` n `100` status `ready` deltaP `7.561` edge `0.0818` maxDD `-3.1677`
- `market_context_high->commodity_4h` score `0.1591` n `100` status `ready` deltaP `9.1037` edge `0.0376` maxDD `-2.4692`
- `market_context_high->index_1h` score `0.0893` n `104` status `ready` deltaP `7.4735` edge `0.0033` maxDD `-0.3343`
- `market_context_high->equity_1h` score `0.0193` n `104` status `ready` deltaP `4.0074` edge `0.0301` maxDD `-1.6811`
- `market_context_high->unknown_1h` score `-0.001` n `104` status `ready` deltaP `7.8823` edge `-0.0291` maxDD `-0.549`
- `market_context_high->fx_4h` score `-0.1968` n `100` status `ready` deltaP `3.628` edge `0.0013` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.3992` n `104` status `ready` deltaP `-0.5124` edge `-0.0016` maxDD `-1.0269`
- `market_context_high->fx_1h` score `-0.5065` n `104` status `ready` deltaP `-1.1746` edge `0.0018` maxDD `-0.2273`
- `market_context_high->crypto_alt_1h` score `-0.587` n `104` status `ready` deltaP `-0.8118` edge `0.0131` maxDD `-2.6358`
- `market_context_high->index_4h` score `-0.5877` n `100` status `ready` deltaP `-2.2622` edge `0.0031` maxDD `-0.403`
- `market_context_high->commodity_1h` score `-0.6911` n `104` status `ready` deltaP `-4.2953` edge `0.0013` maxDD `-1.5684`
- `market_context_high->crypto_alt_4h` score `-0.6936` n `100` status `ready` deltaP `5.6098` edge `0.0665` maxDD `-7.7591`
- `market_context_high->crypto_major_1h` score `-0.7781` n `104` status `ready` deltaP `-1.8597` edge `0.0034` maxDD `-3.2602`
- `market_context_high->equity_4h` score `-0.9378` n `100` status `ready` deltaP `-4.8354` edge `0.0097` maxDD `-3.1489`
- `market_context_high->unknown_24h` score `-1.0436` n `73` status `ready` deltaP `6.2083` edge `-0.0798` maxDD `-0.8847`
- `market_context_high->index_24h` score `-1.2298` n `73` status `ready` deltaP `2.1391` edge `-0.0807` maxDD `-2.9647`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
