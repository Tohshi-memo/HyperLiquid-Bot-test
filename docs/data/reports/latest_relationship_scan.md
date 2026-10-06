# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T02:22:28.882417+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7928`

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

- `news_risk_high->crypto_major_4h` score `9.0115` n `65` status `ready` deltaP `31.3321` edge `0.5624` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.576` n `83` status `ready` deltaP `21.4632` edge `0.6173` maxDD `-1.9912`
- `news_risk_high->crypto_alt_4h` score `5.3892` n `65` status `ready` deltaP `18.872` edge `0.4577` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `4.021` n `83` status `ready` deltaP `20.7634` edge `0.2714` maxDD `-3.9794`
- `news_risk_high->equity_24h` score `3.4968` n `65` status `ready` deltaP `10.5129` edge `0.2313` maxDD `-0.1325`
- `news_risk_high->index_24h` score `3.246` n `65` status `ready` deltaP `22.6804` edge `0.1193` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5524` n `65` status `ready` deltaP `28.5601` edge `0.0485` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4174` n `65` status `ready` deltaP `9.2676` edge `0.1752` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9848` n `65` status `ready` deltaP `24.719` edge `0.0156` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9021` n `117` status `ready` deltaP `10.8193` edge `0.1828` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.8737` n `65` status `ready` deltaP `16.6135` edge `0.1059` maxDD `-2.8413`
- `news_risk_high->metal_4h` score `1.721` n `65` status `ready` deltaP `16.3345` edge `0.0761` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4107` n `117` status `ready` deltaP `25.1434` edge `0.0256` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3109` n `117` status `ready` deltaP `17.2113` edge `0.0645` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2128` n `65` status `ready` deltaP `3.9705` edge `0.1265` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9947` n `117` status `ready` deltaP `15.6866` edge `0.0067` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7333` n `117` status `ready` deltaP `12.0554` edge `0.0204` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.5363` n `83` status `ready` deltaP `21.0822` edge `0.0657` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.1927` n `65` status `ready` deltaP `25.4005` edge `0.0585` maxDD `-10.9169`
- `news_risk_high->metal_1h` score `0.0542` n `65` status `ready` deltaP `5.6172` edge `0.0089` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
