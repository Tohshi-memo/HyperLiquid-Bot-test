# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T02:07:22.996421+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.041` n `68` status `ready` deltaP `8.42` edge `0.1554` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7679` n `68` status `ready` deltaP `13.5402` edge `0.0215` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3248` n `68` status `ready` deltaP `9.324` edge `0.1463` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0417` n `68` status `ready` deltaP `7.1064` edge `0.0033` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.1455` n `68` status `ready` deltaP `3.3806` edge `0.0034` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.173` n `68` status `ready` deltaP `-3.5335` edge `0.0534` maxDD `-0.2073`
- `news_risk_high->equity_1h` score `-0.1876` n `68` status `ready` deltaP `-2.0694` edge `0.0447` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.285` n `68` status `ready` deltaP `0.0705` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4861` n `68` status `ready` deltaP `-2.9676` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.226` n `68` status `ready` deltaP `-3.9186` edge `-0.0405` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.6285` n `68` status `ready` deltaP `-6.3845` edge `-0.0058` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-2.1624` n `68` status `ready` deltaP `-14.5826` edge `-0.0044` maxDD `-1.2868`
- `news_risk_high->crypto_major_1h` score `-2.3465` n `68` status `ready` deltaP `-9.5192` edge `-0.0382` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.5271` n `68` status `ready` deltaP `-5.9792` edge `-0.0532` maxDD `-5.4024`
- `news_risk_high->crypto_alt_4h` score `-2.7572` n `68` status `ready` deltaP `-7.2991` edge `-0.0428` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.5025` n `68` status `ready` deltaP `-2.3897` edge `-0.2435` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.7085` n `68` status `ready` deltaP `23.7132` edge `0.5251` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.6735` n `68` status `ready` deltaP `-32.604` edge `-0.0123` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.4141` n `68` status `ready` deltaP `-30.2287` edge `-0.0984` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.4228` n `68` status `ready` deltaP `-29.136` edge `-0.074` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
