# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T18:22:32.880584+00:00`
- Price records: `672`
- Market context records: `2687`
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

- `market_context_high->crypto_alt_24h` score `9.3821` n `111` status `ready` deltaP `16.0051` edge `1.0245` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6875` n `111` status `ready` deltaP `17.652` edge `0.6391` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8727` n `137` status `ready` deltaP `5.3543` edge `0.142` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.3268` n `137` status `ready` deltaP `11.4574` edge `0.035` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.142` n `142` status `ready` deltaP `3.1943` edge `0.0099` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.1521` n `137` status `ready` deltaP `17.2912` edge `0.2857` maxDD `-27.0921`
- `market_context_high->unknown_1h` score `-0.2079` n `142` status `ready` deltaP `2.5787` edge `0.0383` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3852` n `111` status `ready` deltaP `8.5633` edge `-0.002` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4309` n `142` status `ready` deltaP `1.963` edge `0.007` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4592` n `142` status `ready` deltaP `0.3163` edge `0.004` maxDD `-0.2164`
- `market_context_high->commodity_24h` score `-0.6663` n `111` status `ready` deltaP `7.2682` edge `0.1755` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.6832` n `137` status `ready` deltaP `-0.4295` edge `0.0113` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.7232` n `111` status `ready` deltaP `4.711` edge `0.0064` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `-0.7734` n `142` status `ready` deltaP `6.6986` edge `0.0669` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.8117` n `142` status `ready` deltaP `-2.0684` edge `-0.0057` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9607` n `142` status `ready` deltaP `3.8817` edge `0.0379` maxDD `-9.622`
- `market_context_high->crypto_major_24h` score `-1.0358` n `111` status `ready` deltaP `5.9967` edge `0.5835` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.0738` n `137` status `ready` deltaP `4.463` edge `0.0246` maxDD `-10.0279`
- `market_context_high->equity_1h` score `-1.1744` n `142` status `ready` deltaP `-4.0967` edge `0.0133` maxDD `-2.7085`
- `market_context_high->crypto_major_4h` score `-1.8338` n `137` status `ready` deltaP `5.6035` edge `0.1289` maxDD `-27.1086`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
