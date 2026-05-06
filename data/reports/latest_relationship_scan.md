# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T14:52:20.892235+00:00`
- Price records: `463`
- Market context records: `553`
- Flow alert records: `1562`
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

- `market_context_high->crypto_alt_24h` score `4.9675` n `139` status `ready` deltaP `7.7045` edge `0.3674` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0258` n `139` status `ready` deltaP `10.1169` edge `0.2181` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0386` n `146` status `ready` deltaP `10.5894` edge `0.0215` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3053` n `146` status `ready` deltaP `2.124` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5417` n `146` status `ready` deltaP `2.0111` edge `0.0389` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5785` n `146` status `ready` deltaP `1.6182` edge `0.0004` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.074` n `146` status `ready` deltaP `-0.5796` edge `-0.0046` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1143` n `146` status `ready` deltaP `-3.4082` edge `-0.0098` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2673` n `146` status `ready` deltaP `4.6886` edge `-0.0054` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8089` n `139` status `ready` deltaP `-5.87` edge `0.0879` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-1.9814` n `146` status `ready` deltaP `3.5977` edge `-0.0168` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.1681` n `146` status `ready` deltaP `0.7344` edge `-0.0333` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.6282` n `146` status `ready` deltaP `1.2243` edge `0.0298` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.24` n `146` status `ready` deltaP `-3.3288` edge `-0.0326` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3573` n `146` status `ready` deltaP `-5.2124` edge `-0.0491` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.3797` n `146` status `ready` deltaP `-5.4825` edge `0.105` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.6161` n `146` status `ready` deltaP `0.6114` edge `-0.1176` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-3.7301` n `139` status `ready` deltaP `-10.24` edge `0.0179` maxDD `-10.5047`
- `market_context_high->crypto_major_4h` score `-3.7647` n `146` status `ready` deltaP `8.6068` edge `-0.0005` maxDD `-22.648`
- `market_context_high->fx_24h` score `-4.3309` n `139` status `ready` deltaP `-5.4985` edge `-0.0413` maxDD `-17.8497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
