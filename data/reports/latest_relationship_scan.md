# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T15:22:23.494072+00:00`
- Price records: `561`
- Market context records: `658`
- Flow alert records: `1866`
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

- `market_context_high->crypto_major_24h` score `7.9023` n `146` status `ready` deltaP `20.598` edge `0.5546` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.1946` n `146` status `ready` deltaP `8.7775` edge `0.4625` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1391` n `146` status `ready` deltaP `8.3116` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.324` n `147` status `ready` deltaP `1.9892` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3715` n `147` status `ready` deltaP `2.5488` edge `0.0495` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6251` n `147` status `ready` deltaP `0.6458` edge `0.0009` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.203` n `147` status `ready` deltaP `5.5973` edge `-0.0061` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.2045` n `147` status `ready` deltaP `-4.5213` edge `-0.0099` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2759` n `147` status `ready` deltaP `-2.0236` edge `-0.0118` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6226` n `147` status `ready` deltaP `5.8623` edge `-0.002` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9617` n `146` status `ready` deltaP `4.3949` edge `0.0642` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0286` n `146` status `ready` deltaP `1.1129` edge `-0.0242` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.121` n `146` status `ready` deltaP `15.0371` edge `0.0936` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9042` n `146` status `ready` deltaP `-9.2102` edge `0.0189` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0608` n `146` status `ready` deltaP `-4.0159` edge `0.1218` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.2139` n `146` status `ready` deltaP `-3.1385` edge `-0.0317` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4946` n `147` status `ready` deltaP `-5.6082` edge `-0.0579` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5952` n `146` status `ready` deltaP `-6.5908` edge `-0.028` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7255` n `146` status `ready` deltaP `-11.6423` edge `-0.0557` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8229` n `146` status `ready` deltaP `0.9463` edge `-0.2204` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
