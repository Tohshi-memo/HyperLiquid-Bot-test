# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T23:52:23.373213+00:00`
- Price records: `499`
- Market context records: `593`
- Flow alert records: `1676`
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

- `market_context_high->crypto_alt_24h` score `4.577` n `146` status `ready` deltaP `7.0074` edge `0.3395` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.421` n `146` status `ready` deltaP `10.3912` edge `0.2492` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0844` n `146` status `ready` deltaP `11.6639` edge `0.0202` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2995` n `146` status `ready` deltaP `2.2668` edge `0.0043` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6118` n `146` status `ready` deltaP `1.5094` edge `0.0364` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6526` n `146` status `ready` deltaP `0.6738` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1613` n `146` status `ready` deltaP `-4.2203` edge `-0.0083` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2271` n `146` status `ready` deltaP `5.1917` edge `-0.0054` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2635` n `146` status `ready` deltaP `-1.9739` edge `-0.0111` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.8405` n `146` status `ready` deltaP `4.6395` edge `-0.012` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1628` n `146` status `ready` deltaP `2.7667` edge `0.0583` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2503` n `146` status `ready` deltaP `0.1416` edge `-0.0362` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.356` n `146` status `ready` deltaP `-6.5283` edge `0.0467` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.8412` n `146` status `ready` deltaP `12.2905` edge `0.0519` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2991` n `146` status `ready` deltaP `-4.634` edge `-0.0481` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3493` n `146` status `ready` deltaP `-3.825` edge `-0.0384` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7723` n `146` status `ready` deltaP `-7.0895` edge `0.083` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3798` n `146` status `ready` deltaP `-3.8144` edge `-0.0189` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.3886` n `146` status `ready` deltaP `-10.3718` edge `-0.0361` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-5.0933` n `146` status `ready` deltaP `0.5516` edge `-0.2403` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
