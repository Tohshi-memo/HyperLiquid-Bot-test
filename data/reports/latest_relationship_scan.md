# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T05:07:33.276574+00:00`
- Price records: `672`
- Market context records: `4900`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8590`

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

- `market_context_high->unknown_1h` score `14.7319` n `110` status `ready` deltaP `9.423` edge `1.2066` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5566` n `110` status `ready` deltaP `23.1624` edge `0.6951` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5303` n `110` status `ready` deltaP `21.5133` edge `0.536` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4478` n `110` status `ready` deltaP `18.9495` edge `0.5334` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2716` n `92` status `ready` deltaP `23.6338` edge `0.316` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1101` n `110` status `ready` deltaP `7.9102` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8953` n `110` status `ready` deltaP `12.439` edge `0.17` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5232` n `110` status `ready` deltaP `10.9257` edge `0.0405` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.5225` n `110` status `ready` deltaP `6.9189` edge `0.1247` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4565` n `110` status `ready` deltaP `8.4703` edge `0.1043` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2394` n `110` status `ready` deltaP `4.5346` edge `0.0602` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.2121` n `110` status `ready` deltaP `3.4322` edge `0.0159` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2172` n `110` status `ready` deltaP `-0.0545` edge `0.0305` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7312` n `110` status `ready` deltaP `0.0` edge `0.0033` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7759` n `110` status `ready` deltaP `7.1868` edge `0.0061` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3657` n `110` status `ready` deltaP `-7.1666` edge `-0.0047` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5886` n `92` status `ready` deltaP `-3.5628` edge `-0.0076` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5097` n `92` status `ready` deltaP `-4.997` edge `-0.1363` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.5844` n `92` status `ready` deltaP `16.2666` edge `0.0204` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
