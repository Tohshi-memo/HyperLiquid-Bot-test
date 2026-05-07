# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T04:37:15.883201+00:00`
- Price records: `518`
- Market context records: `613`
- Flow alert records: `1734`
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

- `market_context_high->crypto_alt_24h` score `5.1531` n `146` status `ready` deltaP `7.6089` edge `0.3835` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.6257` n `146` status `ready` deltaP `13.3448` edge `0.3299` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0505` n `146` status `ready` deltaP `9.6248` edge `0.0165` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3348` n `146` status `ready` deltaP `1.7513` edge `0.0032` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.646` n `146` status `ready` deltaP `1.0825` edge `0.0364` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6777` n `146` status `ready` deltaP `0.1746` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.022` n `146` status `ready` deltaP `-3.2141` edge `-0.0034` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0518` n `146` status `ready` deltaP `6.2124` edge `0.0024` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2474` n `146` status `ready` deltaP `-1.9823` edge `-0.0097` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.4842` n `146` status `ready` deltaP `5.3839` edge `0.0974` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6299` n `146` status `ready` deltaP `6.0871` edge `-0.0041` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2442` n `146` status `ready` deltaP `14.5473` edge `0.0866` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.2715` n `146` status `ready` deltaP `-0.3933` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.6948` n `146` status `ready` deltaP `-7.508` edge `0.025` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1744` n `146` status `ready` deltaP `-3.0038` edge `-0.0293` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2671` n `146` status `ready` deltaP `-4.2642` edge `-0.0479` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7145` n `146` status `ready` deltaP `-6.5165` edge `0.084` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.249` n `146` status `ready` deltaP `-2.3334` edge `-0.012` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6931` n `146` status `ready` deltaP `2.344` edge `-0.2189` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.6938` n `146` status `ready` deltaP `-11.0211` edge `-0.0572` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
