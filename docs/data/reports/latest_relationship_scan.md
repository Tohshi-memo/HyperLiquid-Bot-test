# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T06:22:30.223985+00:00`
- Price records: `672`
- Market context records: `4181`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10082`

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

- `risk_on_high->unknown_4h` score `144.8028` n `40` status `ready` deltaP `-9.878` edge `12.3146` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.8028` n `40` status `ready` deltaP `-9.878` edge `12.3146` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.0439` n `202` status `ready` deltaP `0.6417` edge `3.074` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.8037` n `202` status `ready` deltaP `-4.5067` edge `1.39` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.5562` n `198` status `ready` deltaP `-13.0672` edge `1.2035` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.0057` n `40` status `ready` deltaP `3.374` edge `0.3728` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.0057` n `40` status `ready` deltaP `3.374` edge `0.3728` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.7483` n `40` status `ready` deltaP `31.0366` edge `-0.0565` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.7483` n `40` status `ready` deltaP `31.0366` edge `-0.0565` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.5092` n `40` status `ready` deltaP `13.9634` edge `0.0159` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5092` n `40` status `ready` deltaP `13.9634` edge `0.0159` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `0.1031` n `40` status `ready` deltaP `10.2439` edge `0.004` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1031` n `40` status `ready` deltaP `10.2439` edge `0.004` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0934` n `40` status `ready` deltaP `5.0` edge `0.0016` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0934` n `40` status `ready` deltaP `5.0` edge `0.0016` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.0537` n `40` status `ready` deltaP `8.811` edge `-0.0183` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0537` n `40` status `ready` deltaP `8.811` edge `-0.0183` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `-0.0441` n `40` status `ready` deltaP `8.8174` edge `-0.0235` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0441` n `40` status `ready` deltaP `8.8174` edge `-0.0235` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `-0.0689` n `40` status `ready` deltaP `8.5629` edge `-0.0117` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
