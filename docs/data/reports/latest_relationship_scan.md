# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T14:22:22.212552+00:00`
- Price records: `557`
- Market context records: `653`
- Flow alert records: `1854`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.5793` n `146` status `ready` deltaP `19.9804` edge `0.5318` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.0578` n `146` status `ready` deltaP `8.6426` edge `0.452` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1487` n `146` status `ready` deltaP `8.1261` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3515` n `146` status `ready` deltaP `1.4759` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3934` n `146` status `ready` deltaP `2.59` edge `0.0474` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6193` n `146` status `ready` deltaP `0.6675` edge `0.0015` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.1886` n `146` status `ready` deltaP `5.6133` edge `-0.005` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.2063` n `146` status `ready` deltaP `-4.5728` edge `-0.0097` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.208` n `146` status `ready` deltaP `-1.7005` edge `-0.0083` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6187` n `146` status `ready` deltaP `5.8819` edge `-0.0018` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0845` n `146` status `ready` deltaP `3.8956` edge `0.0573` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0967` n `146` status `ready` deltaP `0.6365` edge `-0.0267` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.2567` n `146` status `ready` deltaP `14.6165` edge `0.0851` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9221` n `146` status `ready` deltaP `-9.045` edge `0.0163` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0807` n `146` status `ready` deltaP `-4.1147` edge `0.1208` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3038` n `146` status `ready` deltaP `-3.6466` edge `-0.0358` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4417` n `146` status `ready` deltaP `-5.1265` edge `-0.0567` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5525` n `146` status `ready` deltaP `-6.025` edge `-0.0263` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7272` n `146` status `ready` deltaP `-11.5284` edge `-0.0566` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9152` n `146` status `ready` deltaP `0.4823` edge `-0.225` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
