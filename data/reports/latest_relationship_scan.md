# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T05:52:25.912003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4180`

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

- `news_risk_high->equity_4h` score `1.3198` n `62` status `ready` deltaP `12.7508` edge `0.1581` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.8786` n `62` status `ready` deltaP `14.9095` edge `0.0216` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3731` n `62` status `ready` deltaP `10.103` edge `0.1473` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `0.1689` n `62` status `ready` deltaP `-1.3553` edge `0.0673` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.1018` n `62` status `ready` deltaP `8.248` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.1002` n `62` status `ready` deltaP `-0.7485` edge `0.0471` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.1807` n `62` status `ready` deltaP `1.9606` edge `0.0023` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.3038` n `62` status `ready` deltaP `0.2901` edge `0.0037` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5797` n `62` status `ready` deltaP `-4.7228` edge `-0.0071` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.0719` n `62` status `ready` deltaP `-0.8655` edge `-0.0411` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.232` n `62` status `ready` deltaP `-2.5932` edge `-0.0251` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2808` n `62` status `ready` deltaP `-3.1619` edge `0.0173` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.5691` n `62` status `ready` deltaP `-10.875` edge `-0.0023` maxDD `-1.1434`
- `news_risk_high->crypto_major_1h` score `-1.9523` n `62` status `ready` deltaP `-7.881` edge `-0.0284` maxDD `-3.2066`
- `news_risk_high->crypto_alt_4h` score `-2.2639` n `62` status `ready` deltaP `-3.4667` edge `-0.0051` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.8147` n `62` status `ready` deltaP `-5.9476` edge `-0.2598` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.5433` n `62` status `ready` deltaP `-31.432` edge `-0.0119` maxDD `-3.9061`
- `news_risk_high->equity_24h` score `-4.7833` n `62` status `ready` deltaP `20.5197` edge `0.4086` maxDD `-86.0244`
- `news_risk_high->commodity_24h` score `-10.6671` n `62` status `ready` deltaP `-28.9651` edge `-0.1298` maxDD `-27.9483`
- `news_risk_high->crypto_major_24h` score `-14.5207` n `62` status `ready` deltaP `-31.4908` edge `-0.1498` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
