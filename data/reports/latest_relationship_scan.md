# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T18:22:28.842577+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7098`

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

- `market_context_high->unknown_24h` score `1600.9514` n `134` status `ready` deltaP `-5.2213` edge `133.4904` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `123.8632` n `67` status `ready` deltaP `-2.0556` edge `10.3482` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `30.928` n `134` status `ready` deltaP `0.8737` edge `2.5848` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.4466` n `55` status `ready` deltaP `25.1441` edge `0.4926` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.8821` n `134` status `ready` deltaP `16.6589` edge `0.5715` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.547` n `134` status `ready` deltaP `35.2638` edge `0.0788` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.21` n `55` status `ready` deltaP `10.4684` edge `0.0648` maxDD `-0.7008`
- `news_risk_high->crypto_alt_1h` score `0.7105` n `67` status `ready` deltaP `5.5367` edge `0.0934` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4257` n `134` status `ready` deltaP `11.5024` edge `0.0158` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.4212` n `134` status `ready` deltaP `5.6797` edge `0.0848` maxDD `-2.3383`
- `market_context_high->metal_4h` score `0.3953` n `134` status `ready` deltaP `16.1358` edge `0.0327` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2087` n `134` status `ready` deltaP `13.4806` edge `0.0494` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.1397` n `134` status `ready` deltaP `3.3059` edge `0.1543` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0888` n `134` status `ready` deltaP `7.6146` edge `0.0594` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3296` n `134` status `ready` deltaP `1.6445` edge `0.013` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4631` n `67` status `ready` deltaP `-1.3406` edge `0.0206` maxDD `-0.6872`
- `market_context_high->fx_4h` score `-0.5053` n `134` status `ready` deltaP `-0.3208` edge `-0.0028` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.7863` n `134` status `ready` deltaP `-1.6467` edge `0.0013` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8353` n `134` status `ready` deltaP `3.2979` edge `0.0574` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
