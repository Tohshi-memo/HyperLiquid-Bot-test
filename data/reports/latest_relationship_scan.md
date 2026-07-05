# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T22:22:29.411920+00:00`
- Price records: `672`
- Market context records: `5818`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.3081` n `284` status `ready` deltaP `6.2779` edge `0.1296` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.0643` n `248` status `ready` deltaP `15.3954` edge `0.3999` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.199` n `284` status `ready` deltaP `3.2744` edge `0.0012` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5572` n `284` status `ready` deltaP `-1.2229` edge `-0.0024` maxDD `-2.2045`
- `market_context_high->metal_1h` score `-0.6137` n `284` status `ready` deltaP `2.332` edge `0.0004` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6301` n `284` status `ready` deltaP `0.369` edge `0.003` maxDD `-0.8994`
- `market_context_high->equity_1h` score `-0.6932` n `284` status `ready` deltaP `2.4796` edge `0.0264` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8635` n `284` status `ready` deltaP `3.2913` edge `0.0382` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0361` n `284` status `ready` deltaP `1.7859` edge `0.0352` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1973` n `284` status `ready` deltaP `0.4401` edge `0.0123` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4719` n `284` status `ready` deltaP `0.4359` edge `0.0033` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4816` n `248` status `ready` deltaP `9.4422` edge `0.0289` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1471` n `284` status `ready` deltaP `-4.0901` edge `-0.0421` maxDD `-9.1388`
- `market_context_high->crypto_major_4h` score `-2.6984` n `284` status `ready` deltaP `7.9762` edge `0.1592` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7128` n `284` status `ready` deltaP `-1.3591` edge `-0.0172` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8167` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4308` n `284` status `ready` deltaP `5.4169` edge `0.0955` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.8125` n `248` status `ready` deltaP `-12.4608` edge `-0.062` maxDD `-30.6761`
- `market_context_high->metal_24h` score `-7.7347` n `248` status `ready` deltaP `-3.1586` edge `-0.2298` maxDD `-17.4963`
- `market_context_high->crypto_alt_24h` score `-12.3082` n `248` status `ready` deltaP `-9.5654` edge `-0.4856` maxDD `-61.6215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
