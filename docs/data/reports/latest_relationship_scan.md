# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T05:52:11.497042+00:00`
- Price records: `523`
- Market context records: `619`
- Flow alert records: `1749`
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

- `market_context_high->crypto_alt_24h` score `5.1873` n `146` status `ready` deltaP `7.5118` edge `0.387` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.9439` n `146` status `ready` deltaP `14.2632` edge `0.3503` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0802` n `146` status `ready` deltaP `9.1138` edge `0.0161` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3156` n `146` status `ready` deltaP `2.092` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6227` n `146` status `ready` deltaP `1.3433` edge `0.0366` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6991` n `146` status `ready` deltaP `-0.2061` edge `-0.0029` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0731` n `146` status `ready` deltaP `-3.4787` edge `-0.0059` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1693` n `146` status `ready` deltaP `5.8094` edge `-0.0047` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2942` n `146` status `ready` deltaP `-2.3421` edge `-0.0112` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5886` n `146` status `ready` deltaP `5.0539` edge `0.0909` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6945` n `146` status `ready` deltaP `5.6391` edge `-0.0065` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2295` n `146` status `ready` deltaP `14.5214` edge `0.088` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.305` n `146` status `ready` deltaP `-0.7367` edge `-0.0349` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.773` n `146` status `ready` deltaP `-7.7512` edge `0.0201` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2466` n `146` status `ready` deltaP `-3.3212` edge `-0.0332` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.292` n `146` status `ready` deltaP `-4.4857` edge `-0.0485` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6895` n `146` status `ready` deltaP `-6.3101` edge `0.0847` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.263` n `146` status `ready` deltaP `-2.4386` edge `-0.0131` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6281` n `146` status `ready` deltaP `2.7519` edge `-0.2162` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7583` n `146` status `ready` deltaP `-11.1823` edge `-0.0615` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
