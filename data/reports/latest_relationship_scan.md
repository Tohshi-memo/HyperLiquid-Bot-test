# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T22:07:27.815788+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9918`

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

- `market_context_high->unknown_4h` score `26.0457` n `88` status `ready` deltaP `7.043` edge `2.1683` maxDD `-0.9153`
- `market_context_high->equity_24h` score `14.8689` n `52` status `ready` deltaP `23.8401` edge `1.9878` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.6285` n `52` status `ready` deltaP `19.7307` edge `0.2517` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->metal_24h` score `-0.4992` n `52` status `ready` deltaP `9.0755` edge `-0.0468` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.5756` n `88` status `ready` deltaP `-0.6056` edge `-0.0015` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.852` n `88` status `ready` deltaP `-0.026` edge `-0.0113` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9345` n `88` status `ready` deltaP `-3.0597` edge `0.0112` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0924` n `88` status `ready` deltaP `-1.5878` edge `0.0089` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->commodity_24h` score `-1.2203` n `52` status `ready` deltaP `-12.5083` edge `0.0848` maxDD `-5.9626`
- `market_context_high->fx_1h` score `-1.3101` n `88` status `ready` deltaP `-14.0582` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->crypto_alt_24h` score `-1.3719` n `52` status `ready` deltaP `4.4027` edge `0.3042` maxDD `-33.4213`
- `market_context_high->equity_1h` score `-1.7734` n `88` status `ready` deltaP `-8.4036` edge `0.0133` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.8355` n `52` status `ready` deltaP `-10.502` edge `-0.0482` maxDD `-2.7024`
- `market_context_high->crypto_alt_1h` score `-1.9685` n `88` status `ready` deltaP `0.3334` edge `-0.0567` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0835` n `88` status `ready` deltaP `-6.0727` edge `-0.0085` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.215` n `88` status `ready` deltaP `-5.4096` edge `-0.1138` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4187` n `88` status `ready` deltaP `-2.6636` edge `-0.2193` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.153` n `88` status `ready` deltaP `2.0047` edge `-0.2643` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
