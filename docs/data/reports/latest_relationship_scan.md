# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T01:22:27.078250+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9488`

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

- `market_context_high->unknown_24h` score `1060.8731` n `45` status `ready` deltaP `-19.7916` edge `88.5744` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `38.4985` n `110` status `ready` deltaP `-8.9911` edge `3.3387` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.332` n `45` status `ready` deltaP `30.1736` edge `0.6194` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.0776` n `45` status `ready` deltaP `50.382` edge `0.1749` maxDD `-0.012`
- `risk_on_high->crypto_alt_4h` score `5.4458` n `31` status `ready` deltaP `23.6084` edge `0.3412` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.4458` n `31` status `ready` deltaP `23.6084` edge `0.3412` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `3.9948` n `45` status `ready` deltaP `-11.6667` edge `0.7255` maxDD `-17.8526`
- `risk_on_high->crypto_major_4h` score `3.1221` n `31` status `ready` deltaP `26.1506` edge `0.3112` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.1221` n `31` status `ready` deltaP `26.1506` edge `0.3112` maxDD `-4.1548`
- `risk_on_high->metal_4h` score `2.9073` n `31` status `ready` deltaP `26.3523` edge `0.0898` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.9073` n `31` status `ready` deltaP `26.3523` edge `0.0898` maxDD `-0.1896`
- `market_context_high->fx_24h` score `1.9124` n `45` status `ready` deltaP `23.368` edge `0.0266` maxDD `-0.1747`
- `risk_on_high->crypto_alt_1h` score `1.6153` n `43` status `ready` deltaP `10.775` edge `0.1183` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6153` n `43` status `ready` deltaP `10.775` edge `0.1183` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.5635` n `43` status `ready` deltaP `14.5175` edge `0.0988` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.5635` n `43` status `ready` deltaP `14.5175` edge `0.0988` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.3908` n `43` status `ready` deltaP `17.0728` edge `0.026` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.3908` n `43` status `ready` deltaP `17.0728` edge `0.026` maxDD `-0.2466`
- `market_context_high->unknown_1h` score `1.1917` n `122` status `ready` deltaP `-3.34` edge `0.1552` maxDD `-1.0231`
- `risk_on_high->equity_4h` score `0.668` n `31` status `ready` deltaP `5.6501` edge `0.0861` maxDD `-1.0501`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
