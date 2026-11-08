# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T11:22:27.557437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4713`

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

- `market_context_high->unknown_4h` score `95.9418` n `37` status `ready` deltaP `-4.2436` edge `8.0682` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0141` n `37` status `ready` deltaP `15.4139` edge `0.8279` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.2676` n `37` status `ready` deltaP `10.5074` edge `0.2482` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1205` n `37` status `ready` deltaP `33.619` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.397` n `38` status `ready` deltaP `28.4981` edge `0.0183` maxDD `-0.016`
- `market_context_high->index_4h` score `2.0682` n `37` status `ready` deltaP `26.9652` edge `0.0396` maxDD `-2.4279`
- `market_context_high->crypto_major_1h` score `0.8382` n `37` status `ready` deltaP `10.1999` edge `0.0604` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8381` n `37` status `ready` deltaP `10.6982` edge `0.0992` maxDD `-2.7123`
- `market_context_high->commodity_24h` score `0.8044` n `37` status `ready` deltaP `7.775` edge `0.1708` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.6602` n `37` status `ready` deltaP `10.9422` edge `-0.0091` maxDD `-0.0397`
- `news_risk_high->fx_24h` score `0.6168` n `35` status `ready` deltaP `1.2897` edge `0.0649` maxDD `-0.1014`
- `market_context_high->crypto_alt_1h` score `0.5651` n `37` status `ready` deltaP `12.4454` edge `0.071` maxDD `-3.1881`
- `news_risk_high->fx_1h` score `0.5393` n `38` status `ready` deltaP `12.5828` edge `0.0068` maxDD `-0.0567`
- `market_context_high->fx_1h` score `0.3607` n `37` status `ready` deltaP `6.3239` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3105` n `37` status `ready` deltaP `2.0999` edge `0.0389` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1023` n `37` status `ready` deltaP `8.7191` edge `0.0096` maxDD `-1.7019`
- `news_risk_high->equity_4h` score `0.0151` n `38` status `ready` deltaP `-2.9766` edge `0.095` maxDD `-4.2454`
- `news_risk_high->index_1h` score `-0.0246` n `38` status `ready` deltaP `6.0117` edge `0.0021` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0474` n `37` status `ready` deltaP `1.5011` edge `0.0167` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0607` n `37` status `ready` deltaP `2.2248` edge `0.0228` maxDD `-1.633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
