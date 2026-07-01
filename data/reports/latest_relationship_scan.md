# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T15:52:33.490678+00:00`
- Price records: `672`
- Market context records: `5366`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `10.1624` n `174` status `ready` deltaP `17.1576` edge `0.7455` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.1439` n `174` status `ready` deltaP `22.1684` edge `0.7349` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.3231` n `174` status `ready` deltaP `15.3616` edge `0.7374` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.2484` n `198` status `ready` deltaP `12.7972` edge `0.3313` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.7498` n `198` status `ready` deltaP `9.4051` edge `0.2472` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.205` n `198` status `ready` deltaP `8.2917` edge `0.209` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.4122` n `174` status `ready` deltaP `17.5826` edge `0.0975` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.1095` n `205` status `ready` deltaP `5.9632` edge `0.0659` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.0474` n `174` status `ready` deltaP `8.908` edge `0.0341` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.0878` n `205` status `ready` deltaP `3.8754` edge `0.0914` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.1098` n `205` status `ready` deltaP `4.2289` edge `0.012` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1234` n `205` status `ready` deltaP `1.4802` edge `0.076` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4329` n `205` status `ready` deltaP `-0.804` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5442` n `205` status `ready` deltaP `1.3305` edge `0.0133` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.8913` n `198` status `ready` deltaP `4.7934` edge `0.0234` maxDD `-2.704`
- `market_context_high->fx_4h` score `-1.0483` n `198` status `ready` deltaP `1.974` edge `0.0024` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5034` n `205` status `ready` deltaP `-3.6198` edge `-0.0067` maxDD `-3.5563`
- `market_context_high->unknown_4h` score `-1.5133` n `198` status `ready` deltaP `7.4449` edge `-0.0573` maxDD `-6.1421`
- `market_context_high->metal_4h` score `-2.7925` n `198` status `ready` deltaP `-8.4242` edge `-0.0494` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.5762` n `174` status `ready` deltaP `12.6497` edge `0.3269` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
