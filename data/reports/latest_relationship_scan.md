# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T13:37:28.777295+00:00`
- Price records: `672`
- Market context records: `5667`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `2.1539` n `194` status `ready` deltaP `15.8075` edge `0.582` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8605` n `244` status `ready` deltaP `11.228` edge `0.2261` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.3836` n `244` status `ready` deltaP `6.9497` edge `0.1495` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.3413` n `244` status `ready` deltaP `8.2742` edge `0.1582` maxDD `-9.46`
- `market_context_high->fx_24h` score `-0.1964` n `194` status `ready` deltaP `16.6953` edge `0.0516` maxDD `-2.6747`
- `market_context_high->fx_1h` score `-0.2699` n `256` status `ready` deltaP `1.8034` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.473` n `256` status `ready` deltaP `4.5261` edge `0.0311` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5039` n `256` status `ready` deltaP `0.4818` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5216` n `256` status `ready` deltaP `2.2338` edge `0.0378` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.588` n `256` status `ready` deltaP `0.938` edge `0.0052` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7249` n `256` status `ready` deltaP `3.7565` edge `0.0391` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8781` n `256` status `ready` deltaP `0.9567` edge `-0.003` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.208` n `244` status `ready` deltaP `3.2787` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2826` n `244` status `ready` deltaP `-0.8947` edge `0.0087` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4191` n `194` status `ready` deltaP `7.6568` edge `0.0375` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9631` n `244` status `ready` deltaP `-13.1622` edge `-0.0542` maxDD `-11.7017`
- `market_context_high->commodity_4h` score `-3.6952` n `244` status `ready` deltaP `-1.242` edge `-0.0321` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.7683` n `194` status `ready` deltaP `3.7354` edge `0.0276` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4015` n `194` status `ready` deltaP `-13.5971` edge `-0.2509` maxDD `-32.8456`
- `market_context_high->commodity_24h` score `-12.3602` n `194` status `ready` deltaP `-11.8235` edge `-0.0903` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
