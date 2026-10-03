# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T10:37:26.516750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.2854` n `50` status `ready` deltaP `11.024` edge `30.4552` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.278` n `50` status `ready` deltaP `12.0244` edge `24.443` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.1488` n `50` status `ready` deltaP `27.2062` edge `1.0847` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `10.6466` n `68` status `ready` deltaP `40.0864` edge `0.6403` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.5477` n `50` status `ready` deltaP `34.8596` edge `0.7882` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.1131` n `68` status `ready` deltaP `28.7007` edge `0.6999` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.8732` n `68` status `ready` deltaP `29.132` edge `0.5963` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4639` n `50` status `ready` deltaP `18.3805` edge `0.5698` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3114` n `50` status `ready` deltaP `18.2496` edge `0.5332` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.3408` n `68` status `ready` deltaP `32.8499` edge `0.1586` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.996` n `68` status `ready` deltaP `28.4202` edge `0.2048` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3561` n `50` status `ready` deltaP `15.4012` edge `0.2433` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.0433` n `68` status `ready` deltaP `14.4065` edge `0.1931` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0433` n `68` status `ready` deltaP `33.5415` edge `0.0562` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0127` n `50` status `ready` deltaP `33.8174` edge `0.0391` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0121` n `50` status `ready` deltaP `13.7006` edge `0.2047` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.2451` n `68` status `ready` deltaP `18.5357` edge `0.1051` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.4735` n `50` status `ready` deltaP `20.6407` edge `0.0116` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.4523` n `68` status `ready` deltaP `5.2836` edge `0.1377` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.3753` n `68` status `ready` deltaP `12.5837` edge `0.0669` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
