# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T18:37:15.366435+00:00`
- Price records: `574`
- Market context records: `672`
- Flow alert records: `1907`
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

- `market_context_high->crypto_major_24h` score `8.9188` n `146` status `ready` deltaP `22.5339` edge `0.6264` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5027` n `146` status `ready` deltaP `8.7293` edge `0.4885` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1964` n `147` status `ready` deltaP `7.4204` edge `0.0125` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3348` n `147` status `ready` deltaP `1.8425` edge `0.0026` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5328` n `147` status `ready` deltaP `1.5072` edge `0.007` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5524` n `147` status `ready` deltaP `1.8329` edge `0.0392` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.0785` n `147` status `ready` deltaP `-1.1166` edge `-0.0014` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.254` n `147` status `ready` deltaP `-4.7046` edge `-0.0128` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.323` n `147` status `ready` deltaP `4.9982` edge `-0.0121` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5967` n `147` status `ready` deltaP `6.2012` edge `-0.0021` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.638` n `147` status `ready` deltaP `5.6213` edge `0.083` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.7832` n `147` status `ready` deltaP `2.171` edge `-0.0108` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-1.7853` n `147` status `ready` deltaP `15.6938` edge `0.1172` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.4191` n `146` status `ready` deltaP `-7.4071` edge `0.0473` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.8393` n `147` status `ready` deltaP `-1.9806` edge `-0.0082` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2921` n `147` status `ready` deltaP `-4.6365` edge `-0.0475` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.4769` n `147` status `ready` deltaP `-5.0173` edge `0.0938` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.0656` n `146` status `ready` deltaP `-9.6786` edge `-0.0138` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6373` n `147` status `ready` deltaP `1.6166` edge `-0.2094` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7427` n `146` status `ready` deltaP `-8.3637` edge `-0.0351` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
