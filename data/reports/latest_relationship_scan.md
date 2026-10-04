# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T13:22:25.161551+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `121.0143` n `83` status `ready` deltaP `2.1433` edge `10.1014` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `100.8577` n `95` status `ready` deltaP `-0.9785` edge `8.4528` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `11.0657` n `46` status `ready` deltaP `27.8306` edge `0.8639` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.6804` n `46` status `ready` deltaP `34.2693` edge `0.7268` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.5893` n `65` status `ready` deltaP `37.7345` edge `0.6512` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `8.9562` n `65` status `ready` deltaP `25.2698` edge `0.5879` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2195` n `65` status `ready` deltaP `23.75` edge `0.5777` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.8339` n `83` status `ready` deltaP `24.9449` edge `0.3902` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.0939` n `65` status `ready` deltaP `28.2986` edge `0.1525` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8128` n `65` status `ready` deltaP `25.9123` edge `0.206` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0782` n `65` status `ready` deltaP `33.4381` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9592` n `65` status `ready` deltaP `12.8604` edge `0.1964` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.539` n `65` status `ready` deltaP `21.6698` edge `0.1087` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.4149` n `46` status `ready` deltaP `5.3366` edge `0.2648` maxDD `-6.264`
- `market_context_high->crypto_major_1h` score `2.1746` n `95` status `ready` deltaP `15.1277` edge `0.1254` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0974` n `65` status `ready` deltaP `25.7669` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_4h` score `2.0559` n `83` status `ready` deltaP `6.4006` edge `0.2909` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.5594` n `65` status `ready` deltaP `5.1681` edge `0.1474` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `1.0433` n `95` status `ready` deltaP `15.9975` edge `0.0067` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
