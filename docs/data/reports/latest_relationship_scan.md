# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T09:37:17.696712+00:00`
- Price records: `672`
- Market context records: `1830`
- Flow alert records: `7166`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.9157` n `192` status `ready` deltaP `22.7515` edge `0.5391` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.6863` n `178` status `ready` deltaP `26.5489` edge `0.6228` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4619` n `192` status `ready` deltaP `26.3847` edge `0.4872` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.3624` n `30` status `ready` deltaP `28.496` edge `0.4057` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.4273` n `192` status `ready` deltaP `17.0604` edge `0.4576` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.571` n `178` status `ready` deltaP `17.8683` edge `0.3013` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2494` n `30` status `ready` deltaP `24.7206` edge `0.1377` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9939` n `192` status `ready` deltaP `16.8064` edge `0.2469` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7135` n `178` status `ready` deltaP `14.56` edge `0.6611` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.1495` n `178` status `ready` deltaP `15.7147` edge `0.5642` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `0.9003` n `30` status `ready` deltaP `21.6362` edge `-0.0016` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8254` n `192` status `ready` deltaP `12.0427` edge `0.0974` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4086` n `196` status `ready` deltaP `6.04` edge `0.0924` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.281` n `196` status `ready` deltaP `6.2233` edge `0.0933` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.1646` n `30` status `ready` deltaP `7.9979` edge `0.0401` maxDD `-2.7857`
- `market_context_high->crypto_major_24h` score `0.04` n `178` status `ready` deltaP `18.5121` edge `0.7385` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.0435` n `196` status `ready` deltaP `4.7324` edge `0.0442` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1032` n `178` status `ready` deltaP `11.9558` edge `0.0166` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4761` n `30` status `ready` deltaP `16.1078` edge `-0.1212` maxDD `-2.1115`
- `news_risk_high->fx_1h` score `-0.5216` n `30` status `ready` deltaP `-6.0279` edge `-0.0005` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
