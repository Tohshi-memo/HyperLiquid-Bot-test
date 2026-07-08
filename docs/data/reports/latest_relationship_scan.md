# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T23:22:31.278495+00:00`
- Price records: `672`
- Market context records: `6135`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.7872` n `30` status `ready` deltaP `39.6875` edge `0.6491` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.7505` n `30` status `ready` deltaP `68.5764` edge `0.1887` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3457` n `32` status `ready` deltaP `45.3506` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4051` n `32` status `ready` deltaP `28.8922` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.4238` n `195` status `ready` deltaP `0.6549` edge `0.2151` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.1926` n `32` status `ready` deltaP `13.0801` edge `0.1124` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.5917` n `32` status `ready` deltaP `8.1774` edge `0.0675` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.4091` n `195` status `ready` deltaP `3.9024` edge `0.0998` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1453` n `30` status `ready` deltaP `8.1944` edge `0.0139` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2668` n `195` status `ready` deltaP `1.5845` edge `-0.0002` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3895` n `195` status `ready` deltaP `-2.7643` edge `0.2392` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `-0.5743` n `30` status `ready` deltaP `14.0973` edge `-0.1213` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `-0.5785` n `30` status `ready` deltaP `10.0347` edge `-0.0631` maxDD `-4.2368`
- `market_context_high->metal_4h` score `-0.6532` n `195` status `ready` deltaP `3.3896` edge `0.0124` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7727` n `195` status `ready` deltaP `-2.2885` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.812` n `32` status `ready` deltaP `-3.5928` edge `-0.0304` maxDD `-1.6464`
- `market_context_high->equity_1h` score `-0.8289` n `195` status `ready` deltaP `-0.8583` edge `0.011` maxDD `-4.2573`
- `market_context_high->metal_1h` score `-0.8835` n `195` status `ready` deltaP `1.7918` edge `-0.0057` maxDD `-2.0564`
- `market_context_high->metal_24h` score `-0.9134` n `195` status `ready` deltaP `15.5155` edge `0.0363` maxDD `-11.8809`
- `market_context_high->crypto_alt_1h` score `-0.9842` n `195` status `ready` deltaP `3.1614` edge `0.028` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
