# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T03:37:23.977901+00:00`
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

- `news_risk_high->crypto_major_4h` score `9.1225` n `65` status `ready` deltaP `31.7894` edge `0.5686` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `6.5844` n `88` status `ready` deltaP `16.9478` edge `0.5381` maxDD `-4.8575`
- `news_risk_high->crypto_alt_4h` score `5.5482` n `65` status `ready` deltaP `19.3293` edge `0.4679` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5828` n `65` status `ready` deltaP `11.0283` edge `0.235` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.252` n `65` status `ready` deltaP `22.6804` edge `0.1198` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5512` n `65` status `ready` deltaP `28.5601` edge `0.0484` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4018` n `65` status `ready` deltaP `9.2676` edge `0.1739` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.0131` n `117` status `ready` deltaP `11.2766` edge `0.189` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0087` n `65` status `ready` deltaP `25.0184` edge `0.0156` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8475` n `65` status `ready` deltaP `16.6135` edge `0.103` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.7234` n `65` status `ready` deltaP `16.3345` edge `0.0763` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `1.4818` n `88` status `ready` deltaP `16.8307` edge `0.1829` maxDD `-10.3962`
- `market_context_high->fx_4h` score `1.3693` n `117` status `ready` deltaP `24.686` edge `0.0252` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.3121` n `117` status `ready` deltaP `17.2113` edge `0.0646` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.1552` n `65` status `ready` deltaP `3.9705` edge `0.1217` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9827` n `117` status `ready` deltaP `15.5369` edge `0.0067` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7082` n `117` status `ready` deltaP `11.756` edge `0.0203` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.5179` n `88` status `ready` deltaP `20.8646` edge `0.0648` maxDD `-5.6663`
- `news_risk_high->commodity_24h` score `0.1113` n `65` status `ready` deltaP `24.885` edge `0.0515` maxDD `-10.9169`
- `news_risk_high->metal_1h` score `0.0698` n `65` status `ready` deltaP `5.7669` edge `0.0092` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
