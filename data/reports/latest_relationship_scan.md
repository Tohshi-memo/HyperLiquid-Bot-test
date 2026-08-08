# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T16:52:27.607587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `market_context_high->equity_24h` score `3.0727` n `102` status `ready` deltaP `4.4015` edge `0.5327` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.381` n `102` status `ready` deltaP `11.8668` edge `0.1769` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5214` n `103` status `ready` deltaP `14.5912` edge `0.0968` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0527` n `102` status `ready` deltaP `24.8877` edge `0.0557` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0481` n `104` status `ready` deltaP `12.2006` edge `0.0403` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3904` n `102` status `ready` deltaP `8.8337` edge `0.1443` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.5121` n `104` status `ready` deltaP `2.9825` edge `0.0203` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.5561` n `104` status `ready` deltaP `1.4106` edge `-0.0062` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5713` n `104` status `ready` deltaP `-4.1283` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6393` n `104` status `ready` deltaP `-4.0016` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.681` n `103` status `ready` deltaP `-2.3384` edge `-0.0112` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8807` n `103` status `ready` deltaP `1.1751` edge `-0.0059` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9714` n `104` status `ready` deltaP `-11.0951` edge `-0.0274` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.047` n `103` status `ready` deltaP `1.5214` edge `-0.047` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.1588` n `102` status `ready` deltaP `6.638` edge `-0.0716` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.4978` n `104` status `ready` deltaP `-8.1011` edge `-0.0545` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.8198` n `102` status `ready` deltaP `-12.8268` edge `-0.0885` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.3204` n `103` status `ready` deltaP `-11.6461` edge `-0.1172` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0089` n `103` status `ready` deltaP `-14.7111` edge `-0.2302` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
