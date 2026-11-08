# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T00:37:27.976884+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4416`

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

- `market_context_high->unknown_4h` score `120.7427` n `37` status `ready` deltaP `-7.5972` edge `10.1573` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4666` n `37` status `ready` deltaP `37.7348` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1514` n `37` status `ready` deltaP `9.3098` edge `0.2465` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8599` n `37` status `ready` deltaP `24.5262` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7142` n `52` status `ready` deltaP `10.2831` edge `0.0964` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8674` n `52` status `ready` deltaP `7.1412` edge `0.1375` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7136` n `37` status `ready` deltaP `9.152` edge `0.057` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.496` n `37` status `ready` deltaP `7.9706` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3969` n `37` status `ready` deltaP `10.3496` edge `0.0634` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2464` n `52` status `ready` deltaP `8.8297` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2111` n `37` status `ready` deltaP `0.9023` edge `0.0386` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2017` n `52` status `ready` deltaP `6.851` edge `0.147` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1611` n `52` status `ready` deltaP `8.5248` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1467` n `37` status `ready` deltaP `9.4676` edge `0.0103` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0074` n `37` status `ready` deltaP `3.4443` edge `0.0234` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0497` n `37` status `ready` deltaP `1.5011` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0543` n `52` status `ready` deltaP `5.3201` edge `0.0029` maxDD `-0.2931`
- `news_risk_high->fx_1h` score `-0.2951` n `52` status `ready` deltaP `-0.3454` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3104` n `52` status `ready` deltaP `-3.9959` edge `0.0418` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7558` n `37` status `ready` deltaP `21.6423` edge `0.0868` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
