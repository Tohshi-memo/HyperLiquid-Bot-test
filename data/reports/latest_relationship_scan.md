# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T21:52:22.474461+00:00`
- Price records: `672`
- Market context records: `2906`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `11.6687` n `142` status `ready` deltaP `11.0354` edge `1.2905` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.1739` n `142` status `ready` deltaP `13.0746` edge `0.6277` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.3598` n `142` status `ready` deltaP `11.2822` edge `0.4179` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1958` n `142` status `ready` deltaP `10.2382` edge `0.2128` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.776` n `142` status `ready` deltaP `15.5516` edge `0.3537` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4673` n `142` status `ready` deltaP `13.1484` edge `0.0564` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.1507` n `142` status `ready` deltaP `6.0782` edge `0.11` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1061` n `142` status `ready` deltaP `4.6612` edge `0.0831` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0609` n `142` status `ready` deltaP `3.8986` edge `0.0156` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3169` n `142` status `ready` deltaP `4.1811` edge `0.0188` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.4781` n `142` status `ready` deltaP `14.7951` edge `0.2956` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-0.5095` n `142` status `ready` deltaP `-0.2045` edge `0.0422` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5315` n `142` status `ready` deltaP `5.695` edge `0.0699` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.6029` n `142` status `ready` deltaP `-1.2861` edge `0.0027` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6038` n `142` status `ready` deltaP `-0.5819` edge `0.0018` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6497` n `142` status `ready` deltaP `5.8721` edge `0.0645` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6715` n `142` status `ready` deltaP `-0.3163` edge `0.0006` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-1.0567` n `142` status `ready` deltaP `-2.5335` edge `0.0067` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2056` n `142` status `ready` deltaP `2.7525` edge `0.0191` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2924` n `142` status `ready` deltaP `-1.7116` edge `-0.0091` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
