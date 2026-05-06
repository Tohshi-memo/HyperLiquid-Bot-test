# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T20:22:16.842537+00:00`
- Price records: `485`
- Market context records: `577`
- Flow alert records: `1631`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.7419` n `146` status `ready` deltaP `7.2843` edge `0.3514` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `2.942` n `146` status `ready` deltaP `9.5186` edge `0.2151` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.045` n `146` status `ready` deltaP `10.9074` edge `0.0202` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2831` n `146` status `ready` deltaP `2.5516` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5447` n `146` status `ready` deltaP `2.0333` edge `0.0385` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7025` n `146` status `ready` deltaP `-0.0474` edge `-0.0044` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1601` n `146` status `ready` deltaP `-4.1153` edge `-0.0089` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2867` n `146` status `ready` deltaP `4.7162` edge `-0.0072` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3299` n `146` status `ready` deltaP `-2.3535` edge `-0.0141` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.9475` n `146` status `ready` deltaP `3.8717` edge `-0.0158` maxDD `-11.4508`
- `market_context_high->index_24h` score `-1.9513` n `146` status `ready` deltaP `-5.7445` edge `0.0752` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1835` n `146` status `ready` deltaP `3.0479` edge `0.0547` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2078` n `146` status `ready` deltaP `0.5524` edge `-0.0354` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-3.0272` n `146` status `ready` deltaP `11.1502` edge `0.044` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.3148` n `146` status `ready` deltaP `-3.3186` edge `-0.0389` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.327` n `146` status `ready` deltaP `-4.8487` edge `-0.049` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5258` n `146` status `ready` deltaP `-5.5383` edge `0.0932` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.8599` n `146` status `ready` deltaP `-9.8523` edge `0.0045` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.5756` n `146` status `ready` deltaP `-4.9991` edge `-0.0361` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.1333` n `146` status `ready` deltaP `1.012` edge `-0.2467` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
