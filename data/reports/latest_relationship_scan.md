# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T04:43:29.500636+00:00`
- Price records: `614`
- Market context records: `719`
- Flow alert records: `2032`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.4718` n `146` status `ready` deltaP `27.8812` edge `0.8035` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3378` n `146` status `ready` deltaP `8.0024` edge `0.4796` maxDD `-0.0508`
- `market_context_high->fx_1h` score `-0.2837` n `150` status `ready` deltaP `2.8845` edge `0.0022` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.2934` n `149` status `ready` deltaP `6.0346` edge `0.0093` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.4103` n `150` status `ready` deltaP `2.7986` edge `0.0446` maxDD `-3.7959`
- `market_context_high->index_24h` score `-0.6005` n `146` status `ready` deltaP `-1.234` edge `0.1577` maxDD `-5.9609`
- `market_context_high->index_1h` score `-0.6497` n `150` status `ready` deltaP `-0.066` edge `0.0025` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-1.0196` n `149` status `ready` deltaP `17.2925` edge `0.1246` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1625` n `150` status `ready` deltaP `-1.5512` edge `-0.0055` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1746` n `150` status `ready` deltaP `-3.9672` edge `-0.0111` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3812` n `150` status `ready` deltaP `4.6448` edge `-0.0146` maxDD `-8.1842`
- `market_context_high->equity_24h` score `-1.5347` n `146` status `ready` deltaP `-3.0622` edge `0.153` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.6365` n `150` status `ready` deltaP `5.8689` edge `-0.0032` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.8177` n `149` status `ready` deltaP `1.4688` edge `-0.009` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9643` n `149` status `ready` deltaP `3.5824` edge `0.0694` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7602` n `149` status `ready` deltaP `-1.5615` edge `-0.0044` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.429` n `150` status `ready` deltaP `-5.388` edge `-0.0539` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6616` n `149` status `ready` deltaP `-5.6753` edge `0.0828` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.1208` n `149` status `ready` deltaP `3.8877` edge `-0.1815` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1563` n `146` status `ready` deltaP `-13.2562` edge `-0.0555` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
