# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T00:22:28.387316+00:00`
- Price records: `672`
- Market context records: `4880`
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

- `market_context_high->unknown_1h` score `16.1094` n `110` status `ready` deltaP `10.0218` edge `1.3174` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5732` n `110` status `ready` deltaP `23.0099` edge `0.6975` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4472` n `110` status `ready` deltaP `21.2084` edge `0.5311` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1784` n `110` status `ready` deltaP `18.4922` edge `0.514` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.0754` n `91` status `ready` deltaP `24.6013` edge `0.2932` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1538` n `110` status `ready` deltaP `8.3675` edge `0.1066` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8688` n `110` status `ready` deltaP `12.439` edge `0.1666` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5913` n `110` status `ready` deltaP `12.1452` edge `0.0411` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4562` n `110` status `ready` deltaP `6.3201` edge `0.1202` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4417` n `110` status `ready` deltaP `8.1709` edge `0.1044` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1966` n `110` status `ready` deltaP `3.9358` edge `0.0587` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1853` n `110` status `ready` deltaP `0.5443` edge `0.0306` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2479` n `110` status `ready` deltaP `2.9831` edge `0.0143` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5016` n `110` status `ready` deltaP `0.0109` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.653` n `110` status `ready` deltaP `1.2195` edge `0.0052` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9422` n `110` status `ready` deltaP `5.6624` edge `0.0024` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3106` n `110` status `ready` deltaP `-6.5678` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7916` n `91` status `ready` deltaP `-5.8151` edge `-0.0095` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5757` n `91` status `ready` deltaP `-5.7559` edge `-0.1397` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.9975` n `91` status `ready` deltaP `13.4577` edge `0.0047` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
