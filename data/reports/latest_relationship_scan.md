# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T12:52:26.813377+00:00`
- Price records: `672`
- Market context records: `5353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11482`

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

- `market_context_high->unknown_24h` score `14.7257` n `162` status `ready` deltaP `19.5795` edge `1.1056` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.3497` n `162` status `ready` deltaP `21.7399` edge `0.7549` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.4594` n `162` status `ready` deltaP `17.8048` edge `0.8158` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.6635` n `194` status `ready` deltaP `13.3361` edge `0.3623` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.3456` n `194` status `ready` deltaP `10.2071` edge `0.2915` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6894` n `194` status `ready` deltaP `9.7875` edge `0.2394` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8077` n `162` status `ready` deltaP `24.5178` edge `0.1036` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.2215` n `198` status `ready` deltaP `6.5823` edge `0.0711` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1421` n `162` status `ready` deltaP `9.4908` edge `0.0381` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.0592` n `198` status `ready` deltaP `5.1806` edge `0.0109` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.123` n `198` status `ready` deltaP `3.7803` edge `0.0891` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.1586` n `198` status `ready` deltaP `1.0857` edge `0.0757` maxDD `-5.0257`
- `market_context_high->index_4h` score `-0.4141` n `194` status `ready` deltaP `5.6119` edge `0.0254` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4312` n `198` status `ready` deltaP `-0.7863` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.514` n `198` status `ready` deltaP `0.2434` edge `0.0` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7095` n `194` status `ready` deltaP `1.3735` edge `0.0028` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2171` n `194` status `ready` deltaP `7.908` edge `-0.0359` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5711` n `198` status `ready` deltaP `-4.3776` edge `-0.0085` maxDD `-3.4592`
- `market_context_high->metal_4h` score `-2.6651` n `194` status `ready` deltaP `-7.8341` edge `-0.037` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8286` n `194` status `ready` deltaP `-7.1662` edge `-0.0429` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
