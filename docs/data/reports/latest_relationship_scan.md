# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T07:52:28.848550+00:00`
- Price records: `672`
- Market context records: `3262`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10503`

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

- `risk_on_high->crypto_major_4h` score `16.778` n `31` status `ready` deltaP `31.0041` edge `1.3037` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.778` n `31` status `ready` deltaP `31.0041` edge `1.3037` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.7948` n `103` status `ready` deltaP `15.8727` edge `2.6469` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.7828` n `103` status `ready` deltaP `45.5637` edge `0.8043` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1254` n `103` status `ready` deltaP `29.5796` edge `0.8187` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.2409` n `103` status `ready` deltaP `17.6595` edge `1.524` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `5.1146` n `31` status `ready` deltaP `11.8263` edge `0.7613` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1146` n `31` status `ready` deltaP `11.8263` edge `0.7613` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.2498` n `31` status `ready` deltaP `18.809` edge `0.5329` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.2498` n `31` status `ready` deltaP `18.809` edge `0.5329` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.3798` n `159` status `ready` deltaP `20.3453` edge `0.1585` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.1632` n `32` status `ready` deltaP `7.7657` edge `0.3325` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.1632` n `32` status `ready` deltaP `7.7657` edge `0.3325` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.5632` n `31` status `ready` deltaP `5.7533` edge `0.2208` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.5632` n `31` status `ready` deltaP `5.7533` edge `0.2208` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.2632` n `103` status `ready` deltaP `19.0753` edge `2.1047` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3071` n `32` status `ready` deltaP `6.25` edge `0.0662` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3071` n `32` status `ready` deltaP `6.25` edge `0.0662` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2875` n `32` status `ready` deltaP `1.0479` edge `0.1736` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2875` n `32` status `ready` deltaP `1.0479` edge `0.1736` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
