# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T19:22:19.730800+00:00`
- Price records: `577`
- Market context records: `676`
- Flow alert records: `1916`
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

- `market_context_high->crypto_major_24h` score `9.1441` n `146` status `ready` deltaP `22.9658` edge `0.6423` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.522` n `146` status `ready` deltaP `8.6706` edge `0.4905` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2124` n `147` status `ready` deltaP `7.1569` edge `0.0122` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3072` n `149` status `ready` deltaP `2.3578` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4502` n `149` status `ready` deltaP `2.4204` edge `0.0438` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5771` n `149` status `ready` deltaP `1.0002` edge `0.0047` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1571` n `149` status `ready` deltaP `-1.6042` edge `-0.0047` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3581` n `149` status `ready` deltaP `-5.2556` edge `-0.0178` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4241` n `149` status `ready` deltaP `4.2739` edge `-0.0157` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6914` n `147` status `ready` deltaP `2.5074` edge `-0.0054` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.6956` n `147` status `ready` deltaP `5.4421` edge `0.0794` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6976` n `149` status `ready` deltaP `5.5097` edge `-0.0059` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7446` n `147` status `ready` deltaP `15.9919` edge `0.1186` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.2616` n `146` status `ready` deltaP `-6.9082` edge `0.0571` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.7026` n `147` status `ready` deltaP `-1.6219` edge `0.0008` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3556` n `149` status `ready` deltaP `-5.0411` edge `-0.0501` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6097` n `147` status `ready` deltaP `-5.342` edge `0.0849` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.85` n `146` status `ready` deltaP `-9.1439` edge `0.0006` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.6108` n `147` status `ready` deltaP `1.768` edge `-0.2082` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7765` n `146` status `ready` deltaP `-8.7591` edge `-0.0368` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
