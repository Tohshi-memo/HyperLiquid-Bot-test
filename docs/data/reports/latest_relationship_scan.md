# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T15:22:25.737543+00:00`
- Price records: `672`
- Market context records: `4946`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9456`

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

- `market_context_high->unknown_1h` score `18.7776` n `97` status `ready` deltaP `10.0593` edge `1.5395` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.115` n `94` status `ready` deltaP `28.2596` edge `0.8726` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.1836` n `94` status `ready` deltaP `20.6766` edge `0.5832` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `6.9629` n `94` status `ready` deltaP `21.2799` edge `0.5736` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8324` n `91` status `ready` deltaP `27.0891` edge `0.3397` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7397` n `94` status `ready` deltaP `14.433` edge `0.1869` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.6329` n `94` status `ready` deltaP `12.4806` edge `0.1191` maxDD `-1.9651`
- `market_context_high->index_4h` score `0.9603` n `94` status `ready` deltaP `12.3151` edge `0.0441` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8269` n `97` status `ready` deltaP `7.5823` edge `0.0757` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8216` n `97` status `ready` deltaP `8.5314` edge `0.1523` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.6386` n `97` status `ready` deltaP `9.3617` edge `0.1217` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.0626` n `97` status `ready` deltaP `4.1252` edge `0.0357` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4089` n `97` status `ready` deltaP `0.9985` edge `0.0069` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4203` n `97` status `ready` deltaP `1.3797` edge `0.0124` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.9811` n `94` status `ready` deltaP `6.2564` edge `-0.0048` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.1207` n `94` status `ready` deltaP `-6.3797` edge `-0.0041` maxDD `-1.0967`
- `market_context_high->fx_24h` score `-1.3875` n `91` status `ready` deltaP `-0.4349` edge `-0.0117` maxDD `-2.749`
- `market_context_high->fx_1h` score `-1.5792` n `97` status `ready` deltaP `-9.7259` edge `-0.0055` maxDD `-0.5675`
- `market_context_high->commodity_24h` score `-4.0307` n `91` status `ready` deltaP `19.6485` edge `0.044` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.8751` n `91` status `ready` deltaP `-8.6463` edge `0.0302` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
