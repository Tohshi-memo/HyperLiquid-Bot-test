# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T10:37:42.706044+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `2.6794` n `112` status `ready` deltaP `21.627` edge `0.7229` maxDD `-35.8856`
- `news_risk_high->crypto_alt_4h` score `0.7756` n `134` status `ready` deltaP `7.9769` edge `0.2425` maxDD `-10.6996`
- `news_risk_high->fx_1h` score `-0.519` n `146` status `ready` deltaP `0.9208` edge `-0.0026` maxDD `-0.6065`
- `news_risk_high->crypto_alt_1h` score `-0.547` n `146` status `ready` deltaP `1.2837` edge `0.0441` maxDD `-5.8225`
- `news_risk_high->metal_24h` score `-0.8387` n `112` status `ready` deltaP `13.4672` edge `0.1283` maxDD `-14.0483`
- `news_risk_high->index_1h` score `-1.1395` n `146` status `ready` deltaP `-1.1976` edge `-0.007` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.2821` n `146` status `ready` deltaP `-4.9483` edge `-0.0092` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3272` n `134` status `ready` deltaP `-4.8144` edge `-0.0129` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.2841` n `134` status `ready` deltaP `-5.151` edge `-0.0284` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.3536` n `112` status `ready` deltaP `-17.2619` edge `-0.0158` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.4056` n `146` status `ready` deltaP `-8.777` edge `-0.0053` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-2.8762` n `134` status `ready` deltaP `-2.8736` edge `-0.0291` maxDD `-9.3056`
- `news_risk_high->equity_1h` score `-2.9837` n `146` status `ready` deltaP `-8.133` edge `-0.0607` maxDD `-16.4088`
- `news_risk_high->index_24h` score `-3.1981` n `112` status `ready` deltaP `-13.3681` edge `-0.0367` maxDD `-7.402`
- `news_risk_high->crypto_major_1h` score `-3.359` n `146` status `ready` deltaP `-8.9041` edge `-0.048` maxDD `-9.4709`
- `news_risk_high->commodity_4h` score `-3.9227` n `134` status `ready` deltaP `-13.0642` edge `-0.0166` maxDD `-8.5225`
- `news_risk_high->equity_24h` score `-6.1418` n `112` status `ready` deltaP `4.4395` edge `0.1925` maxDD `-67.0937`
- `news_risk_high->crypto_major_4h` score `-7.2983` n `134` status `ready` deltaP `-14.3474` edge `-0.1106` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5513` n `134` status `ready` deltaP `-3.9475` edge `-0.2339` maxDD `-52.2214`
- `news_risk_high->commodity_24h` score `-10.7057` n `112` status `ready` deltaP `-25.3721` edge `-0.1359` maxDD `-24.6342`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
