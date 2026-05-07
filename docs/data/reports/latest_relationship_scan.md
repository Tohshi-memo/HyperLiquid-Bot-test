# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T16:07:20.053924+00:00`
- Price records: `564`
- Market context records: `661`
- Flow alert records: `1876`
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

- `market_context_high->crypto_major_24h` score `8.156` n `146` status `ready` deltaP `21.0543` edge `0.5727` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3184` n `146` status `ready` deltaP `8.9305` edge `0.4718` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1558` n `146` status `ready` deltaP `8.0354` edge `0.0136` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.339` n `147` status `ready` deltaP `1.7472` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4381` n `147` status `ready` deltaP `2.2561` edge `0.0459` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6074` n `147` status `ready` deltaP `0.7928` edge `0.0022` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1624` n `147` status `ready` deltaP `-4.2347` edge `-0.0083` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1791` n `147` status `ready` deltaP `5.7313` edge `-0.005` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2093` n `147` status `ready` deltaP `-1.686` edge `-0.0085` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.5973` n `147` status `ready` deltaP `5.9694` edge `-0.0006` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.8542` n `146` status `ready` deltaP `4.7645` edge `0.0707` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.9656` n `146` status `ready` deltaP `1.4656` edge `-0.0213` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.0025` n `146` status `ready` deltaP `15.3485` edge `0.1014` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.8523` n `146` status `ready` deltaP `-9.1167` edge `0.0226` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1179` n `146` status `ready` deltaP `-2.7624` edge `-0.0262` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.1396` n `146` status `ready` deltaP `-4.3563` edge `0.1175` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4193` n `147` status `ready` deltaP `-5.2976` edge `-0.0537` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.6294` n `146` status `ready` deltaP `-7.0088` edge `-0.0296` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6574` n `146` status `ready` deltaP `-11.5109` edge `-0.0509` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.7498` n `146` status `ready` deltaP `1.2898` edge `-0.2166` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
