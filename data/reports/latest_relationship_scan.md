# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T14:37:35.087641+00:00`
- Price records: `672`
- Market context records: `7678`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14675`

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

- `market_context_high->index_1h` score `0.0234` n `145` status `ready` deltaP `5.8952` edge `0.0116` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1175` n `145` status `ready` deltaP `8.471` edge `0.0245` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1992` n `145` status `ready` deltaP `2.4726` edge `0.0212` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2895` n `144` status `ready` deltaP `9.7706` edge `0.0195` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4417` n `145` status `ready` deltaP `0.7238` edge `-0.0045` maxDD `-1.5561`
- `market_context_high->equity_1h` score `-0.442` n `145` status `ready` deltaP `4.5439` edge `0.0504` maxDD `-6.9884`
- `market_context_high->metal_1h` score `-0.6075` n `145` status `ready` deltaP `1.5693` edge `0.0162` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6856` n `145` status `ready` deltaP `7.7781` edge `0.0284` maxDD `-3.1189`
- `market_context_high->fx_1h` score `-0.7717` n `145` status `ready` deltaP `-1.8411` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->commodity_4h` score `-0.8077` n `145` status `ready` deltaP `0.2299` edge `-0.0008` maxDD `-1.7768`
- `market_context_high->crypto_alt_4h` score `-0.8284` n `145` status `ready` deltaP `3.5607` edge `0.0612` maxDD `-9.2919`
- `market_context_high->crypto_major_4h` score `-0.9481` n `145` status `ready` deltaP `10.1524` edge `0.0678` maxDD `-13.563`
- `market_context_high->commodity_24h` score `-1.3457` n `144` status `ready` deltaP `7.2009` edge `-0.0018` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5341` n `145` status `ready` deltaP `-1.6333` edge `-0.0546` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6347` n `145` status `ready` deltaP `-2.2687` edge `0.0487` maxDD `-4.4521`
- `market_context_high->equity_4h` score `-1.6499` n `145` status `ready` deltaP `-0.3416` edge `0.178` maxDD `-18.647`
- `market_context_high->metal_24h` score `-2.1067` n `145` status `ready` deltaP `-2.8568` edge `0.0615` maxDD `-6.67`
- `market_context_high->equity_24h` score `-2.3316` n `144` status `ready` deltaP `12.4516` edge `0.0451` maxDD `-29.496`
- `market_context_high->fx_4h` score `-2.6381` n `145` status `ready` deltaP `-7.0294` edge `-0.0051` maxDD `-2.0973`
- `market_context_high->index_24h` score `-3.6041` n `144` status `ready` deltaP `-21.5471` edge `-0.0423` maxDD `-7.4228`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
