# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T17:22:28.297720+00:00`
- Price records: `672`
- Market context records: `2683`
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

- `market_context_high->crypto_alt_24h` score `9.2297` n `111` status `ready` deltaP `16.0051` edge `1.0118` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7349` n `111` status `ready` deltaP `17.8256` edge `0.6419` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `1.4664` n `133` status `ready` deltaP `18.9609` edge `0.331` maxDD `-20.8162`
- `market_context_high->unknown_4h` score `1.3164` n `133` status `ready` deltaP `7.0008` edge `0.168` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.135` n `133` status `ready` deltaP `10.4037` edge `0.0321` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1539` n `141` status `ready` deltaP `2.9951` edge `0.0097` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1843` n `141` status `ready` deltaP `2.8135` edge `0.0387` maxDD `-3.1587`
- `market_context_high->fx_24h` score `-0.3189` n `111` status `ready` deltaP `9.2577` edge `-0.0011` maxDD `-0.6418`
- `market_context_high->commodity_1h` score `-0.4174` n `141` status `ready` deltaP `2.0724` edge `0.008` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4547` n `141` status `ready` deltaP `0.3865` edge `0.0039` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5043` n `141` status `ready` deltaP `6.6983` edge `0.0667` maxDD `-10.747`
- `market_context_high->commodity_24h` score `-0.5506` n `111` status `ready` deltaP `7.9627` edge `0.1857` maxDD `-12.4171`
- `market_context_high->fx_4h` score `-0.5995` n `133` status `ready` deltaP `0.4975` edge `0.0121` maxDD `-0.5631`
- `market_context_high->index_24h` score `-0.6312` n `111` status `ready` deltaP `5.2318` edge `0.0106` maxDD `-2.5127`
- `market_context_high->crypto_major_4h` score `-0.6734` n `133` status `ready` deltaP `7.1841` edge `0.1749` maxDD `-20.3972`
- `market_context_high->metal_1h` score `-0.7943` n `141` status `ready` deltaP `-2.0332` edge `-0.0054` maxDD `-2.9635`
- `market_context_high->crypto_major_1h` score `-0.9843` n `141` status `ready` deltaP `3.562` edge `0.037` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1548` n `141` status `ready` deltaP `-4.0015` edge `0.0143` maxDD `-2.7085`
- `market_context_high->crypto_major_24h` score `-1.1723` n `111` status `ready` deltaP `5.9967` edge `0.566` maxDD `-44.169`
- `market_context_high->commodity_4h` score `-1.1959` n `133` status `ready` deltaP `3.4947` edge `0.0154` maxDD `-10.0279`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
