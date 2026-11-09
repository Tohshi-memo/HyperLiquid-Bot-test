# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T08:22:37.479511+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9496`

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

- `market_context_high->equity_24h` score `9.1904` n `32` status `ready` deltaP `16.4931` edge `0.8932` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4305` n `32` status `ready` deltaP `7.8125` edge `0.2092` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.36` n `32` status `ready` deltaP `16.6667` edge `0.1095` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8073` n `32` status `ready` deltaP `11.8056` edge `-0.0026` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.0128` n `77` status `ready` deltaP `5.6858` edge `0.0388` maxDD `-2.3383`
- `market_context_high->metal_1h` score `-0.2562` n `88` status `ready` deltaP `4.8449` edge `0.014` maxDD `-1.4122`
- `market_context_high->commodity_4h` score `-0.2785` n `77` status `ready` deltaP `-0.1801` edge `0.0394` maxDD `-2.9122`
- `market_context_high->commodity_1h` score `-0.4361` n `88` status `ready` deltaP `1.3405` edge `0.0034` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5047` n `77` status `ready` deltaP `5.9234` edge `0.0113` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.8414` n `88` status `ready` deltaP `-5.1102` edge `0.0093` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.1776` n `88` status `ready` deltaP `-5.4096` edge `0.0687` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3031` n `88` status `ready` deltaP `-13.9085` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.6785` n `88` status `ready` deltaP `1.9801` edge `-0.0305` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.82` n `32` status `ready` deltaP `-1.9097` edge `-0.1653` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.6025` n `77` status `ready` deltaP `-15.0024` edge `-0.0155` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0185` n `88` status `ready` deltaP `-4.0623` edge `-0.0976` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.3018` n `32` status `ready` deltaP `-4.8611` edge `0.0382` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.5101` n `77` status `ready` deltaP `3.5457` edge `-0.0215` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-8.8872` n `77` status `ready` deltaP `0.3207` edge `-0.2514` maxDD `-32.6405`
- `market_context_high->crypto_alt_24h` score `-9.175` n `32` status `ready` deltaP `-18.75` edge `-0.1817` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
