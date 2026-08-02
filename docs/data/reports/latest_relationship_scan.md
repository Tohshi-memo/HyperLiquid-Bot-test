# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T19:52:26.282483+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4404.1014` n `68` status `ready` deltaP `24.4995` edge `366.8872` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.459` n `40` status `ready` deltaP `55.2778` edge `1.0428` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0634` n `40` status `ready` deltaP `51.3194` edge `0.5926` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.708` n `68` status `ready` deltaP `17.7456` edge `0.3504` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6935` n `68` status `ready` deltaP `16.6786` edge `0.068` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0958` n `40` status `ready` deltaP `14.2073` edge `0.1304` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7015` n `40` status `ready` deltaP `8.3537` edge `0.1248` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.67` n `40` status `ready` deltaP `12.3952` edge `0.0407` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.6622` n `40` status `ready` deltaP `20.6098` edge `0.0271` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.5845` n `68` status `ready` deltaP `9.1934` edge `0.0697` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.4614` n `40` status `ready` deltaP `14.1467` edge `0.0026` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.333` n `68` status `ready` deltaP `14.5804` edge `0.0263` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1964` n `68` status `ready` deltaP `6.5369` edge `0.0292` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0453` n `68` status `ready` deltaP `5.583` edge `0.0368` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.0505` n `68` status `ready` deltaP `3.1173` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0847` n `68` status `ready` deltaP `2.1663` edge `0.007` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1333` n `68` status `ready` deltaP `2.6154` edge `0.0058` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.242` n `68` status `ready` deltaP `2.0694` edge `0.0272` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4627` n `40` status `ready` deltaP `-0.2994` edge `0.0054` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.607` n `68` status `ready` deltaP `3.8658` edge `-0.0256` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
