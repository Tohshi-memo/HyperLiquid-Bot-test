# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T18:37:35.495616+00:00`
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

- `market_context_high->unknown_24h` score `1600.0051` n `134` status `ready` deltaP `-5.3949` edge `133.4127` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `128.565` n `68` status `ready` deltaP `-1.8581` edge `10.7387` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `30.887` n `134` status `ready` deltaP `0.7212` edge `2.5824` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3806` n `56` status `ready` deltaP `25.4137` edge `0.4853` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.9985` n `134` status `ready` deltaP `16.6589` edge `0.5812` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5578` n `134` status `ready` deltaP `35.2638` edge `0.0797` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.1294` n `56` status `ready` deltaP `9.5819` edge `0.064` maxDD `-0.7008`
- `news_risk_high->crypto_alt_1h` score `0.5164` n `68` status `ready` deltaP `4.7904` edge `0.0822` maxDD `-3.3547`
- `market_context_high->equity_1h` score `0.426` n `134` status `ready` deltaP `5.6797` edge `0.0852` maxDD `-2.3383`
- `market_context_high->metal_1h` score `0.4257` n `134` status `ready` deltaP `11.5024` edge `0.0158` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3976` n `134` status `ready` deltaP `16.1358` edge `0.033` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2245` n `134` status `ready` deltaP `13.633` edge `0.0497` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.1607` n `134` status `ready` deltaP `3.3059` edge `0.157` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.09` n `134` status `ready` deltaP `7.6146` edge `0.0595` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.314` n `134` status `ready` deltaP `1.7942` edge `0.0133` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5046` n `134` status `ready` deltaP `-0.3208` edge `-0.0027` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5289` n `68` status `ready` deltaP `-1.8933` edge `0.0188` maxDD `-0.6872`
- `market_context_high->index_1h` score `-0.7851` n `134` status `ready` deltaP `-1.6467` edge `0.0014` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8399` n `134` status `ready` deltaP `3.2979` edge `0.0568` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
