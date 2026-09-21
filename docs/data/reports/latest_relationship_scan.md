# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T07:52:32.388838+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9154`

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

- `market_context_high->unknown_4h` score `33.0001` n `58` status `ready` deltaP `1.23` edge `2.7568` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.3442` n `101` status `ready` deltaP `11.4428` edge `2.5549` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.1518` n `101` status `ready` deltaP `11.8279` edge `1.9219` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.2827` n `101` status `ready` deltaP `18.919` edge `0.3517` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9635` n `101` status `ready` deltaP `21.2056` edge `0.3147` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7078` n `101` status `ready` deltaP `16.0817` edge `0.165` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1192` n `101` status `ready` deltaP `18.1775` edge `0.1077` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0802` n `101` status `ready` deltaP `22.676` edge `0.1179` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.9206` n `58` status `ready` deltaP `6.9069` edge `0.056` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7484` n `58` status `ready` deltaP `11.0262` edge `0.0144` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.573` n `101` status `ready` deltaP `14.1489` edge `0.0136` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.3527` n `101` status `ready` deltaP `15.2695` edge `0.033` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3438` n `58` status `ready` deltaP `14.9338` edge `0.0082` maxDD `-1.0949`
- `market_context_high->fx_1h` score `0.3211` n `58` status `ready` deltaP `8.4762` edge `0.0059` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.295` n `58` status `ready` deltaP `5.699` edge `0.0174` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2065` n `101` status `ready` deltaP `8.6407` edge `0.0232` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.1543` n `101` status `ready` deltaP `2.5197` edge `0.0109` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1657` n `58` status `ready` deltaP `-1.6415` edge `0.069` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.228` n `101` status `ready` deltaP `2.8428` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.4032` n `101` status `ready` deltaP `9.6036` edge `-0.0313` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
