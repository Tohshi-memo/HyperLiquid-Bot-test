# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T07:22:32.593534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6964`

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

- `market_context_high->unknown_1h` score `85.3698` n `116` status `ready` deltaP `1.0221` edge `7.1488` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `59.1893` n `104` status `ready` deltaP `2.0403` edge `4.95` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.4947` n `73` status `ready` deltaP `29.3973` edge `0.6922` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3179` n `65` status `ready` deltaP `32.5516` edge `0.5798` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.108` n `73` status `ready` deltaP `24.2842` edge `0.4924` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8334` n `65` status `ready` deltaP `19.939` edge `0.4876` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4106` n `65` status `ready` deltaP `12.7698` edge `0.2091` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3445` n `65` status `ready` deltaP `23.6111` edge `0.1213` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.931` n `104` status `ready` deltaP `13.3208` edge `0.2352` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8731` n `65` status `ready` deltaP `31.6088` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5072` n `65` status `ready` deltaP `20.272` edge `0.1348` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4281` n `65` status `ready` deltaP `9.7167` edge `0.1731` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0602` n `65` status `ready` deltaP `25.4675` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.927` n `65` status `ready` deltaP `17.8588` edge `0.0831` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2237` n `104` status `ready` deltaP `22.8659` edge `0.0252` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1001` n `65` status `ready` deltaP `3.3717` edge `0.1211` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.9005` n `116` status `ready` deltaP `10.8043` edge `0.0919` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5671` n `65` status `ready` deltaP `25.0855` edge `0.1086` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4885` n `116` status `ready` deltaP `12.962` edge `0.0046` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.3107` n `73` status `ready` deltaP `5.225` edge `0.0113` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
