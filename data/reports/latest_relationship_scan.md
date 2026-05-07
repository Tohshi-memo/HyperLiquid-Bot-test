# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T18:07:20.732936+00:00`
- Price records: `572`
- Market context records: `670`
- Flow alert records: `1901`
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

- `market_context_high->crypto_major_24h` score `8.7887` n `146` status `ready` deltaP `22.243` edge `0.6175` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5119` n `146` status `ready` deltaP `8.7689` edge `0.489` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2019` n `146` status `ready` deltaP `7.3134` edge `0.0125` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3458` n `147` status `ready` deltaP `1.6464` edge `0.0025` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5353` n `147` status `ready` deltaP `1.4727` edge `0.0069` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5775` n `147` status `ready` deltaP `1.6681` edge `0.0382` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.0676` n `147` status `ready` deltaP `-0.9806` edge `-0.0014` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2349` n `147` status `ready` deltaP `-4.5415` edge `-0.0123` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2754` n `147` status `ready` deltaP `5.1428` edge `-0.0091` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5667` n `147` status `ready` deltaP `6.3668` edge `-0.0007` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6268` n `146` status `ready` deltaP `5.5509` edge `0.0844` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-1.7142` n `146` status `ready` deltaP `16.1624` edge `0.12` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7455` n `146` status `ready` deltaP `2.3873` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.5156` n `146` status `ready` deltaP `-7.7432` edge `0.0415` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.75` n `146` status `ready` deltaP `-1.7793` edge `-0.0021` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.28` n `147` status `ready` deltaP `-4.4852` edge `-0.0475` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5732` n `146` status `ready` deltaP `-5.2462` edge `0.0873` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.1964` n `146` status `ready` deltaP `-10.0389` edge `-0.0223` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.612` n `146` status `ready` deltaP `1.8281` edge `-0.2087` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7203` n `146` status `ready` deltaP `-8.0973` edge `-0.034` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
