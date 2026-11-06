# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T08:07:30.075883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4097`

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

- `news_risk_high->crypto_alt_4h` score `-0.084` n `138` status `ready` deltaP `7.3612` edge `0.2038` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.418` n `138` status `ready` deltaP `3.7186` edge `0.0444` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.6742` n `138` status `ready` deltaP `-2.1674` edge `-0.0019` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7995` n `138` status `ready` deltaP `1.868` edge `0.0009` maxDD `-1.3981`
- `news_risk_high->index_4h` score `-1.2621` n `138` status `ready` deltaP `3.3161` edge `0.0086` maxDD `-3.7341`
- `news_risk_high->metal_1h` score `-1.3277` n `138` status `ready` deltaP `-6.0488` edge `-0.0147` maxDD `-2.5487`
- `news_risk_high->fx_4h` score `-1.5276` n `138` status `ready` deltaP `-8.7288` edge `-0.0125` maxDD `-1.6794`
- `news_risk_high->index_24h` score `-1.7657` n `138` status `ready` deltaP `-9.9393` edge `0.0817` maxDD `-6.6786`
- `news_risk_high->crypto_major_1h` score `-2.0264` n `138` status `ready` deltaP `-4.6299` edge `-0.007` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-2.4211` n `138` status `ready` deltaP `-23.3238` edge `-0.0245` maxDD `-1.7661`
- `news_risk_high->commodity_1h` score `-2.6884` n `138` status `ready` deltaP `-12.4924` edge `-0.0041` maxDD `-3.2657`
- `news_risk_high->crypto_major_4h` score `-3.2546` n `138` status `ready` deltaP `-6.6786` edge `0.0335` maxDD `-15.4824`
- `news_risk_high->equity_1h` score `-3.3093` n `138` status `ready` deltaP `-4.875` edge `0.0057` maxDD `-14.9182`
- `news_risk_high->commodity_4h` score `-4.454` n `138` status `ready` deltaP `-19.0704` edge `-0.0086` maxDD `-9.5011`
- `news_risk_high->equity_24h` score `-4.8053` n `138` status `ready` deltaP `13.194` edge `0.7244` maxDD `-86.0244`
- `news_risk_high->metal_4h` score `-4.9781` n `138` status `ready` deltaP `-10.9823` edge `-0.0685` maxDD `-8.1837`
- `news_risk_high->metal_24h` score `-7.5747` n `138` status `ready` deltaP `-13.9586` edge `-0.2699` maxDD `-12.1284`
- `news_risk_high->equity_4h` score `-7.7995` n `138` status `ready` deltaP `3.7734` edge `0.0374` maxDD `-45.0012`
- `news_risk_high->commodity_24h` score `-10.874` n `138` status `ready` deltaP `-20.8791` edge `0.0591` maxDD `-43.7525`
- `news_risk_high->crypto_alt_24h` score `-12.293` n `138` status `ready` deltaP `6.1858` edge `0.0822` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
