# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T00:37:17.361425+00:00`
- Price records: `598`
- Market context records: `701`
- Flow alert records: `1981`
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

- `market_context_high->crypto_major_24h` score `10.6224` n `146` status `ready` deltaP `25.8445` edge `0.7463` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5879` n `146` status `ready` deltaP `8.2792` edge `0.4986` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2004` n `149` status `ready` deltaP `7.3721` edge `0.0123` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.268` n `149` status `ready` deltaP `3.1418` edge `0.0025` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5051` n `149` status `ready` deltaP `2.2136` edge `0.0406` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6079` n `149` status `ready` deltaP `0.5722` edge `0.0036` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1611` n `149` status `ready` deltaP `-1.6244` edge `-0.0049` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1736` n `149` status `ready` deltaP `15.8306` edge `0.1146` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1923` n `149` status `ready` deltaP `-4.2032` edge `-0.011` maxDD `-2.1602`
- `market_context_high->index_24h` score `-1.2337` n `146` status `ready` deltaP `-3.5842` edge `0.1206` maxDD `-5.9609`
- `market_context_high->crypto_alt_1h` score `-1.4353` n `149` status `ready` deltaP `4.1646` edge `-0.0159` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6466` n `149` status `ready` deltaP `2.5127` edge `-0.0017` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6708` n `149` status `ready` deltaP `5.6957` edge `-0.0049` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9709` n `149` status `ready` deltaP `4.1306` edge `0.0652` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.3866` n `146` status `ready` deltaP `-5.5812` edge `0.0988` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5466` n `149` status `ready` deltaP `-0.6015` edge `0.007` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.34` n `149` status `ready` deltaP `-5.0561` edge `-0.0487` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8807` n `149` status `ready` deltaP `-6.644` edge `0.071` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.3403` n `149` status `ready` deltaP `2.7941` edge `-0.1925` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9954` n `146` status `ready` deltaP `-11.3935` edge `-0.0473` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
