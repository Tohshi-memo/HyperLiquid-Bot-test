# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T06:07:28.735481+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.7034` n `60` status `ready` deltaP `32.6747` edge `432.2162` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.7377` n `51` status `ready` deltaP `60.9611` edge `1.1948` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.4791` n `68` status `ready` deltaP `16.0688` edge `0.3425` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `3.6643` n `51` status `ready` deltaP `30.3701` edge `0.2674` maxDD `-9.1609`
- `news_risk_high->index_4h` score `1.5902` n `68` status `ready` deltaP `15.6115` edge `0.0665` maxDD `-0.3783`
- `market_context_high->fx_4h` score `0.696` n `51` status `ready` deltaP `17.6859` edge `0.0197` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.6492` n `68` status `ready` deltaP `9.9419` edge `0.0701` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.5298` n `51` status `ready` deltaP `8.1032` edge `0.1096` maxDD `-5.323`
- `market_context_high->fx_24h` score `0.1664` n `51` status `ready` deltaP `10.684` edge `0.0481` maxDD `-2.506`
- `news_risk_high->fx_4h` score `0.1248` n `68` status `ready` deltaP `12.2938` edge `0.0242` maxDD `-0.6604`
- `market_context_high->commodity_4h` score `0.106` n `51` status `ready` deltaP `5.5745` edge `0.0615` maxDD `-2.8061`
- `news_risk_high->metal_4h` score `0.0985` n `68` status `ready` deltaP `5.165` edge `0.0258` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.064` n `68` status `ready` deltaP `6.1818` edge `0.0352` maxDD `-3.1233`
- `market_context_high->fx_1h` score `-0.0304` n `51` status `ready` deltaP `6.6984` edge `0.0017` maxDD `-0.6874`
- `news_risk_high->fx_1h` score `-0.0427` n `68` status `ready` deltaP `3.267` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0863` n `68` status `ready` deltaP `2.1663` edge `0.0068` maxDD `-0.5845`
- `market_context_high->commodity_1h` score `-0.1263` n `51` status `ready` deltaP `2.6271` edge `0.0204` maxDD `-1.3282`
- `news_risk_high->metal_1h` score `-0.1598` n `68` status `ready` deltaP `2.1663` edge `0.0054` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2911` n `68` status `ready` deltaP `1.3209` edge `0.0259` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.5307` n `51` status `ready` deltaP `-2.6418` edge `0.0123` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
