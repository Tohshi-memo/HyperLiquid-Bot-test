# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T02:37:29.491097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6593`

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

- `market_context_high->equity_24h` score `9.7013` n `33` status `ready` deltaP `16.7772` edge `0.9697` maxDD `-19.5155`
- `market_context_high->commodity_24h` score `2.3903` n `33` status `ready` deltaP `8.2702` edge `0.2028` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3766` n `33` status `ready` deltaP `16.6667` edge `0.1173` maxDD `-2.4868`
- `market_context_high->metal_1h` score `1.0332` n `67` status `ready` deltaP `12.2375` edge `0.0373` maxDD `-0.6226`
- `market_context_high->equity_1h` score `1.0254` n `67` status `ready` deltaP `5.2283` edge `0.1703` maxDD `-5.5762`
- `market_context_high->fx_24h` score `0.6847` n `33` status `ready` deltaP `10.5587` edge `-0.0045` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.2839` n `55` status `ready` deltaP `6.6796` edge `0.0444` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.0593` n `55` status `ready` deltaP `-0.0166` edge `0.0481` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `-0.1271` n `67` status `ready` deltaP `4.7659` edge `0.0107` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.2154` n `55` status `ready` deltaP `9.3902` edge `0.0123` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.3591` n `67` status `ready` deltaP `0.9004` edge `0.0224` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.4054` n `67` status `ready` deltaP `11.8062` edge `0.0586` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8025` n `67` status `ready` deltaP `-9.2658` edge `-0.0026` maxDD `-0.4145`
- `market_context_high->fx_4h` score `-0.8487` n `55` status `ready` deltaP `-1.1059` edge `0.0025` maxDD `-0.981`
- `market_context_high->metal_24h` score `-1.373` n `33` status `ready` deltaP `2.6515` edge `-0.1384` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.647` n `67` status `ready` deltaP `4.0397` edge `-0.0282` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-5.0504` n `55` status `ready` deltaP `4.2628` edge `-0.0713` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-5.4433` n `33` status `ready` deltaP `-5.8081` edge `-0.0283` maxDD `-24.9269`
- `market_context_high->crypto_alt_4h` score `-8.45` n `55` status `ready` deltaP `3.0987` edge `-0.2544` maxDD `-30.9674`
- `market_context_high->crypto_alt_24h` score `-9.9565` n `33` status `ready` deltaP `-19.4129` edge `-0.206` maxDD `-32.8764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
