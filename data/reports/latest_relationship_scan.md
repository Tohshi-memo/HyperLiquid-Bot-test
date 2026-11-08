# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T06:22:27.353590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4792`

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

- `market_context_high->unknown_4h` score `122.9025` n `37` status `ready` deltaP `-5.0057` edge `10.32` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.2984` n `37` status `ready` deltaP `35.7531` edge `0.0455` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2916` n `37` status `ready` deltaP `10.8068` edge `0.2482` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.9927` n `37` status `ready` deltaP `26.0506` edge `0.0394` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.8044` n `52` status `ready` deltaP `10.6303` edge `0.1016` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.9689` n `52` status `ready` deltaP `8.2082` edge `0.1434` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.8011` n `37` status `ready` deltaP `9.9005` edge `0.0593` maxDD `-3.0172`
- `market_context_high->crypto_alt_1h` score `0.5098` n `37` status `ready` deltaP `11.5472` edge `0.0699` maxDD `-3.1881`
- `market_context_high->fx_1h` score `0.4338` n `37` status `ready` deltaP `7.2221` edge `0.0151` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.3327` n `52` status `ready` deltaP `10.3541` edge `0.0214` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.3213` n `37` status `ready` deltaP `2.2496` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2781` n `52` status `ready` deltaP `6.851` edge `0.1568` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.1615` n `37` status `ready` deltaP `9.767` edge `0.0102` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.1041` n `54` status `ready` deltaP `8.3056` edge `0.0033` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `0.0636` n `37` status `ready` deltaP `4.359` edge `0.0245` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.0518` n `52` status `ready` deltaP `6.5431` edge `0.0069` maxDD `-0.1771`
- `market_context_high->metal_1h` score `-0.0178` n `37` status `ready` deltaP `2.0999` edge `0.0165` maxDD `-0.6226`
- `news_risk_high->equity_1h` score `-0.0953` n `54` status `ready` deltaP `-0.5046` edge `0.0461` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2436` n `54` status `ready` deltaP `0.6155` edge `0.0032` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.6543` n `37` status `ready` deltaP `22.7093` edge `0.0927` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
