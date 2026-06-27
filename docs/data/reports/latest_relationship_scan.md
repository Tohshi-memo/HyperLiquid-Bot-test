# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T00:07:27.609647+00:00`
- Price records: `672`
- Market context records: `4879`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `16.1178` n `110` status `ready` deltaP `10.0218` edge `1.3181` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5864` n `110` status `ready` deltaP `23.0099` edge `0.6986` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4496` n `110` status `ready` deltaP `21.2084` edge `0.5313` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.176` n `110` status `ready` deltaP `18.4922` edge `0.5138` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1001` n `91` status `ready` deltaP `24.7749` edge `0.2941` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1696` n `110` status `ready` deltaP `8.52` edge `0.1069` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8688` n `110` status `ready` deltaP `12.439` edge `0.1666` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5913` n `110` status `ready` deltaP `12.1452` edge `0.0411` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.457` n `110` status `ready` deltaP `6.3201` edge `0.1203` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4519` n `110` status `ready` deltaP `8.3206` edge `0.1047` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2051` n `110` status `ready` deltaP `4.0855` edge `0.0588` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1775` n `110` status `ready` deltaP `0.694` edge `0.0306` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2394` n `110` status `ready` deltaP `3.1328` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4931` n `110` status `ready` deltaP `0.1606` edge `0.0112` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6442` n `110` status `ready` deltaP `1.372` edge `0.0053` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9398` n `110` status `ready` deltaP `5.6624` edge `0.0026` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3226` n `110` status `ready` deltaP `-6.7175` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8078` n `91` status `ready` deltaP `-5.9887` edge `-0.0097` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5886` n `91` status `ready` deltaP `-5.9295` edge `-0.1402` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0234` n `91` status `ready` deltaP `13.2841` edge `0.0037` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
