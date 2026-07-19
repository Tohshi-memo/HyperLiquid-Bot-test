# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T23:07:22.146597+00:00`
- Price records: `672`
- Market context records: `7299`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.0976` n `126` status `ready` deltaP `5.148` edge `0.0021` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5162` n `126` status `ready` deltaP `0.1716` edge `-0.0101` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.5272` n `126` status `ready` deltaP `0.1497` edge `0.0353` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.627` n `126` status `ready` deltaP `4.0586` edge `0.0336` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.6763` n `122` status `ready` deltaP `3.0656` edge `-0.0103` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.8892` n `118` status `ready` deltaP `1.0641` edge `0.0017` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-0.939` n `122` status `ready` deltaP `4.0182` edge `0.0128` maxDD `-1.4649`
- `market_context_high->index_1h` score `-1.2366` n `126` status `ready` deltaP `-4.5688` edge `-0.0084` maxDD `-2.1355`
- `market_context_high->unknown_1h` score `-1.2532` n `126` status `ready` deltaP `0.1639` edge `-0.0994` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-1.2569` n `122` status `ready` deltaP `6.5149` edge `0.0877` maxDD `-6.2031`
- `market_context_high->metal_1h` score `-1.3345` n `126` status `ready` deltaP `-8.8062` edge `-0.002` maxDD `-1.4971`
- `market_context_high->crypto_alt_4h` score `-2.1445` n `122` status `ready` deltaP `1.1796` edge `-0.0085` maxDD `-15.2776`
- `market_context_high->metal_4h` score `-2.4087` n `122` status `ready` deltaP `-8.829` edge `-0.0044` maxDD `-4.6441`
- `market_context_high->crypto_major_4h` score `-3.0769` n `122` status `ready` deltaP `1.7343` edge `-0.0166` maxDD `-23.4879`
- `market_context_high->commodity_24h` score `-3.2542` n `118` status `ready` deltaP `-6.5719` edge `-0.1476` maxDD `-2.3815`
- `market_context_high->unknown_24h` score `-3.3013` n `119` status `ready` deltaP `-8.5318` edge `-0.0424` maxDD `-13.9168`
- `market_context_high->equity_1h` score `-4.3326` n `126` status `ready` deltaP `-8.5371` edge `-0.0665` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.8867` n `122` status `ready` deltaP `-14.6387` edge `-0.0562` maxDD `-9.9414`
- `market_context_high->metal_24h` score `-10.9649` n `119` status `ready` deltaP `-28.6517` edge `-0.1265` maxDD `-21.0317`
- `market_context_high->index_24h` score `-12.9248` n `118` status `ready` deltaP `-30.3272` edge `-0.1642` maxDD `-33.1882`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
