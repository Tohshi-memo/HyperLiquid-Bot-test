# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T21:52:17.587808+00:00`
- Price records: `672`
- Market context records: `1054`
- Flow alert records: `4940`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.3074` n `181` status `ready` deltaP `32.8004` edge `1.0283` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.549` n `181` status `ready` deltaP `11.6824` edge `0.4246` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.8602` n `181` status `ready` deltaP `9.9466` edge `0.2467` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2669` n `181` status `ready` deltaP `9.2309` edge `0.204` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.6172` n `181` status `ready` deltaP `-7.7222` edge `0.3511` maxDD `-12.8549`
- `market_context_high->fx_1h` score `-0.059` n `183` status `ready` deltaP `5.6256` edge `0.0005` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4424` n `183` status `ready` deltaP `4.2791` edge `0.0126` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.635` n `183` status `ready` deltaP `-0.4442` edge `0.0245` maxDD `-4.29`
- `market_context_high->commodity_1h` score `-0.6519` n `183` status `ready` deltaP `1.1788` edge `0.0186` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.717` n `182` status `ready` deltaP `0.8577` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-0.9008` n `183` status `ready` deltaP `5.925` edge `0.0039` maxDD `-7.4772`
- `market_context_high->crypto_alt_1h` score `-1.2788` n `183` status `ready` deltaP `0.2438` edge `0.0004` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.34` n `182` status `ready` deltaP `-0.2144` edge `0.0374` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.612` n `182` status `ready` deltaP `0.9766` edge `0.0666` maxDD `-10.2625`
- `market_context_high->metal_1h` score `-1.8282` n `183` status `ready` deltaP `2.931` edge `-0.0337` maxDD `-7.055`
- `market_context_high->crypto_alt_4h` score `-2.7986` n `182` status `ready` deltaP `1.1157` edge `0.0348` maxDD `-15.0367`
- `market_context_high->crypto_major_4h` score `-3.1964` n `182` status `ready` deltaP `6.384` edge `0.0482` maxDD `-21.5703`
- `market_context_high->fx_24h` score `-3.1982` n `181` status `ready` deltaP `2.8354` edge `-0.0213` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5118` n `182` status `ready` deltaP `-4.6184` edge `0.0549` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.8558` n `182` status `ready` deltaP `-0.8443` edge `-0.1636` maxDD `-19.6747`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
