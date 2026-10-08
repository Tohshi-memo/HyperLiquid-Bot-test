# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T03:37:30.516738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.7208` n `90` status `ready` deltaP `-3.8965` edge `3.3066` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8538` n `62` status `ready` deltaP `38.2064` edge `0.6701` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9648` n `62` status `ready` deltaP `22.4113` edge `0.5654` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.3044` n `62` status `ready` deltaP `15.8282` edge `0.4298` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.8575` n `62` status `ready` deltaP `35.2332` edge `0.1699` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.377` n `90` status `ready` deltaP `10.6563` edge `0.7875` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0059` n `62` status `ready` deltaP `32.8497` edge `0.0577` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4796` n `62` status `ready` deltaP `10.256` edge `0.1738` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.349` n `90` status `ready` deltaP `16.2709` edge `0.1837` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2522` n `62` status `ready` deltaP `18.0267` edge `0.1273` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9771` n `62` status `ready` deltaP `24.8036` edge `0.0144` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.7998` n `90` status `ready` deltaP `13.3909` edge `0.1036` maxDD `-1.0977`
- `news_risk_high->unknown_4h` score `1.5004` n `62` status `ready` deltaP `-6.8715` edge `0.2954` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.4525` n `62` status `ready` deltaP `21.0144` edge `0.0877` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2401` n `90` status `ready` deltaP `21.5371` edge `0.1639` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0991` n `62` status `ready` deltaP `2.9389` edge `0.1239` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0926` n `90` status `ready` deltaP `22.0396` edge `0.0188` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7176` n `90` status `ready` deltaP `12.0179` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1467` n `90` status `ready` deltaP `10.1843` edge `0.0398` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1316` n `90` status `ready` deltaP `7.1964` edge `0.5627` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
