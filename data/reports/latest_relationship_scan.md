# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T03:37:27.700238+00:00`
- Price records: `672`
- Market context records: `5942`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.7859` n `30` status `ready` deltaP `61.9792` edge `0.1523` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4824` n `30` status `ready` deltaP `39.2709` edge `0.2156` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6849` n `30` status `ready` deltaP `38.1707` edge `0.0572` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1052` n `30` status `ready` deltaP `25.4291` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5147` n `221` status `ready` deltaP `10.5852` edge `0.1651` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8902` n `30` status `ready` deltaP `10.9381` edge `0.0879` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2278` n `30` status `ready` deltaP `5.4691` edge `0.0389` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0966` n `224` status `ready` deltaP `6.0789` edge `0.0391` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2425` n `30` status `ready` deltaP `6.8055` edge `0.0107` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3271` n `224` status `ready` deltaP `3.5634` edge `0.0014` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4087` n `30` status `ready` deltaP `1.986` edge `-0.029` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.5401` n `224` status `ready` deltaP `1.489` edge `0.0056` maxDD `-0.7819`
- `market_context_high->commodity_1h` score `-0.5987` n `224` status `ready` deltaP `-3.2694` edge `-0.0034` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.7695` n `224` status `ready` deltaP `-1.9221` edge `-0.0011` maxDD `-0.6834`
- `market_context_high->crypto_major_1h` score `-0.7746` n `224` status `ready` deltaP `2.9619` edge `0.0273` maxDD `-7.3747`
- `market_context_high->crypto_alt_1h` score `-0.7903` n `224` status `ready` deltaP `2.3738` edge `0.024` maxDD `-7.2921`
- `market_context_high->equity_24h` score `-1.0248` n `213` status `ready` deltaP `18.1852` edge `0.255` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0766` n `30` status `ready` deltaP `-9.8503` edge `-0.0209` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.6817` n `221` status `ready` deltaP `-2.8611` edge `-0.0333` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6946` n `221` status `ready` deltaP `1.3974` edge `0.0182` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
