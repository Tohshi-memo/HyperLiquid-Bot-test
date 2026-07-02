# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T06:37:27.283148+00:00`
- Price records: `672`
- Market context records: `5429`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11450`

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

- `market_context_high->equity_24h` score `4.7655` n `185` status `ready` deltaP `11.8694` edge `0.6716` maxDD `-21.6219`
- `market_context_high->crypto_major_24h` score `4.7228` n `185` status `ready` deltaP `20.3688` edge `0.7118` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8942` n `196` status `ready` deltaP `16.7652` edge `0.442` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `3.0756` n `196` status `ready` deltaP `12.1329` edge `0.3395` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.7042` n `196` status `ready` deltaP `12.6618` edge `0.3048` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5405` n `196` status `ready` deltaP `8.5299` edge `0.0847` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1653` n `196` status `ready` deltaP `6.9321` edge `0.0169` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0443` n `185` status `ready` deltaP `8.9142` edge `0.0338` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.1689` n `196` status `ready` deltaP `1.8575` edge `0.0697` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.1993` n `196` status `ready` deltaP `3.4706` edge `0.0848` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3914` n `196` status `ready` deltaP `2.8504` edge `0.0159` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5802` n `196` status `ready` deltaP `0.0947` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8985` n `196` status `ready` deltaP `6.7726` edge `0.0409` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0638` n `185` status `ready` deltaP `16.1627` edge `0.1022` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1806` n `196` status `ready` deltaP `0.2894` edge `0.0022` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.514` n `196` status `ready` deltaP `-3.6325` edge `-0.0075` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.7553` n `196` status `ready` deltaP `-9.3423` edge `-0.0385` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.4093` n `196` status `ready` deltaP `-8.0419` edge `-0.05` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-5.8673` n `185` status `ready` deltaP `11.0811` edge `0.3069` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.3605` n `185` status `ready` deltaP `-5.7742` edge `-0.1674` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
