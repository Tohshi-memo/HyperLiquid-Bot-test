# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T16:52:26.798726+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4192`

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

- `market_context_high->unknown_4h` score `144.0374` n `37` status `ready` deltaP `-8.3594` edge `12.1036` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.3642` n `37` status `ready` deltaP `36.5153` edge `0.0459` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1706` n `37` status `ready` deltaP `9.4595` edge `0.2471` maxDD `-2.3425`
- `market_context_high->index_4h` score `2.0001` n `37` status `ready` deltaP `26.2031` edge `0.039` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.6098` n `52` status `ready` deltaP `9.0678` edge `0.0958` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.7988` n `52` status `ready` deltaP `6.2265` edge `0.1348` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7627` n `37` status `ready` deltaP `9.6011` edge `0.0581` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4942` n `37` status `ready` deltaP `11.5472` edge `0.0679` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.3375` n `52` status `ready` deltaP `10.5066` edge `0.021` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2602` n `37` status `ready` deltaP `1.5011` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.1758` n `52` status `ready` deltaP `6.5038` edge `0.146` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1171` n `37` status `ready` deltaP `9.0185` edge `0.0095` maxDD `-1.7019`
- `news_risk_high->fx_4h` score `0.0945` n `52` status `ready` deltaP `7.3053` edge `0.0073` maxDD `-0.1771`
- `market_context_high->commodity_4h` score `-0.0092` n `37` status `ready` deltaP `3.1395` edge `0.0233` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.0224` n `52` status `ready` deltaP `5.9189` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0272` n `37` status `ready` deltaP `1.9502` edge `0.0163` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2718` n `52` status `ready` deltaP `0.1037` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2979` n `52` status `ready` deltaP `-3.8462` edge `0.0424` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.8245` n `37` status `ready` deltaP `20.7276` edge `0.0841` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
