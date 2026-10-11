# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T08:52:23.356640+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5970`

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

- `market_context_high->unknown_4h` score `42.6363` n `85` status `ready` deltaP `-12.9484` edge `3.6974` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4856` n `66` status `ready` deltaP `37.058` edge `0.5863` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.0157` n `66` status `ready` deltaP `9.5959` edge `1.1503` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.5374` n `85` status `ready` deltaP `21.702` edge `0.0118` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.6792` n `66` status `ready` deltaP `15.2936` edge `0.1105` maxDD `-1.364`
- `market_context_high->fx_1h` score `0.1187` n `97` status `ready` deltaP `5.5852` edge `0.0022` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.1086` n `85` status `ready` deltaP `8.2173` edge `0.0076` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.0564` n `97` status `ready` deltaP `3.3907` edge `0.0072` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.3798` n `97` status `ready` deltaP `1.3797` edge `0.031` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.5208` n `97` status `ready` deltaP `-1.2809` edge `0.0013` maxDD `-0.7626`
- `market_context_high->fx_24h` score `-0.5867` n `66` status `ready` deltaP `6.4078` edge `0.0082` maxDD `-1.4241`
- `market_context_high->crypto_major_4h` score `-0.6418` n `85` status `ready` deltaP `1.4365` edge `0.1105` maxDD `-10.5224`
- `market_context_high->crypto_alt_1h` score `-0.9734` n `97` status `ready` deltaP `-4.3907` edge `0.0204` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.0079` n `66` status `ready` deltaP `-3.9931` edge `0.0459` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.2606` n `85` status `ready` deltaP `-10.3049` edge `0.0003` maxDD `-1.1242`
- `market_context_high->equity_1h` score `-1.5475` n `97` status `ready` deltaP `-5.3398` edge `-0.0064` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.5695` n `97` status `ready` deltaP `-6.2689` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->metal_4h` score `-1.6179` n `85` status `ready` deltaP `-9.6521` edge `0.0143` maxDD `-1.1153`
- `market_context_high->crypto_alt_24h` score `-2.1054` n `66` status `ready` deltaP `-5.3978` edge `0.3773` maxDD `-35.5652`
- `market_context_high->crypto_alt_4h` score `-2.6154` n `85` status `ready` deltaP `-14.5302` edge `0.0174` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
