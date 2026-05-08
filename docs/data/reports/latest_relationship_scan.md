# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T03:52:12.955168+00:00`
- Price records: `611`
- Market context records: `715`
- Flow alert records: `2021`
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

- `market_context_high->crypto_major_24h` score `11.3244` n `146` status `ready` deltaP `27.509` edge `0.7937` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3994` n `146` status `ready` deltaP `8.053` edge `0.4844` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2767` n `149` status `ready` deltaP `6.2799` edge `0.0098` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2883` n `149` status `ready` deltaP `2.8259` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4415` n `149` status `ready` deltaP `2.5588` edge `0.0436` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6239` n `149` status `ready` deltaP `0.3695` edge `0.0029` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.7176` n `146` status `ready` deltaP `-1.6634` edge `0.1508` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.053` n `149` status `ready` deltaP `17.0244` edge `0.1221` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1586` n `149` status `ready` deltaP `-3.902` edge `-0.0102` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1699` n `149` status `ready` deltaP `-1.6284` edge `-0.0056` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3666` n `149` status `ready` deltaP `4.6029` edge `-0.0131` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.578` n `149` status `ready` deltaP `6.33` edge `-0.0014` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.6963` n `146` status `ready` deltaP `-3.5225` edge `0.1426` maxDD `-10.5047`
- `market_context_high->index_4h` score `-1.7964` n `149` status `ready` deltaP `1.6603` edge `-0.0085` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.962` n `149` status `ready` deltaP `3.7459` edge `0.0685` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7353` n `149` status `ready` deltaP `-1.3854` edge `-0.0035` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3747` n `149` status `ready` deltaP `-4.9943` edge `-0.052` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6951` n `149` status `ready` deltaP `-5.8847` edge `0.0814` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.1828` n `149` status `ready` deltaP `3.5926` edge `-0.1847` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1269` n `146` status `ready` deltaP `-12.9159` edge `-0.054` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
