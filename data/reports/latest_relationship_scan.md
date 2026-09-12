# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T19:07:25.563894+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12779`

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

- `market_context_high->unknown_24h` score `9430.3517` n `79` status `ready` deltaP `12.9198` edge `785.7817` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `7151.7745` n `39` status `ready` deltaP `15.4514` edge `595.8782` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `7151.7745` n `39` status `ready` deltaP `15.4514` edge `595.8782` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.4903` n `82` status `ready` deltaP `-5.2505` edge `32.0347` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `20.6699` n `69` status `ready` deltaP `45.9768` edge `1.5356` maxDD `-6.9028`
- `news_risk_high->crypto_alt_24h` score `17.1784` n `69` status `ready` deltaP `29.8837` edge `1.2811` maxDD `-2.2369`
- `risk_on_high->crypto_alt_24h` score `15.8057` n `39` status `ready` deltaP `37.3531` edge `1.0911` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `15.8057` n `39` status `ready` deltaP `37.3531` edge `1.0911` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.9516` n `79` status `ready` deltaP `29.9204` edge `1.0459` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.9136` n `39` status `ready` deltaP `41.8403` edge `0.5472` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.9136` n `39` status `ready` deltaP `41.8403` edge `0.5472` maxDD `0.0`
- `market_context_high->equity_24h` score `9.5284` n `79` status `ready` deltaP `41.8403` edge `0.5151` maxDD `0.0`
- `news_risk_high->equity_24h` score `9.2383` n `69` status `ready` deltaP `24.449` edge `0.6876` maxDD `-3.1258`
- `risk_on_high->crypto_alt_4h` score `7.4632` n `47` status `ready` deltaP `36.0145` edge `0.419` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.4632` n `47` status `ready` deltaP `36.0145` edge `0.419` maxDD `-1.9733`
- `news_risk_high->index_24h` score `6.6973` n `69` status `ready` deltaP `43.9009` edge `0.2831` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `6.4136` n `69` status `ready` deltaP `40.7759` edge `0.3067` maxDD `-0.526`
- `risk_on_high->index_24h` score `4.9202` n `39` status `ready` deltaP `49.2521` edge `0.0859` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.9202` n `39` status `ready` deltaP `49.2521` edge `0.0859` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `3.3102` n `47` status `ready` deltaP `28.7104` edge `0.1021` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
