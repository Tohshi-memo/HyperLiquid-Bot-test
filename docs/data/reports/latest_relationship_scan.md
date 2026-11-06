# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T11:07:40.686841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4236`

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

- `news_risk_high->crypto_alt_4h` score `-0.4922` n `126` status `ready` deltaP `4.641` edge `0.1696` maxDD `-14.0916`
- `news_risk_high->index_1h` score `-0.5755` n `126` status `ready` deltaP `3.9374` edge `0.0013` maxDD `-1.0403`
- `news_risk_high->index_4h` score `-0.5776` n `126` status `ready` deltaP `6.3178` edge `0.0118` maxDD `-2.5714`
- `news_risk_high->crypto_alt_1h` score `-0.7456` n `126` status `ready` deltaP `0.3136` edge `0.0251` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7587` n `126` status `ready` deltaP `-4.3865` edge `-0.0027` maxDD `-0.5597`
- `news_risk_high->index_24h` score `-0.9618` n `126` status `ready` deltaP `-6.0746` edge `0.109` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `-0.9831` n `126` status `ready` deltaP `-4.8151` edge `-0.0068` maxDD `-0.9709`
- `news_risk_high->equity_24h` score `-1.3593` n `126` status `ready` deltaP `18.784` edge `0.9243` maxDD `-86.0244`
- `news_risk_high->fx_24h` score `-1.5966` n `126` status `ready` deltaP `-18.4928` edge `-0.013` maxDD `-0.8055`
- `news_risk_high->metal_1h` score `-1.6469` n `126` status `ready` deltaP `-5.451` edge `-0.0161` maxDD `-2.1176`
- `news_risk_high->equity_1h` score `-1.7902` n `126` status `ready` deltaP `-3.2198` edge `0.0079` maxDD `-12.276`
- `news_risk_high->crypto_major_1h` score `-2.127` n `126` status `ready` deltaP `-4.9877` edge `-0.013` maxDD `-6.1465`
- `news_risk_high->crypto_major_4h` score `-2.3812` n `126` status `ready` deltaP `-4.6143` edge `0.043` maxDD `-11.5202`
- `news_risk_high->commodity_1h` score `-2.9494` n `126` status `ready` deltaP `-15.2291` edge `-0.0076` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.6396` n `126` status `ready` deltaP `-8.8778` edge `-0.0586` maxDD `-5.1743`
- `news_risk_high->commodity_4h` score `-4.5522` n `126` status `ready` deltaP `-20.0881` edge `-0.01` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-4.9565` n `126` status `ready` deltaP `6.7751` edge `0.0649` maxDD `-33.8489`
- `news_risk_high->metal_24h` score `-5.8356` n `126` status `ready` deltaP `-8.7136` edge `-0.2386` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.4346` n `126` status `ready` deltaP `-22.4721` edge `0.0273` maxDD `-41.4294`
- `news_risk_high->crypto_major_24h` score `-11.3141` n `126` status `ready` deltaP `-19.281` edge `0.0618` maxDD `-52.7551`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
