# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T14:52:17.320036+00:00`
- Price records: `559`
- Market context records: `655`
- Flow alert records: `1860`
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

- `market_context_high->crypto_major_24h` score `7.7397` n `146` status `ready` deltaP `20.2905` edge `0.5431` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.111` n `146` status `ready` deltaP `8.6024` edge `0.4567` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1391` n `146` status `ready` deltaP `8.312` edge `0.0139` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3411` n `146` status `ready` deltaP `1.6769` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4176` n `146` status `ready` deltaP `2.3917` edge `0.0467` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6292` n `146` status `ready` deltaP `0.5233` edge `0.0012` maxDD `-2.8282`
- `market_context_high->crypto_alt_1h` score `-1.138` n `146` status `ready` deltaP `5.825` edge `-0.0022` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.1715` n `146` status `ready` deltaP `-4.3786` edge `-0.0081` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2079` n `146` status `ready` deltaP `-1.6545` edge `-0.0086` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.5744` n `146` status `ready` deltaP `6.0755` edge `0.0006` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.032` n `146` status `ready` deltaP `4.1462` edge `0.06` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.0632` n `146` status `ready` deltaP `0.8756` edge `-0.0255` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.1942` n `146` status `ready` deltaP `14.8276` edge `0.0889` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9168` n `146` status `ready` deltaP `-9.128` edge `0.0173` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.0453` n `146` status `ready` deltaP `-3.9723` edge `0.1228` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.2678` n `146` status `ready` deltaP `-3.3916` edge `-0.0345` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4634` n `146` status `ready` deltaP `-5.2783` edge `-0.0575` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.5735` n `146` status `ready` deltaP `-6.3092` edge `-0.0271` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.7402` n `146` status `ready` deltaP `-11.5856` edge `-0.0573` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8774` n `146` status `ready` deltaP `0.7152` edge `-0.2234` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
