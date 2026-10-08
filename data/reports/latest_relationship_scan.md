# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T04:37:29.596353+00:00`
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

- `market_context_high->unknown_4h` score `38.8066` n `90` status `ready` deltaP `-3.4398` edge `3.3107` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `11.0022` n `62` status `ready` deltaP `38.8153` edge `0.6784` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1347` n `62` status `ready` deltaP `23.0201` edge `0.5755` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.5456` n `62` status `ready` deltaP `16.519` edge `0.4453` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.9439` n `62` status `ready` deltaP `35.924` edge `0.1725` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.4972` n `90` status `ready` deltaP `11.0017` edge `0.8006` maxDD `-16.7906`
- `news_risk_high->index_4h` score `3.0786` n `62` status `ready` deltaP `33.4586` edge `0.0597` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.4973` n `90` status `ready` deltaP `16.8798` edge `0.192` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.4923` n `62` status `ready` deltaP `10.1748` edge `0.1754` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4197` n `62` status `ready` deltaP `18.6356` edge `0.1372` maxDD `-2.7837`
- `market_context_high->equity_24h` score `2.0411` n `90` status `ready` deltaP `14.0817` edge `0.1191` maxDD `-1.0977`
- `news_risk_high->index_1h` score `2.0128` n `62` status `ready` deltaP `25.1739` edge `0.0149` maxDD `-0.1997`
- `news_risk_high->unknown_4h` score `1.5862` n `62` status `ready` deltaP `-6.4148` edge `0.2995` maxDD `-5.6309`
- `news_risk_high->metal_4h` score `1.447` n `62` status `ready` deltaP `21.0144` edge `0.087` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.2377` n `90` status `ready` deltaP `21.5371` edge `0.1636` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.161` n `62` status `ready` deltaP `3.3079` edge `0.1266` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0525` n `90` status `ready` deltaP `21.5829` edge `0.0185` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7118` n `90` status `ready` deltaP `11.9461` edge `0.0039` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.1655` n `90` status `ready` deltaP `7.3691` edge `0.5659` maxDD `-34.5048`
- `market_context_high->crypto_major_1h` score `0.1549` n `90` status `ready` deltaP `10.1031` edge `0.0414` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
