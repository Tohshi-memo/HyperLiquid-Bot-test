# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T04:37:20.787402+00:00`
- Price records: `672`
- Market context records: `3038`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `23.8913` n `99` status `ready` deltaP `11.8529` edge `2.3036` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.2713` n `99` status `ready` deltaP `23.6269` edge `0.9949` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.924` n `99` status `ready` deltaP `42.5505` edge `0.8174` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.6426` n `99` status `ready` deltaP `23.0272` edge `1.2297` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.326` n `99` status `ready` deltaP `22.6168` edge `0.6686` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7162` n `128` status `ready` deltaP `18.4451` edge `0.1681` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0421` n `129` status `ready` deltaP `2.4405` edge `0.0295` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3718` n `129` status `ready` deltaP `4.3866` edge `0.0245` maxDD `-4.1126`
- `market_context_high->unknown_4h` score `-0.4388` n `128` status `ready` deltaP `1.8103` edge `0.0567` maxDD `-3.7602`
- `market_context_high->crypto_alt_1h` score `-0.4469` n `129` status `ready` deltaP `6.6855` edge `0.1111` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.4497` n `129` status `ready` deltaP `3.8679` edge `0.0381` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.5415` n `129` status `ready` deltaP `-4.8891` edge `0.0` maxDD `-0.2801`
- `market_context_high->unknown_1h` score `-0.6906` n `129` status `ready` deltaP `4.3703` edge `-0.0136` maxDD `-3.1801`
- `market_context_high->index_4h` score `-0.8288` n `128` status `ready` deltaP `12.5572` edge `0.063` maxDD `-15.9043`
- `market_context_high->crypto_major_1h` score `-0.9061` n `129` status `ready` deltaP `4.5792` edge `0.0796` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1116` n `129` status `ready` deltaP `-1.4993` edge `-0.0007` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.1673` n `128` status `ready` deltaP `-9.394` edge `-0.0039` maxDD `-0.9832`
- `market_context_high->fx_24h` score `-1.4213` n `99` status `ready` deltaP `-1.9728` edge `-0.0181` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.7009` n `128` status `ready` deltaP `9.394` edge `0.0543` maxDD `-32.3894`
- `market_context_high->crypto_alt_4h` score `-2.7172` n `128` status `ready` deltaP `18.0068` edge `0.277` maxDD `-53.9652`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
