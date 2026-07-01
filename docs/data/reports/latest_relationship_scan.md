# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T03:52:28.321081+00:00`
- Price records: `672`
- Market context records: `5315`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `18.9837` n `153` status `ready` deltaP `22.8247` edge `1.4388` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.2926` n `153` status `ready` deltaP `25.5617` edge `0.8523` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.134` n `153` status `ready` deltaP `19.0972` edge `0.8634` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.1831` n `194` status `ready` deltaP `12.0364` edge `0.3491` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.1447` n `194` status `ready` deltaP `13.3361` edge `0.4024` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.0826` n `194` status `ready` deltaP `11.3119` edge `0.262` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5241` n `153` status `ready` deltaP `13.3068` edge `0.0445` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.4882` n `194` status `ready` deltaP `8.462` edge `0.0808` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.3969` n `153` status `ready` deltaP `20.9967` edge `0.0744` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.0578` n `194` status `ready` deltaP `2.2455` edge `0.086` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0262` n `194` status `ready` deltaP `6.218` edge `0.0111` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0277` n `194` status `ready` deltaP `4.491` edge `0.0923` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.3436` n `194` status `ready` deltaP `2.2455` edge `0.0085` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3874` n `194` status `ready` deltaP `-0.0339` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.482` n `194` status `ready` deltaP `4.6973` edge `0.0228` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6296` n `194` status `ready` deltaP `2.7454` edge `0.0039` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-0.6971` n `194` status `ready` deltaP `10.0421` edge `-0.0068` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4347` n `194` status `ready` deltaP `-3.1761` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3377` n `194` status `ready` deltaP `-6.1573` edge `-0.0062` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1067` n `153` status `ready` deltaP `13.3476` edge `0.3537` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
