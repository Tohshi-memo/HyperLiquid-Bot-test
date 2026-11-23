# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T07:07:36.095507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5232`

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

- `market_context_high->unknown_1h` score `16957.8336` n `80` status `ready` deltaP `2.2305` edge `1413.1541` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `11100.8162` n `80` status `ready` deltaP `3.5671` edge `925.0581` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1315.2935` n `31` status `ready` deltaP `3.2789` edge `109.6035` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1167.4767` n `31` status `ready` deltaP `4.0913` edge `97.2681` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.0844` n `31` status `ready` deltaP `35.8527` edge `0.7329` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.4718` n `31` status `ready` deltaP `23.7116` edge `0.8016` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3044` n `31` status `ready` deltaP `12.3574` edge `0.8676` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7795` n `31` status `ready` deltaP `18.9395` edge `0.2074` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4602` n `31` status `ready` deltaP `36.31` edge `0.0723` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6651` n `31` status `ready` deltaP `31.244` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3924` n `31` status `ready` deltaP `9.4118` edge `0.2901` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9824` n `31` status `ready` deltaP `7.9148` edge `0.2371` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5096` n `31` status `ready` deltaP `28.8342` edge `0.0292` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4198` n `31` status `ready` deltaP `19.6744` edge `0.1066` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8351` n `31` status `ready` deltaP `18.1255` edge `0.026` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.3347` n `80` status `ready` deltaP `13.1707` edge `0.0146` maxDD `-0.4261`
- `news_risk_high->commodity_1h` score `-0.0178` n `31` status `ready` deltaP `1.6805` edge `0.0135` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.132` n `80` status `ready` deltaP `3.3907` edge `0.0123` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1617` n `80` status `ready` deltaP `3.0988` edge `0.0042` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.8176` n `80` status `ready` deltaP `8.3841` edge `0.0164` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
