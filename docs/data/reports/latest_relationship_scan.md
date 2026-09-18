# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T10:37:30.590605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8380`

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

- `market_context_high->unknown_4h` score `39.6` n `149` status `ready` deltaP `-0.311` edge `3.3254` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.4787` n `52` status `ready` deltaP `-7.5516` edge `1.1961` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4787` n `52` status `ready` deltaP `-7.5516` edge `1.1961` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8684` n `52` status `ready` deltaP `50.0` edge `0.4057` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8684` n `52` status `ready` deltaP `50.0` edge `0.4057` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5693` n `149` status `ready` deltaP `43.2886` edge `0.3947` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.0898` n `86` status `ready` deltaP `20.1893` edge `0.4766` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7192` n `149` status `ready` deltaP `29.0422` edge `0.0748` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.3177` n `86` status `ready` deltaP `17.1192` edge `0.1385` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1181` n `149` status `ready` deltaP `16.2109` edge `0.0228` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.9331` n `52` status `ready` deltaP `18.3894` edge `-0.0406` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.9331` n `52` status `ready` deltaP `18.3894` edge `-0.0406` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.7983` n `149` status `ready` deltaP `15.6145` edge `-0.016` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4948` n `52` status `ready` deltaP `9.293` edge `0.0145` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3461` n `86` status `ready` deltaP `9.5151` edge `0.0256` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.285` n `95` status `ready` deltaP `9.9905` edge `0.0221` maxDD `-1.8403`
- `market_context_high->fx_1h` score `-0.0682` n `149` status `ready` deltaP `2.556` edge `0.0` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
