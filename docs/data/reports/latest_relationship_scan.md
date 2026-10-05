# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T04:37:27.887164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5134`

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

- `market_context_high->unknown_1h` score `104.9611` n `105` status `ready` deltaP `0.0186` edge `8.7881` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `72.6892` n `95` status `ready` deltaP `2.4743` edge `6.0721` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.8509` n `62` status `ready` deltaP `29.7099` edge `0.7198` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2817` n `65` status `ready` deltaP `32.3992` edge `0.5778` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `8.7377` n `62` status `ready` deltaP `24.076` edge `0.6296` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `6.027` n `65` status `ready` deltaP `20.2439` edge `0.5017` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `4.1744` n `95` status `ready` deltaP `17.9862` edge `0.2983` maxDD `-3.294`
- `news_risk_high->equity_24h` score `4.0254` n `65` status `ready` deltaP `14.6795` edge `0.2476` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3769` n `65` status `ready` deltaP `23.6111` edge `0.124` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.6706` n `65` status `ready` deltaP `20.4245` edge `0.1474` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.6115` n `65` status `ready` deltaP `10.7646` edge `0.1814` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.1249` n `65` status `ready` deltaP `26.216` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9741` n `65` status `ready` deltaP `18.1637` edge `0.085` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5463` n `95` status `ready` deltaP `26.2388` edge `0.0296` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3496` n `65` status `ready` deltaP `4.4196` edge `0.1349` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `1.204` n `105` status `ready` deltaP `11.2775` edge `0.0922` maxDD `-3.0307`
- `market_context_high->equity_24h` score `1.1114` n `62` status `ready` deltaP `4.7043` edge `0.0815` maxDD `-0.6196`
- `market_context_high->fx_24h` score `1.0421` n `62` status `ready` deltaP `15.0538` edge `0.0786` maxDD `-1.703`
- `market_context_high->crypto_alt_4h` score `0.9068` n `95` status `ready` deltaP `3.4018` edge `0.2318` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
