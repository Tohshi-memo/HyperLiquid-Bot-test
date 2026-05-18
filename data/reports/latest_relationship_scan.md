# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T09:07:16.174429+00:00`
- Price records: `672`
- Market context records: `1103`
- Flow alert records: `5079`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `17.2267` n `150` status `ready` deltaP `37.382` edge `1.2327` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `6.6338` n `150` status `ready` deltaP `13.743` edge `0.5846` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.1331` n `150` status `ready` deltaP `15.6527` edge `0.4564` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.283` n `150` status `ready` deltaP `-2.9305` edge `0.6265` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.8753` n `150` status `ready` deltaP `15.1319` edge `0.3362` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.8918` n `168` status `ready` deltaP `10.9466` edge `0.151` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.9747` n `168` status `ready` deltaP `8.8995` edge `0.0902` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.451` n `168` status `ready` deltaP `7.346` edge `0.0203` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.2285` n `168` status `ready` deltaP `2.2811` edge `0.0416` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1376` n `168` status `ready` deltaP `8.3155` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0657` n `168` status `ready` deltaP `7.1322` edge `0.0345` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `0.0395` n `168` status `ready` deltaP `8.4567` edge `0.1408` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.222` n `168` status `ready` deltaP `6.8007` edge `-0.0028` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.279` n `168` status `ready` deltaP `2.9441` edge `0.0414` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.6835` n `168` status `ready` deltaP `-1.0265` edge `0.0` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.6875` n `168` status `ready` deltaP `1.5461` edge `0.0012` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.0803` n `168` status `ready` deltaP `5.2338` edge `0.1231` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.2785` n `168` status `ready` deltaP `7.3098` edge `-0.0432` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1235` n `168` status `ready` deltaP `-10.6635` edge `-0.0126` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.2605` n `150` status `ready` deltaP `2.3889` edge `-0.0263` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
