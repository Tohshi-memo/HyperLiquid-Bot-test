# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T12:37:24.140405+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `3.137` n `37` status `ready` deltaP `9.1601` edge `0.2463` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2573` n `62` status `ready` deltaP `11.6837` edge `0.1572` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7207` n `37` status `ready` deltaP `9.4514` edge `0.0556` maxDD `-3.0172`
- `news_risk_high->index_4h` score `0.6263` n `62` status `ready` deltaP `11.8607` edge `0.0209` maxDD `-0.4888`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `news_risk_high->index_24h` score `0.3843` n `62` status `ready` deltaP `10.7975` edge `0.1441` maxDD `-6.6786`
- `market_context_high->crypto_alt_1h` score `0.3805` n `37` status `ready` deltaP `10.4993` edge `0.0603` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.3476` n `37` status `ready` deltaP `2.549` edge `0.039` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1786` n `37` status `ready` deltaP `10.0664` edge `0.0104` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0707` n `62` status `ready` deltaP `7.6492` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->fx_24h` score `0.053` n `62` status `ready` deltaP `-2.7442` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->equity_1h` score `-0.076` n `62` status `ready` deltaP `-0.2994` edge `0.0472` maxDD `-1.396`
- `market_context_high->metal_1h` score `-0.0832` n `37` status `ready` deltaP `0.9023` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1487` n `62` status `ready` deltaP `2.5594` edge `0.0024` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.2199` n `62` status `ready` deltaP `1.8145` edge `0.0043` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5237` n `62` status `ready` deltaP `-3.6749` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9071` n `62` status `ready` deltaP `2.1833` edge `-0.0403` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1097` n `62` status `ready` deltaP `-1.0962` edge `-0.0194` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.1864` n `62` status `ready` deltaP `-2.2472` edge `0.0233` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6482` n `62` status `ready` deltaP `-11.7732` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
