# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T01:22:27.051225+00:00`
- Price records: `672`
- Market context records: `4884`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7586`

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

- `market_context_high->unknown_1h` score `15.9907` n `110` status `ready` deltaP `9.423` edge `1.3115` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5383` n `110` status `ready` deltaP `22.8575` edge `0.6956` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4218` n `110` status `ready` deltaP `21.056` edge `0.53` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.2108` n `110` status `ready` deltaP `18.4922` edge `0.5167` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.0146` n `91` status `ready` deltaP `24.0804` edge `0.2916` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1223` n `110` status `ready` deltaP `8.0627` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8711` n `110` status `ready` deltaP `12.439` edge `0.1669` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5905` n `110` status `ready` deltaP `12.1452` edge `0.041` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4866` n `110` status `ready` deltaP `6.6195` edge `0.1221` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4254` n `110` status `ready` deltaP `8.0212` edge `0.1033` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1973` n `110` status `ready` deltaP `3.9358` edge `0.0588` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1939` n `110` status `ready` deltaP `0.3946` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2355` n `110` status `ready` deltaP `3.1328` edge `0.0149` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5172` n `110` status `ready` deltaP `-0.2885` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6791` n `110` status `ready` deltaP `0.7622` edge `0.0049` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9338` n `110` status `ready` deltaP `5.6624` edge `0.0031` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3106` n `110` status `ready` deltaP `-6.5678` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7439` n `91` status `ready` deltaP `-5.2942` edge `-0.009` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5369` n `91` status `ready` deltaP `-5.2351` edge `-0.1382` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.8904` n `91` status `ready` deltaP `14.1521` edge `0.009` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
