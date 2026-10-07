# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T13:37:41.968694+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_4h` score `36.2908` n `90` status `ready` deltaP `-5.8468` edge `3.1171` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.6521` n `62` status `ready` deltaP `36.6001` edge `0.664` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4678` n `62` status `ready` deltaP `24.1543` edge `0.5957` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.8765` n `62` status `ready` deltaP `27.9514` edge `0.1367` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.4366` n `62` status `ready` deltaP `8.8262` edge `0.2375` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0921` n `62` status `ready` deltaP `34.1365` edge `0.0563` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4768` n `62` status `ready` deltaP `10.0251` edge `0.1751` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3657` n `62` status `ready` deltaP `19.9105` edge `0.1242` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.1473` n `90` status `ready` deltaP `14.6646` edge `0.1776` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0654` n `62` status `ready` deltaP `25.9224` edge `0.0143` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.9171` n `90` status `ready` deltaP `6.9097` edge `0.4971` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.4632` n `62` status `ready` deltaP `20.4858` edge `0.0926` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3241` n `62` status `ready` deltaP `4.0564` edge `0.1352` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.7932` n `90` status `ready` deltaP `18.7771` edge `0.0156` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7525` n `90` status `ready` deltaP `12.5449` edge `0.0033` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7072` n `90` status `ready` deltaP `18.7152` edge `0.1144` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.218` n `62` status `ready` deltaP `7.4995` edge `0.01` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1448` n `90` status `ready` deltaP `9.9534` edge `0.0411` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.0601` n `62` status `ready` deltaP `24.244` edge `0.0027` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `-0.0418` n `90` status `ready` deltaP `-4.878` edge `0.2014` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
