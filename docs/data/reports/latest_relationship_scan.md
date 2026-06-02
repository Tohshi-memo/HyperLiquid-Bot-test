# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T15:22:32.597176+00:00`
- Price records: `672`
- Market context records: `2674`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9240`

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

- `market_context_high->crypto_alt_24h` score `8.9873` n `111` status `ready` deltaP `16.0051` edge `0.9916` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.5637` n `111` status `ready` deltaP `17.3048` edge `0.6311` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.6497` n `128` status `ready` deltaP `21.3987` edge `0.4266` maxDD `-15.2094`
- `market_context_high->crypto_major_4h` score `1.6703` n `128` status `ready` deltaP `9.2988` edge `0.2582` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.4917` n `128` status `ready` deltaP `7.8125` edge `0.1772` maxDD `-3.7312`
- `market_context_high->index_4h` score `-0.0249` n `128` status `ready` deltaP `8.9939` edge `0.021` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1718` n `137` status `ready` deltaP `2.8924` edge `0.0081` maxDD `-1.2855`
- `market_context_high->fx_24h` score `-0.1741` n `111` status `ready` deltaP `10.6466` edge `0.0017` maxDD `-0.6418`
- `market_context_high->crypto_alt_1h` score `-0.3208` n `137` status `ready` deltaP `6.7846` edge `0.0601` maxDD `-8.3837`
- `market_context_high->index_24h` score `-0.3232` n `111` status `ready` deltaP `6.6207` edge `0.027` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `-0.4047` n `137` status `ready` deltaP `1.9188` edge `0.0149` maxDD `-2.2466`
- `market_context_high->commodity_1h` score `-0.4201` n `137` status `ready` deltaP `2.4422` edge `0.0052` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4969` n `137` status `ready` deltaP `-0.1399` edge `0.0039` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.4984` n `111` status `ready` deltaP `7.9627` edge `0.1924` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.501` n `128` status `ready` deltaP `1.6387` edge `0.0127` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-0.7372` n `137` status `ready` deltaP `-1.5254` edge `-0.002` maxDD `-2.9203`
- `market_context_high->crypto_major_1h` score `-0.7822` n `137` status `ready` deltaP `3.5655` edge `0.0391` maxDD `-7.7187`
- `market_context_high->commodity_4h` score `-1.2772` n `128` status `ready` deltaP `3.0107` edge `0.0082` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.2876` n `137` status `ready` deltaP `-4.986` edge `0.0098` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.3712` n `111` status `ready` deltaP `5.9967` edge `0.5405` maxDD `-44.169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
