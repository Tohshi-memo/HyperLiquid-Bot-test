# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T10:52:24.541023+00:00`
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

- `market_context_high->unknown_1h` score `366.3262` n `50` status `ready` deltaP `11.024` edge `30.4586` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.2828` n `50` status `ready` deltaP `12.0244` edge `24.4434` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2191` n `50` status `ready` deltaP `27.3795` edge `1.0894` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `10.7473` n `67` status `ready` deltaP `40.0849` edge `0.6487` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.6251` n `50` status `ready` deltaP `35.0329` edge `0.7935` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.1368` n `67` status `ready` deltaP `28.547` edge `0.7029` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.9056` n `67` status `ready` deltaP `28.8466` edge `0.6009` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4773` n `50` status `ready` deltaP `18.5327` edge `0.5699` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3126` n `50` status `ready` deltaP `18.2496` edge `0.5333` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.3619` n `67` status `ready` deltaP `32.7841` edge `0.1608` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9995` n `67` status `ready` deltaP `28.1788` edge `0.2067` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3525` n `50` status `ready` deltaP `15.4012` edge `0.243` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.0418` n `67` status `ready` deltaP `33.3878` edge `0.0571` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0261` n `50` status `ready` deltaP `33.9696` edge `0.0392` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0145` n `50` status `ready` deltaP `13.7006` edge `0.2049` maxDD `-2.2692`
- `news_risk_high->crypto_major_1h` score `3.0047` n `67` status `ready` deltaP `13.8797` edge `0.1934` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2289` n `67` status `ready` deltaP `18.183` edge `0.1061` maxDD `-0.993`
- `market_context_high->fx_1h` score `1.4855` n `50` status `ready` deltaP `20.7904` edge `0.0116` maxDD `-0.113`
- `news_risk_high->crypto_alt_1h` score `1.3768` n `67` status `ready` deltaP `4.6251` edge `0.1358` maxDD `-2.4854`
- `news_risk_high->equity_1h` score `1.3397` n `67` status `ready` deltaP `12.0788` edge `0.0673` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
