# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T09:22:30.199867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `market_context_high->unknown_4h` score `884.1257` n `30` status `ready` deltaP `8.8415` edge `73.6182` maxDD `0.0`
- `market_context_high->unknown_1h` score `258.054` n `30` status `ready` deltaP `9.0519` edge `21.4548` maxDD `-0.1853`
- `market_context_high->crypto_alt_4h` score `5.1117` n `30` status `ready` deltaP `22.246` edge `0.3071` maxDD `-1.6876`
- `news_risk_high->crypto_alt_24h` score `4.8627` n `107` status `ready` deltaP `25.0065` edge `0.8217` maxDD `-24.8652`
- `market_context_high->equity_4h` score `4.681` n `30` status `ready` deltaP `3.313` edge `0.4382` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `3.8061` n `30` status `ready` deltaP `18.7805` edge `0.2256` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.8307` n `30` status `ready` deltaP `6.517` edge `0.2325` maxDD `-1.2043`
- `market_context_high->index_4h` score `2.4032` n `30` status `ready` deltaP `22.5508` edge `0.0726` maxDD `-0.1474`
- `news_risk_high->crypto_alt_4h` score `1.5779` n `129` status `ready` deltaP `9.9204` edge `0.2748` maxDD `-7.4246`
- `market_context_high->crypto_alt_1h` score `1.0903` n `30` status `ready` deltaP `7.2655` edge `0.1355` maxDD `-1.5324`
- `market_context_high->crypto_major_1h` score `0.9557` n `30` status `ready` deltaP `6.517` edge `0.1181` maxDD `-1.1219`
- `market_context_high->metal_4h` score `0.8786` n `30` status `ready` deltaP `15.3354` edge `0.0442` maxDD `-0.704`
- `market_context_high->commodity_4h` score `0.718` n `30` status `ready` deltaP `16.2296` edge `0.0251` maxDD `-1.633`
- `market_context_high->fx_1h` score `0.7167` n `30` status `ready` deltaP `9.5509` edge `0.0132` maxDD `-0.0388`
- `market_context_high->index_1h` score `0.0227` n `30` status `ready` deltaP `-0.8982` edge `0.032` maxDD `-0.2628`
- `market_context_high->metal_1h` score `-0.0529` n `30` status `ready` deltaP `1.1577` edge `0.0112` maxDD `-0.3895`
- `news_risk_high->crypto_alt_1h` score `-0.2485` n `141` status `ready` deltaP `3.0811` edge `0.0549` maxDD `-4.584`
- `news_risk_high->fx_1h` score `-0.5342` n `141` status `ready` deltaP `0.6147` edge `-0.0025` maxDD `-0.6065`
- `market_context_high->commodity_1h` score `-0.7689` n `30` status `ready` deltaP `-8.2036` edge `0.01` maxDD `-0.6439`
- `market_context_high->fx_4h` score `-0.8914` n `30` status `ready` deltaP `-7.8862` edge `0.0174` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
