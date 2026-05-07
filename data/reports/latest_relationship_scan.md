# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T13:07:21.703752+00:00`
- Price records: `552`
- Market context records: `648`
- Flow alert records: `1838`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `7.2463` n `146` status `ready` deltaP `19.1931` edge `0.5093` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.042` n `146` status `ready` deltaP `8.7449` edge `0.45` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1732` n `146` status `ready` deltaP `7.6553` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3485` n `146` status `ready` deltaP `1.5184` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.3937` n `146` status `ready` deltaP `2.5408` edge `0.0477` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6692` n `146` status `ready` deltaP `0.1133` edge `-0.0012` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1958` n `146` status `ready` deltaP `-4.517` edge `-0.0092` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.267` n `146` status `ready` deltaP `-2.0926` edge `-0.0106` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2829` n `146` status `ready` deltaP `5.2595` edge `-0.0105` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.7299` n `146` status `ready` deltaP `5.3919` edge `-0.0078` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1037` n `146` status `ready` deltaP `3.8208` edge `0.0562` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1956` n `146` status `ready` deltaP `0.0309` edge `-0.0309` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3553` n `146` status `ready` deltaP `14.2685` edge `0.0792` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9173` n `146` status `ready` deltaP `-8.8344` edge `0.0153` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.1816` n `146` status `ready` deltaP `-4.4752` edge `0.1148` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.4155` n `146` status `ready` deltaP `-4.2924` edge `-0.0408` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4945` n `146` status `ready` deltaP `-5.472` edge `-0.0588` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4978` n `146` status `ready` deltaP `-5.3037` edge `-0.0241` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6424` n `146` status `ready` deltaP `-11.3832` edge `-0.0505` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8775` n `146` status `ready` deltaP `0.6389` edge `-0.2229` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
