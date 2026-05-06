# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T16:52:24.955742+00:00`
- Price records: `471`
- Market context records: `562`
- Flow alert records: `1587`
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

- `market_context_high->crypto_alt_24h` score `4.8514` n `141` status `ready` deltaP `7.5575` edge `0.3587` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0244` n `141` status `ready` deltaP `9.8894` edge `0.2195` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0214` n `146` status `ready` deltaP `9.6604` edge `0.02` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3379` n `146` status `ready` deltaP `1.5577` edge `0.0041` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5425` n `146` status `ready` deltaP `1.9409` edge `0.0393` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6186` n `146` status `ready` deltaP `1.1317` edge `-0.0015` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1799` n `146` status `ready` deltaP `-1.2441` edge `-0.009` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2415` n `146` status `ready` deltaP `-4.2181` edge `-0.015` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3666` n `146` status `ready` deltaP `4.2123` edge `-0.0105` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8807` n `141` status `ready` deltaP `-5.8974` edge `0.0821` maxDD `-5.9609`
- `market_context_high->index_4h` score `-2.0057` n `146` status `ready` deltaP `1.6539` edge `-0.0259` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-2.0195` n `146` status `ready` deltaP `3.2721` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.2719` n `146` status `ready` deltaP `2.4673` edge `0.0512` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0143` n `146` status `ready` deltaP `-2.3373` edge `-0.0204` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.288` n `146` status `ready` deltaP `9.72` edge `0.0318` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2978` n `146` status `ready` deltaP `-4.6479` edge `-0.0479` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5786` n `146` status `ready` deltaP `-6.1082` edge `0.0926` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7819` n `141` status `ready` deltaP `-10.168` edge `0.0131` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.3826` n `141` status `ready` deltaP `-5.2532` edge `-0.0388` maxDD `-18.7108`
- `market_context_high->unknown_4h` score `-5.3492` n `146` status `ready` deltaP `-0.0377` edge `-0.2577` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
