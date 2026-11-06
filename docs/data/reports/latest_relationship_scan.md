# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T12:07:26.089416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3931`

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

- `news_risk_high->equity_24h` score `-0.307` n `122` status `ready` deltaP `20.8917` edge `0.98` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.3652` n `122` status `ready` deltaP `7.5294` edge `0.0115` maxDD `-2.3482`
- `news_risk_high->index_1h` score `-0.4453` n `122` status `ready` deltaP `5.3033` edge `0.0017` maxDD `-0.9328`
- `news_risk_high->crypto_alt_4h` score `-0.4483` n `122` status `ready` deltaP `5.1854` edge `0.1716` maxDD `-14.0916`
- `news_risk_high->fx_1h` score `-0.5538` n `122` status `ready` deltaP `-3.3719` edge `-0.0019` maxDD `-0.3963`
- `news_risk_high->index_24h` score `-0.7579` n `122` status `ready` deltaP `-4.6174` edge `0.1171` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.7886` n `122` status `ready` deltaP `-0.0638` edge `0.0221` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.8535` n `122` status `ready` deltaP `-3.7335` edge `-0.0036` maxDD `-0.4745`
- `news_risk_high->metal_1h` score `-1.3126` n `122` status `ready` deltaP `-4.6186` edge `-0.0147` maxDD `-1.7784`
- `news_risk_high->fx_24h` score `-1.472` n `122` status `ready` deltaP `-17.3635` edge `-0.0089` maxDD `-0.4586`
- `news_risk_high->equity_1h` score `-1.5987` n `122` status `ready` deltaP `-2.3093` edge `0.0112` maxDD `-11.0612`
- `news_risk_high->crypto_major_1h` score `-1.8085` n `122` status `ready` deltaP `-4.9033` edge `-0.012` maxDD `-5.1484`
- `news_risk_high->crypto_major_4h` score `-1.8218` n `122` status `ready` deltaP `-3.8709` edge `0.0551` maxDD `-9.1553`
- `news_risk_high->commodity_1h` score `-2.8985` n `122` status `ready` deltaP `-14.5332` edge `-0.008` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.1221` n `122` status `ready` deltaP `-8.0043` edge `-0.053` maxDD `-3.9716`
- `news_risk_high->metal_24h` score `-3.6076` n `122` status `ready` deltaP `-6.736` edge `-0.228` maxDD `-8.5019`
- `news_risk_high->equity_4h` score `-3.8522` n `122` status `ready` deltaP `7.9868` edge `0.0766` maxDD `-29.4026`
- `news_risk_high->commodity_4h` score `-4.5909` n `122` status `ready` deltaP `-20.5118` edge `-0.0104` maxDD `-9.5011`
- `news_risk_high->commodity_24h` score `-10.2616` n `122` status `ready` deltaP `-22.982` edge `0.0186` maxDD `-40.3083`
- `news_risk_high->crypto_major_24h` score `-10.3799` n `122` status `ready` deltaP `-18.3703` edge `0.1078` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
