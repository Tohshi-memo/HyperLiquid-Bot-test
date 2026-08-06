# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T09:37:29.740977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `10.8298` n `96` status `ready` deltaP `4.1666` edge `0.879` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.131` n `109` status `ready` deltaP `-0.7356` edge `0.4487` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.059` n `109` status `ready` deltaP `12.8371` edge `0.0873` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9675` n `96` status `ready` deltaP `4.1666` edge `0.2131` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5738` n `96` status `ready` deltaP `21.875` edge `0.0483` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4227` n `109` status `ready` deltaP `7.7597` edge `0.0251` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0003` n `109` status `ready` deltaP `5.6831` edge `-0.0029` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2561` n `109` status `ready` deltaP `7.18` edge `0.0053` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5331` n `109` status `ready` deltaP `-1.7099` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7159` n `109` status `ready` deltaP `-2.9075` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.75` n `109` status `ready` deltaP `3.2418` edge `0.0057` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3828` n `96` status `ready` deltaP `-4.5139` edge `0.0723` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4701` n `109` status `ready` deltaP `-4.8385` edge `-0.0192` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7731` n `109` status `ready` deltaP `1.7182` edge `-0.0852` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0098` n `109` status `ready` deltaP `-11.4483` edge `-0.0559` maxDD `-4.7021`
- `market_context_high->crypto_alt_24h` score `-2.1412` n `96` status `ready` deltaP `-0.6945` edge `-0.0295` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-2.1695` n `109` status `ready` deltaP `1.0796` edge `-0.049` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.2096` n `109` status `ready` deltaP `1.1344` edge `-0.147` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2396` n `109` status `ready` deltaP `-10.9996` edge `-0.0593` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.6962` n `96` status `ready` deltaP `5.5555` edge `-0.0345` maxDD `-52.2157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
