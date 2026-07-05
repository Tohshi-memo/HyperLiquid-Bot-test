# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T16:07:30.532951+00:00`
- Price records: `672`
- Market context records: `5788`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8106`

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

- `market_context_high->equity_24h` score `0.4448` n `244` status `ready` deltaP `15.1838` edge `0.4637` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0049` n `301` status `ready` deltaP `6.7437` edge `0.1185` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2396` n `305` status `ready` deltaP `2.5233` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.627` n `305` status `ready` deltaP `3.292` edge `0.0265` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6455` n `305` status `ready` deltaP `2.2092` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7259` n `305` status `ready` deltaP `-1.1971` edge `-0.0046` maxDD `-3.7721`
- `market_context_high->index_1h` score `-0.9772` n `305` status `ready` deltaP `0.2705` edge `0.0036` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.9894` n `305` status `ready` deltaP `2.7226` edge `0.0315` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-1.0221` n `244` status `ready` deltaP `14.0227` edge `0.0396` maxDD `-4.1297`
- `market_context_high->crypto_alt_1h` score `-1.1011` n `305` status `ready` deltaP `1.6178` edge `0.0309` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2014` n `301` status `ready` deltaP `0.6311` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4475` n `301` status `ready` deltaP `0.4552` edge `0.0035` maxDD `-2.0352`
- `market_context_high->commodity_4h` score `-2.455` n `301` status `ready` deltaP `-3.2691` edge `-0.0254` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8379` n `244` status `ready` deltaP `3.0653` edge `0.0302` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9684` n `301` status `ready` deltaP `7.5257` edge `0.1397` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8206` n `301` status `ready` deltaP `-5.2396` edge `-0.0475` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.5676` n `301` status `ready` deltaP `5.2979` edge `0.0849` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.1037` n `244` status `ready` deltaP `-7.9207` edge `-0.251` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.5015` n `244` status `ready` deltaP `1.4999` edge `-0.1186` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.019` n `244` status `ready` deltaP `-14.6146` edge `-0.0832` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
