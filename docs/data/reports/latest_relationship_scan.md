# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T17:52:39.423165+00:00`
- Price records: `672`
- Market context records: `5271`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.2337` n `151` status `ready` deltaP `29.4047` edge `1.9991` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `8.9807` n `151` status `ready` deltaP `26.6096` edge `0.9314` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.4021` n `166` status `ready` deltaP `16.3238` edge `0.4221` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8598` n `166` status `ready` deltaP `15.1043` edge `0.4502` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.6029` n `151` status `ready` deltaP `19.8181` edge `0.731` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.219` n `166` status `ready` deltaP `15.7049` edge `0.0991` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8141` n `166` status `ready` deltaP `8.9554` edge `0.172` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5567` n `151` status `ready` deltaP `13.0991` edge `0.0486` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4808` n `177` status `ready` deltaP `4.7879` edge `0.1043` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2504` n `151` status `ready` deltaP `21.015` edge `0.0555` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.2405` n `177` status `ready` deltaP `5.4882` edge `0.108` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.0553` n `177` status `ready` deltaP `6.5598` edge `0.0574` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0081` n `177` status `ready` deltaP `5.7292` edge `0.0115` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2916` n `177` status `ready` deltaP `3.5082` edge `0.0115` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.327` n `177` status `ready` deltaP `0.4127` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5863` n `166` status `ready` deltaP `5.6824` edge `0.025` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6883` n `166` status `ready` deltaP `1.8421` edge `0.0024` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4539` n `177` status `ready` deltaP `-3.4067` edge `-0.0075` maxDD `-3.2759`
- `market_context_high->metal_4h` score `-1.5683` n `166` status `ready` deltaP `-1.9082` edge `0.012` maxDD `-9.3609`
- `market_context_high->crypto_alt_24h` score `-1.8107` n `151` status `ready` deltaP `14.0142` edge `0.4423` maxDD `-48.43`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
