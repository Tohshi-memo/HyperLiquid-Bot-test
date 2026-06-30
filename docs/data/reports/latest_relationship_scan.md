# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T14:22:31.212986+00:00`
- Price records: `672`
- Market context records: `5255`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `25.4057` n `144` status `ready` deltaP `29.6875` edge `1.9382` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.8577` n `144` status `ready` deltaP `29.8611` edge `1.0719` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.0592` n `159` status `ready` deltaP `13.6927` edge `0.4069` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.7465` n `159` status `ready` deltaP `13.8835` edge `0.4489` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.1055` n `144` status `ready` deltaP `19.2708` edge `0.6932` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.7364` n `159` status `ready` deltaP `16.1729` edge `0.1391` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `1.7143` n `144` status `ready` deltaP `16.493` edge `0.5677` maxDD `-32.7838`
- `market_context_high->crypto_alt_1h` score `0.6057` n `166` status `ready` deltaP `5.1042` edge `0.1126` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.5122` n `159` status `ready` deltaP `8.1675` edge `0.1521` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5071` n `144` status `ready` deltaP `12.6736` edge `0.0473` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4646` n `166` status `ready` deltaP `6.4443` edge `0.1203` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.1355` n `144` status `ready` deltaP `20.4861` edge `0.0443` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.098` n `166` status `ready` deltaP `6.6446` edge `0.0604` maxDD `-5.0555`
- `market_context_high->unknown_1h` score `-0.057` n `166` status `ready` deltaP `8.1596` edge `0.005` maxDD `-2.7986`
- `market_context_high->index_1h` score `-0.0857` n `166` status `ready` deltaP `4.8337` edge `0.011` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1518` n `166` status `ready` deltaP `4.6551` edge `0.0155` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3185` n `166` status `ready` deltaP `0.7665` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.7422` n `159` status `ready` deltaP `4.6028` edge `0.0192` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8113` n `159` status `ready` deltaP `-0.1984` edge `0.0007` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.3012` n `166` status `ready` deltaP `-2.7054` edge `-0.0063` maxDD `-2.728`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
