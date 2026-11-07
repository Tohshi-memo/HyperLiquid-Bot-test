# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T12:52:25.863350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4003`

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

- `market_context_high->equity_1h` score `3.1239` n `37` status `ready` deltaP `9.0104` edge `0.2462` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2652` n `62` status `ready` deltaP `11.8361` edge `0.1572` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7387` n `37` status `ready` deltaP `9.6011` edge `0.0561` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.6263` n `62` status `ready` deltaP `11.8607` edge `0.0209` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.508` n `37` status `ready` deltaP `8.1203` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3945` n `37` status `ready` deltaP `10.649` edge `0.0611` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.3941` n `62` status `ready` deltaP `10.9711` edge `0.1442` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.3356` n `37` status `ready` deltaP `2.3993` edge `0.039` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1872` n `37` status `ready` deltaP `10.2161` edge `0.0105` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0629` n `62` status `ready` deltaP `7.4995` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.0391` n `62` status `ready` deltaP `-2.9178` edge `0.0669` maxDD `-0.2016`
- `market_context_high->metal_1h` score `-0.0832` n `37` status `ready` deltaP `0.9023` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0846` n `62` status `ready` deltaP `-0.4491` edge `0.0471` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1565` n `62` status `ready` deltaP `2.4097` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2286` n `62` status `ready` deltaP `1.6621` edge `0.0042` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5237` n `62` status `ready` deltaP `-3.6749` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.8984` n `62` status `ready` deltaP `2.3357` edge `-0.0402` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.0956` n `62` status `ready` deltaP `-0.9465` edge `-0.0186` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.1794` n `62` status `ready` deltaP `-2.2472` edge `0.0242` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.635` n `62` status `ready` deltaP `-11.6235` edge `-0.0028` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
