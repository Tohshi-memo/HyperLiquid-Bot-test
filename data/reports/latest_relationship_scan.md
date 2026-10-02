# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T00:37:29.398713+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.6651` n `50` status `ready` deltaP `9.8263` edge `28.1615` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.3257` n `50` status `ready` deltaP `8.5366` edge `23.8869` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3709` n `84` status `ready` deltaP `37.7232` edge `1.3837` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.8398` n `50` status `ready` deltaP `35.6458` edge `0.8073` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2597` n `50` status `ready` deltaP `19.0671` edge `0.5482` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.8024` n `50` status `ready` deltaP `14.1042` edge `0.6438` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.9826` n `50` status `ready` deltaP `16.3415` edge `0.4356` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.6308` n `50` status `ready` deltaP `18.8681` edge `0.5259` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.5147` n `84` status `ready` deltaP `15.5506` edge `0.5046` maxDD `-15.8971`
- `market_context_high->crypto_major_1h` score `3.0347` n `50` status `ready` deltaP `14.7485` edge `0.1996` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9709` n `50` status `ready` deltaP `13.9042` edge `0.2212` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9482` n `50` status `ready` deltaP `33.1463` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.7955` n `97` status `ready` deltaP `24.7281` edge `0.1377` maxDD `-2.9013`
- `news_risk_high->crypto_alt_4h` score `2.5456` n `97` status `ready` deltaP `10.259` edge `0.2781` maxDD `-6.4152`
- `news_risk_high->equity_24h` score `2.3066` n `84` status `ready` deltaP `15.1538` edge `0.4231` maxDD `-9.2721`
- `news_risk_high->commodity_24h` score `1.7733` n `84` status `ready` deltaP `27.877` edge `0.1539` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.5859` n `84` status `ready` deltaP `17.0883` edge `0.2168` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.4952` n `84` status `ready` deltaP `18.6012` edge `0.0484` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.4735` n `50` status `ready` deltaP `20.6407` edge `0.0116` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9198` n `50` status `ready` deltaP `14.7917` edge `0.0764` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
