# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T06:22:25.813097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5165`

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

- `market_context_high->unknown_24h` score `6625.2835` n `37` status `ready` deltaP `1.3889` edge `552.0977` maxDD `0.0`
- `market_context_high->unknown_4h` score `523.5749` n `42` status `ready` deltaP `8.8415` edge `43.5723` maxDD `0.0`
- `market_context_high->unknown_1h` score `120.1709` n `42` status `ready` deltaP `6.0451` edge `9.985` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.1404` n `37` status `ready` deltaP `41.9154` edge `1.3392` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.6248` n `95` status `ready` deltaP `33.5271` edge `1.0475` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.1828` n `37` status `ready` deltaP `43.8532` edge `0.3373` maxDD `-0.8203`
- `market_context_high->index_24h` score `6.6762` n `37` status `ready` deltaP `49.1319` edge `0.2288` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.3651` n `42` status `ready` deltaP `27.0833` edge `0.3793` maxDD `-1.6876`
- `market_context_high->equity_4h` score `5.5948` n `42` status `ready` deltaP `12.246` edge `0.4548` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `5.0379` n `42` status `ready` deltaP `25.5226` edge `0.2833` maxDD `-1.6901`
- `market_context_high->equity_1h` score `2.4993` n `42` status `ready` deltaP `6.5441` edge `0.2047` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.3605` n `126` status `ready` deltaP `9.623` edge `0.2712` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.9297` n `42` status `ready` deltaP `22.1545` edge `0.0556` maxDD `-0.7323`
- `market_context_high->crypto_alt_1h` score `1.7242` n `42` status `ready` deltaP `5.0613` edge `0.1541` maxDD `-1.5324`
- `market_context_high->crypto_alt_24h` score `1.7123` n `37` status `ready` deltaP `-8.4929` edge `0.3511` maxDD `-8.8096`
- `market_context_high->crypto_major_1h` score `1.5175` n `42` status `ready` deltaP `6.8435` edge `0.1209` maxDD `-1.2051`
- `market_context_high->commodity_4h` score `1.3338` n `42` status `ready` deltaP `24.8766` edge `0.0464` maxDD `-1.633`
- `market_context_high->index_4h` score `1.1747` n `42` status `ready` deltaP `14.6269` edge `0.0393` maxDD `-1.1138`
- `market_context_high->fx_1h` score `1.0482` n `42` status `ready` deltaP `14.2857` edge `0.0095` maxDD `-0.0575`
- `market_context_high->metal_1h` score `0.5107` n `42` status `ready` deltaP `10.586` edge `0.0206` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
