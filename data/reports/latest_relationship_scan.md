# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T12:07:31.701975+00:00`
- Price records: `672`
- Market context records: `4932`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `17.0735` n `102` status `ready` deltaP `10.118` edge `1.3971` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.3503` n `102` status `ready` deltaP `28.781` edge `0.8054` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `7.2128` n `102` status `ready` deltaP `24.0734` edge `0.5758` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.8429` n `102` status `ready` deltaP `19.8679` edge `0.5602` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `6.006` n `86` status `ready` deltaP `26.5141` edge `0.358` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.5983` n `102` status `ready` deltaP `13.7913` edge `0.1794` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.3431` n `102` status `ready` deltaP `9.9534` edge `0.1118` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.7275` n `102` status `ready` deltaP `9.8248` edge `0.0413` maxDD `-0.6938`
- `market_context_high->crypto_major_1h` score `0.4955` n `102` status `ready` deltaP `5.9205` edge `0.1279` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3536` n `102` status `ready` deltaP `5.5008` edge `0.066` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.3082` n `102` status `ready` deltaP `6.5487` edge `0.0981` maxDD `-5.5126`
- `market_context_high->metal_1h` score `-0.0645` n `102` status `ready` deltaP `2.8971` edge `0.0333` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2466` n `102` status `ready` deltaP `2.8443` edge `0.0154` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5263` n `102` status `ready` deltaP `-0.4491` edge `0.011` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7682` n `102` status `ready` deltaP `7.6429` edge `0.0037` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.9376` n `102` status `ready` deltaP `-3.1594` edge `-0.0021` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4794` n `102` status `ready` deltaP `-8.5535` edge `-0.005` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.9751` n `86` status `ready` deltaP `-7.0293` edge `-0.0167` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9323` n `86` status `ready` deltaP `-9.9281` edge `-0.1576` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.082` n `86` status `ready` deltaP `12.9724` edge `0.0009` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
