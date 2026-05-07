# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T17:37:12.617110+00:00`
- Price records: `570`
- Market context records: `668`
- Flow alert records: `1895`
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

- `market_context_high->crypto_major_24h` score `8.65` n `146` status `ready` deltaP `21.9496` edge `0.6079` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4911` n `146` status `ready` deltaP `8.8088` edge `0.487` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1911` n `146` status `ready` deltaP `7.4919` edge `0.0127` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.356` n `147` status `ready` deltaP `1.4489` edge `0.0025` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5403` n `147` status `ready` deltaP `1.438` edge `0.0065` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5802` n `147` status `ready` deltaP `1.6801` edge `0.0379` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.0745` n `147` status `ready` deltaP `-1.0216` edge `-0.0017` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2218` n `147` status `ready` deltaP `-4.3773` edge `-0.0123` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2494` n `147` status `ready` deltaP `5.2884` edge `-0.0079` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5603` n `147` status `ready` deltaP `6.3568` edge `-0.0001` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6304` n `146` status `ready` deltaP `5.4918` edge `0.0845` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.7531` n `146` status `ready` deltaP `15.9611` edge `0.1181` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7901` n `146` status `ready` deltaP `2.1594` edge `-0.0113` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.6051` n `146` status `ready` deltaP `-8.0822` edge `0.0363` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.8259` n `146` status `ready` deltaP `-2.0224` edge `-0.0068` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3068` n `147` status `ready` deltaP `-4.6861` edge `-0.0484` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.4704` n `146` status `ready` deltaP `-5.0261` edge `0.0944` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.3155` n `146` status `ready` deltaP `-10.4022` edge `-0.0298` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6538` n `146` status `ready` deltaP `1.6047` edge `-0.2107` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.6977` n `146` status `ready` deltaP `-7.8286` edge `-0.0329` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
