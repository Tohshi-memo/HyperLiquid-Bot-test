# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T17:52:17.220870+00:00`
- Price records: `571`
- Market context records: `669`
- Flow alert records: `1898`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `848`

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

- `market_context_high->crypto_major_24h` score `8.7242` n `146` status `ready` deltaP `22.0966` edge `0.6131` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5111` n `146` status `ready` deltaP `8.7888` edge `0.4888` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1965` n `146` status `ready` deltaP `7.4025` edge `0.0126` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3509` n `147` status `ready` deltaP `1.5479` edge `0.0025` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5301` n `147` status `ready` deltaP `1.5442` edge `0.0071` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5926` n `147` status `ready` deltaP `1.5853` edge `0.0375` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.0562` n `147` status `ready` deltaP `-0.9123` edge `-0.0009` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2284` n `147` status `ready` deltaP `-4.4596` edge `-0.0123` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2564` n `147` status `ready` deltaP `5.2154` edge `-0.008` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5528` n `147` status `ready` deltaP `6.45` edge `-0.0001` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6148` n `146` status `ready` deltaP `5.6115` edge `0.085` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.7282` n `146` status `ready` deltaP `16.0619` edge `0.1195` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7641` n `146` status `ready` deltaP `2.2736` edge `-0.0099` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.5567` n `146` status `ready` deltaP `-7.9123` edge `0.0392` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.7849` n `146` status `ready` deltaP `-1.9006` edge `-0.0042` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2916` n `147` status `ready` deltaP `-4.5855` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5236` n `146` status `ready` deltaP `-5.1363` edge `0.0907` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.2529` n `146` status `ready` deltaP `-10.2201` edge `-0.0258` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6317` n `146` status `ready` deltaP `1.7166` edge `-0.2096` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7094` n `146` status `ready` deltaP `-7.9633` edge `-0.0335` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
