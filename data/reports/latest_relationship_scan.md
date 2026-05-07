# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T18:52:18.087577+00:00`
- Price records: `575`
- Market context records: `673`
- Flow alert records: `1910`
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

- `market_context_high->crypto_major_24h` score `8.9916` n `146` status `ready` deltaP `22.6785` edge `0.6315` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5072` n `146` status `ready` deltaP `8.7097` edge `0.489` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2017` n `147` status `ready` deltaP `7.3322` edge `0.0124` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3297` n `147` status `ready` deltaP `1.9401` edge `0.0026` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.5257` n `147` status `ready` deltaP `1.6125` edge `0.0072` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.5434` n `147` status `ready` deltaP `1.9148` edge `0.0394` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-1.065` n `147` status `ready` deltaP `-1.0078` edge `-0.001` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2749` n `147` status `ready` deltaP `-4.7857` edge `-0.014` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3383` n `147` status `ready` deltaP `4.9263` edge `-0.0129` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6045` n `147` status `ready` deltaP `6.1189` edge `-0.0022` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.6536` n `147` status `ready` deltaP `5.5614` edge `0.0821` maxDD `-15.2248`
- `market_context_high->index_4h` score `-1.7501` n `147` status `ready` deltaP `2.2836` edge `-0.0088` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-1.7701` n `147` status `ready` deltaP `15.7935` edge `0.1178` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.3661` n `146` status `ready` deltaP `-7.2401` edge `0.0506` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.7877` n `147` status `ready` deltaP `-1.8606` edge `-0.0047` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2781` n `147` status `ready` deltaP `-4.5367` edge `-0.047` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5252` n `147` status `ready` deltaP `-5.1259` edge `0.0905` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.9937` n `146` status `ready` deltaP `-9.4996` edge `-0.009` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6512` n `147` status `ready` deltaP `1.5479` edge `-0.2101` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7543` n `146` status `ready` deltaP `-8.4961` edge `-0.0357` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
