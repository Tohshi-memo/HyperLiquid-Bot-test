# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T12:07:30.323770+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `40.0044` n `149` status `ready` deltaP `-0.311` edge `3.3591` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.8831` n `52` status `ready` deltaP `-7.5516` edge `1.2298` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8831` n `52` status `ready` deltaP `-7.5516` edge `1.2298` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8883` n `52` status `ready` deltaP `50.1736` edge `0.4062` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8883` n `52` status `ready` deltaP `50.1736` edge `0.4062` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5891` n `149` status `ready` deltaP `43.4622` edge `0.3952` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1458` n `92` status `ready` deltaP `20.7715` edge `0.4799` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8231` n `52` status `ready` deltaP `32.5399` edge `0.0533` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8231` n `52` status `ready` deltaP `32.5399` edge `0.0533` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7228` n `149` status `ready` deltaP `29.0422` edge `0.0751` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.1193` n `149` status `ready` deltaP `16.2109` edge `0.0229` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.9173` n `92` status `ready` deltaP `13.408` edge `0.1119` maxDD `-3.3619`
- `risk_on_high->fx_24h` score `0.8174` n `52` status `ready` deltaP `17.3477` edge `-0.0433` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.8174` n `52` status `ready` deltaP `17.3477` edge `-0.0433` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.6825` n `149` status `ready` deltaP `14.5728` edge `-0.0187` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.496` n `52` status `ready` deltaP `9.293` edge `0.0146` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.496` n `52` status `ready` deltaP `9.293` edge `0.0146` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3722` n `92` status `ready` deltaP `9.9417` edge `0.0261` maxDD `-0.2398`
- `news_risk_high->crypto_major_4h` score `0.3139` n `92` status `ready` deltaP `12.4933` edge `0.2816` maxDD `-19.972`
- `news_risk_high->equity_1h` score `0.2896` n `95` status `ready` deltaP `9.9905` edge `0.0227` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
