# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T17:52:26.848326+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4304`

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

- `market_context_high->unknown_4h` score `132.198` n `37` status `ready` deltaP `-8.5118` edge `11.118` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4154` n `37` status `ready` deltaP `37.1251` edge `0.0461` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1418` n `37` status `ready` deltaP `9.1601` edge `0.2467` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9745` n `37` status `ready` deltaP `25.8982` edge `0.0389` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.5959` n `52` status `ready` deltaP `8.8942` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8383` n `52` status `ready` deltaP `6.8363` edge `0.1358` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.734` n `37` status `ready` deltaP `9.3017` edge `0.0577` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4397` n `37` status `ready` deltaP `10.9484` edge `0.0649` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3209` n `52` status `ready` deltaP `10.2017` edge `0.0209` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2362` n `37` status `ready` deltaP `1.2017` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1962` n `52` status `ready` deltaP `6.851` edge `0.1463` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1278` n `52` status `ready` deltaP `7.9151` edge `0.0075` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1` n `37` status `ready` deltaP `8.7191` edge `0.0093` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0211` n `37` status `ready` deltaP `2.987` edge `0.0228` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0349` n `37` status `ready` deltaP `1.8005` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.038` n `52` status `ready` deltaP `5.6195` edge `0.003` maxDD `-0.2931`
- `news_risk_high->fx_1h` score `-0.2718` n `52` status `ready` deltaP `0.1037` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3166` n `52` status `ready` deltaP `-4.1456` edge `0.042` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7849` n `37` status `ready` deltaP `21.3374` edge `0.0851` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
