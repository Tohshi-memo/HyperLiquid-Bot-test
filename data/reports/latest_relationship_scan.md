# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T21:07:30.952784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10649`

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

- `risk_on_high->unknown_4h` score `20.8461` n `137` status `ready` deltaP `-1.0749` edge `1.9449` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.8461` n `137` status `ready` deltaP `-1.0749` edge `1.9449` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `7.9142` n `228` status `ready` deltaP `2.0913` edge `0.8924` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.7007` n `37` status `ready` deltaP `25.1783` edge `0.4175` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8491` n `37` status `ready` deltaP `20.1389` edge `0.1865` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2627` n `37` status `ready` deltaP `16.5706` edge `0.2027` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3381` n `37` status `ready` deltaP `23.694` edge `0.059` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6439` n `37` status `ready` deltaP `8.5325` edge `0.1002` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6063` n `37` status `ready` deltaP `13.2344` edge `0.0847` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.3317` n `37` status `ready` deltaP `15.9128` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1383` n `37` status `ready` deltaP `14.2742` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1223` n `37` status `ready` deltaP `5.8667` edge `0.0727` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.8866` n `37` status `ready` deltaP `8.5775` edge `0.0432` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.8436` n `37` status `ready` deltaP `19.0878` edge `0.0446` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.8375` n `164` status `ready` deltaP `12.2332` edge `0.4227` maxDD `-20.757`
- `news_risk_high->crypto_major_24h` score `0.4909` n `37` status `ready` deltaP `16.4039` edge `0.2312` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.3335` n `37` status `ready` deltaP `4.5691` edge `0.0302` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0202` n `145` status `ready` deltaP `6.7066` edge `-0.0026` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0202` n `145` status `ready` deltaP `6.7066` edge `-0.0026` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0433` n `37` status `ready` deltaP `5.4257` edge `0.0029` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
