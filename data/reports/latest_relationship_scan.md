# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T13:52:28.749564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `risk_on_high->crypto_alt_24h` score `16.3676` n `62` status `ready` deltaP `39.6506` edge `1.2989` maxDD `-12.9414`
- `risk_on_and_context->crypto_alt_24h` score `16.3676` n `62` status `ready` deltaP `39.6506` edge `1.2989` maxDD `-12.9414`
- `risk_on_high->unknown_4h` score `8.1348` n `107` status `ready` deltaP `25.4032` edge `0.5702` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1348` n `107` status `ready` deltaP `25.4032` edge `0.5702` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5888` n `159` status `ready` deltaP `22.0998` edge `0.4711` maxDD `-2.5493`
- `risk_on_high->crypto_major_24h` score `3.7388` n `62` status `ready` deltaP `24.6639` edge `0.644` maxDD `-21.661`
- `risk_on_and_context->crypto_major_24h` score `3.7388` n `62` status `ready` deltaP `24.6639` edge `0.644` maxDD `-21.661`
- `market_context_high->metal_24h` score `3.7375` n `104` status `ready` deltaP `30.9829` edge `0.2146` maxDD `-3.1087`
- `market_context_high->crypto_alt_24h` score `3.6034` n `104` status `ready` deltaP `19.5513` edge `0.7506` maxDD `-27.517`
- `risk_on_high->fx_24h` score `3.4036` n `62` status `ready` deltaP `64.0569` edge `0.0479` maxDD `-0.7533`
- `risk_on_and_context->fx_24h` score `3.4036` n `62` status `ready` deltaP `64.0569` edge `0.0479` maxDD `-0.7533`
- `market_context_high->crypto_major_24h` score `2.6061` n `104` status `ready` deltaP `19.391` edge `0.4354` maxDD `-22.7997`
- `risk_on_high->unknown_1h` score `2.443` n `107` status `ready` deltaP `6.8149` edge `0.2158` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.443` n `107` status `ready` deltaP `6.8149` edge `0.2158` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2204` n `159` status `ready` deltaP `6.1566` edge `0.207` maxDD `-2.041`
- `risk_on_high->metal_24h` score `1.5997` n `62` status `ready` deltaP `31.1379` edge `0.1018` maxDD `-3.0107`
- `risk_on_and_context->metal_24h` score `1.5997` n `62` status `ready` deltaP `31.1379` edge `0.1018` maxDD `-3.0107`
- `news_risk_high->unknown_1h` score `1.5395` n `61` status `ready` deltaP `3.9192` edge `0.1368` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.0159` n `104` status `ready` deltaP `36.8857` edge `0.0302` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.6846` n `62` status `ready` deltaP `8.4397` edge `0.1303` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
