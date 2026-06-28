# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T06:07:30.438346+00:00`
- Price records: `672`
- Market context records: `5012`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10194`

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

- `market_context_high->unknown_1h` score `15.3896` n `93` status `ready` deltaP `3.8182` edge `1.3071` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.3073` n `93` status `ready` deltaP `21.7545` edge `0.7328` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.7051` n `93` status `ready` deltaP `17.7092` edge `0.5158` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2854` n `93` status `ready` deltaP `14.331` edge `0.4843` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `2.4929` n `74` status `ready` deltaP `28.4253` edge `0.0525` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3669` n `93` status `ready` deltaP `14.6112` edge `0.1244` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.9579` n `93` status `ready` deltaP `9.085` edge `0.0766` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8692` n `93` status `ready` deltaP `6.7027` edge `0.1195` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5516` n `93` status `ready` deltaP `4.6453` edge `0.1779` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3784` n `93` status `ready` deltaP `6.4033` edge `0.0385` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.175` n `93` status `ready` deltaP `5.1107` edge `0.0906` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0547` n `93` status `ready` deltaP `4.6289` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1243` n `74` status `ready` deltaP `8.1691` edge `0.0058` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2948` n `93` status `ready` deltaP `2.0073` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5455` n `93` status `ready` deltaP `2.3614` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7884` n `93` status `ready` deltaP `4.0028` edge `-0.0025` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.733` n `93` status `ready` deltaP `-11.6992` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.0126` n `74` status `ready` deltaP `2.2569` edge `0.016` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.3155` n `74` status `ready` deltaP `4.2323` edge `-0.0706` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
