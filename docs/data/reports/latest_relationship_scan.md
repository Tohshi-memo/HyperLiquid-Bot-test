# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T05:52:29.556017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.7257` n `60` status `ready` deltaP `32.848` edge `432.2169` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.9058` n `52` status `ready` deltaP `61.1119` edge `1.2078` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.4887` n `68` status `ready` deltaP `16.0688` edge `0.3433` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `3.2342` n `52` status `ready` deltaP `28.8995` edge `0.2518` maxDD `-9.6623`
- `news_risk_high->index_4h` score `1.5938` n `68` status `ready` deltaP `15.6115` edge `0.0668` maxDD `-0.3783`
- `news_risk_high->equity_1h` score `0.6504` n `68` status `ready` deltaP `9.9419` edge `0.0702` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.6021` n `52` status `ready` deltaP `8.9704` edge `0.1131` maxDD `-5.323`
- `market_context_high->fx_4h` score `0.5977` n `52` status `ready` deltaP `16.5924` edge `0.0188` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.2362` n `52` status `ready` deltaP `11.7551` edge `0.0499` maxDD `-2.506`
- `news_risk_high->fx_4h` score `0.1248` n `68` status `ready` deltaP `12.2938` edge `0.0242` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.0993` n `68` status `ready` deltaP `5.165` edge `0.0259` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.0733` n `68` status `ready` deltaP `6.3315` edge `0.0354` maxDD `-3.1233`
- `market_context_high->commodity_4h` score `0.0248` n `52` status `ready` deltaP `4.6318` edge `0.0585` maxDD `-2.8961`
- `market_context_high->fx_1h` score `0.0076` n `52` status `ready` deltaP `7.4159` edge `0.0018` maxDD `-0.6874`
- `news_risk_high->fx_1h` score `-0.0505` n `68` status `ready` deltaP `3.1173` edge `0.005` maxDD `-0.2475`
- `market_context_high->commodity_1h` score `-0.0827` n `52` status `ready` deltaP `3.4201` edge `0.0207` maxDD `-1.3282`
- `news_risk_high->index_1h` score `-0.0855` n `68` status `ready` deltaP `2.1663` edge `0.0069` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1676` n `68` status `ready` deltaP `2.0166` edge `0.0054` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2895` n `68` status `ready` deltaP `1.3209` edge `0.0261` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.5684` n `52` status `ready` deltaP `-3.3971` edge `0.0125` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
