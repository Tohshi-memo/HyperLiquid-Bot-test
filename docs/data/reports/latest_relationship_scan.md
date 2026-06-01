# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T18:37:34.159467+00:00`
- Price records: `672`
- Market context records: `2586`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.3561` n `129` status `ready` deltaP `18.1847` edge `0.5246` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.9955` n `146` status `ready` deltaP `26.5683` edge `0.5904` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.2194` n `146` status `ready` deltaP `17.5075` edge `0.4159` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.7092` n `129` status `ready` deltaP `3.0846` edge `0.7597` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4324` n `146` status `ready` deltaP `11.73` edge `0.1599` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.1254` n `146` status `ready` deltaP `8.9041` edge `0.1394` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9139` n `146` status `ready` deltaP `10.0607` edge `0.1285` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.8421` n `129` status `ready` deltaP `8.3172` edge `0.1128` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.4532` n `129` status `ready` deltaP `17.3531` edge `-0.0109` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.3016` n `146` status `ready` deltaP `9.4325` edge `0.0464` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `0.0009` n `129` status `ready` deltaP `6.9242` edge `0.4557` maxDD `-29.4762`
- `market_context_high->index_1h` score `-0.2222` n `146` status `ready` deltaP `3.3426` edge `0.0086` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4086` n `146` status `ready` deltaP `5.3523` edge `0.0181` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4655` n `146` status `ready` deltaP `1.5011` edge `0.0175` maxDD `-2.6375`
- `market_context_high->metal_4h` score `-0.5602` n `146` status `ready` deltaP `4.9594` edge `0.059` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6656` n `146` status `ready` deltaP `0.8121` edge `0.0139` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7012` n `146` status `ready` deltaP `-1.2837` edge `0.0036` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.8962` n `146` status `ready` deltaP `-0.2255` edge `0.0126` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.9295` n `146` status `ready` deltaP `-1.1258` edge `0.0139` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.971` n `129` status `ready` deltaP `2.6324` edge `0.0009` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
