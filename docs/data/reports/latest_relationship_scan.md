# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T06:37:28.095526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8749` n `91` status `ready` deltaP `-6.3404` edge `3.5024` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4325` n `91` status `ready` deltaP `33.7841` edge `0.6037` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.771` n `91` status `ready` deltaP `18.6166` edge `1.3152` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5711` n `91` status `ready` deltaP `10.0578` edge `0.7456` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.3976` n `91` status `ready` deltaP `16.4869` edge `0.2023` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2607` n `91` status `ready` deltaP `6.6971` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1564` n `91` status `ready` deltaP `9.2453` edge `0.0473` maxDD `-3.7778`
- `market_context_high->fx_4h` score `-0.0307` n `91` status `ready` deltaP `9.5886` edge `0.0082` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2978` n `91` status `ready` deltaP `3.7475` edge `0.0014` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3785` n `91` status `ready` deltaP `7.8638` edge `0.09` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3866` n `91` status `ready` deltaP `0.4031` edge `0.0027` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3926` n `91` status `ready` deltaP `6.024` edge `0.058` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.7369` n `91` status `ready` deltaP `-1.9465` edge `-0.0115` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9399` n `91` status `ready` deltaP `-4.7377` edge `-0.0049` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9728` n `91` status `ready` deltaP `-5.6185` edge `0.0135` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-0.9918` n `91` status `ready` deltaP `-3.9185` edge `-0.015` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-1.1309` n `91` status `ready` deltaP `-8.1715` edge `0.1028` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1915` n `91` status `ready` deltaP `-2.2438` edge `0.0295` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2497` n `91` status `ready` deltaP `-10.637` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2969` n `91` status `ready` deltaP `-11.0175` edge `0.0004` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
