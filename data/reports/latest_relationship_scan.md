# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T22:07:14.217078+00:00`
- Price records: `492`
- Market context records: `585`
- Flow alert records: `1653`
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

- `market_context_high->crypto_alt_24h` score `4.6683` n `146` status `ready` deltaP `7.1434` edge `0.3462` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.1541` n `146` status `ready` deltaP `9.7101` edge `0.2315` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0839` n `146` status `ready` deltaP `11.609` edge `0.0205` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2745` n `146` status `ready` deltaP `2.7171` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6208` n `146` status `ready` deltaP `1.4576` edge `0.036` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6549` n `146` status `ready` deltaP `0.6283` edge `-0.0028` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1899` n `146` status `ready` deltaP `-4.5783` edge `-0.0083` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2155` n `146` status `ready` deltaP `-1.6444` edge `-0.0093` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3162` n `146` status `ready` deltaP `4.7525` edge `-0.0099` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.9255` n `146` status `ready` deltaP `4.0562` edge `-0.0152` maxDD `-11.4508`
- `market_context_high->index_24h` score `-2.1632` n `146` status `ready` deltaP `-6.1434` edge `0.0602` maxDD `-5.9609`
- `market_context_high->crypto_alt_4h` score `-2.1661` n `146` status `ready` deltaP `3.0102` edge `0.0564` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2763` n `146` status `ready` deltaP `0.0261` edge `-0.0376` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.9689` n `146` status `ready` deltaP `11.4136` edge `0.0471` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2853` n `146` status `ready` deltaP `-4.4324` edge `-0.0483` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.3751` n `146` status `ready` deltaP `-3.7874` edge `-0.0408` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.6355` n `146` status `ready` deltaP `-6.2195` edge `0.0886` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-4.175` n `146` status `ready` deltaP `-10.1167` edge `-0.02` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.481` n `146` status `ready` deltaP `-4.3962` edge `-0.028` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-5.0643` n `146` status `ready` deltaP `1.0936` edge `-0.2415` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
