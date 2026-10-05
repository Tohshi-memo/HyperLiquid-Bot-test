# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T08:07:31.466802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8468`

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

- `market_context_high->unknown_1h` score `80.3921` n `119` status `ready` deltaP `0.7661` edge `6.7357` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `54.9207` n `107` status `ready` deltaP `1.6626` edge `4.5968` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.7249` n `76` status `ready` deltaP `29.5595` edge `0.7103` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3119` n `65` status `ready` deltaP `32.5516` edge `0.5793` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1774` n `76` status `ready` deltaP `24.7168` edge `0.4953` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7876` n `65` status `ready` deltaP `19.7866` edge `0.4848` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3433` n `65` status `ready` deltaP `23.6111` edge `0.1212` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.3078` n `65` status `ready` deltaP `12.249` edge `0.204` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.0922` n `107` status `ready` deltaP `14.0757` edge `0.2436` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.4854` n `65` status `ready` deltaP `20.1196` edge `0.134` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3993` n `65` status `ready` deltaP `9.567` edge `0.1717` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0339` n `65` status `ready` deltaP `25.1681` edge `0.0167` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9222` n `65` status `ready` deltaP `17.8588` edge `0.0827` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2688` n `107` status `ready` deltaP `23.4599` edge `0.025` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0534` n `65` status `ready` deltaP `3.0723` edge `0.1192` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `1.0182` n `119` status `ready` deltaP `11.4804` edge `0.0972` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5734` n `65` status `ready` deltaP `25.0855` edge `0.1094` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4827` n `119` status `ready` deltaP `12.8654` edge `0.0045` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.2163` n `76` status `ready` deltaP `5.2449` edge `0.0033` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
