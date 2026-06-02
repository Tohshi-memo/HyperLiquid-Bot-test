# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T17:52:26.569915+00:00`
- Price records: `672`
- Market context records: `2685`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `9.2885` n `111` status `ready` deltaP `16.0051` edge `1.0167` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6983` n `111` status `ready` deltaP `17.652` edge `0.64` maxDD `-1.626`
- `market_context_high->unknown_4h` score `1.1356` n `135` status `ready` deltaP `6.1654` edge `0.1585` maxDD `-3.7312`
- `market_context_high->crypto_alt_4h` score `0.5488` n `135` status `ready` deltaP `18.0364` edge `0.3047` maxDD `-24.3368`
- `market_context_high->index_4h` score `0.2793` n `135` status `ready` deltaP `10.9383` edge `0.0345` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1337` n `141` status `ready` deltaP `3.2945` edge `0.0103` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1459` n `141` status `ready` deltaP `2.9632` edge `0.0409` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3514` n `111` status `ready` deltaP `8.9105` edge `-0.0015` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4385` n `141` status `ready` deltaP `1.773` edge `0.0073` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4416` n `141` status `ready` deltaP `0.5362` edge `0.004` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5401` n `141` status `ready` deltaP `6.3989` edge `0.0641` maxDD `-10.747`
- `market_context_high->commodity_24h` score `-0.6093` n `111` status `ready` deltaP `7.6155` edge `0.1805` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.6411` n `135` status `ready` deltaP `0.0226` edge `0.0118` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.6889` n `111` status `ready` deltaP `4.8846` edge `0.0081` maxDD `-2.5127`
- `market_context_high->metal_1h` score `-0.7943` n `141` status `ready` deltaP `-2.0332` edge `-0.0054` maxDD `-2.9635`
- `market_context_high->crypto_major_1h` score `-0.9906` n `141` status `ready` deltaP `3.562` edge `0.0362` maxDD `-9.622`
- `market_context_high->crypto_major_24h` score `-1.1084` n `111` status `ready` deltaP `5.9967` edge `0.5742` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.1147` n `135` status `ready` deltaP `4.1407` edge `0.0215` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.138` n `141` status `ready` deltaP `-3.8518` edge `0.0147` maxDD `-2.7085`
- `market_context_high->crypto_major_4h` score `-1.2765` n `135` status `ready` deltaP `6.3821` edge `0.1489` maxDD `-24.0746`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
