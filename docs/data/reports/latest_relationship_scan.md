# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T05:22:34.348124+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7022`

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

- `market_context_high->unknown_1h` score `99.6145` n `108` status `ready` deltaP `0.5212` edge `8.3392` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.923` n `96` status `ready` deltaP `2.6168` edge `6.0073` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.5451` n `65` status `ready` deltaP `29.4124` edge `0.6963` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2709` n `65` status `ready` deltaP `32.3992` edge `0.5769` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `8.0297` n `65` status `ready` deltaP `24.1506` edge `0.5701` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.967` n `65` status `ready` deltaP `20.2439` edge `0.4967` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.9271` n `96` status `ready` deltaP `17.1748` edge `0.2831` maxDD `-3.294`
- `news_risk_high->equity_24h` score `3.8301` n `65` status `ready` deltaP `14.1587` edge `0.2348` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3637` n `65` status `ready` deltaP `23.6111` edge `0.1229` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8841` n `65` status `ready` deltaP `31.7613` edge `0.0548` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.6178` n `65` status `ready` deltaP `20.4245` edge `0.143` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5851` n `65` status `ready` deltaP `10.7646` edge `0.1792` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.1249` n `65` status `ready` deltaP `26.216` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9657` n `65` status `ready` deltaP `18.1637` edge `0.0843` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.5484` n `96` status `ready` deltaP `26.2957` edge `0.0294` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3196` n `65` status `ready` deltaP `4.4196` edge `0.1324` maxDD `-2.4854`
- `market_context_high->equity_24h` score `0.8401` n `65` status `ready` deltaP `4.9279` edge `0.0574` maxDD `-0.6196`
- `market_context_high->crypto_alt_4h` score `0.6429` n `96` status `ready` deltaP `2.7439` edge `0.2142` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.5404` n `108` status `ready` deltaP `13.7503` edge `0.006` maxDD `-0.271`
- `market_context_high->fx_24h` score `0.4967` n `65` status `ready` deltaP `12.8205` edge `0.0745` maxDD `-1.703`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
