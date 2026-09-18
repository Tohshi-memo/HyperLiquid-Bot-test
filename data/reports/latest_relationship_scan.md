# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T15:52:31.784542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8528`

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

- `market_context_high->unknown_4h` score `40.0186` n `149` status `ready` deltaP `-0.4634` edge `3.3613` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `15.6439` n `37` status `ready` deltaP `25.6006` edge `1.2709` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.8973` n `52` status `ready` deltaP `-7.704` edge `1.232` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8973` n `52` status `ready` deltaP `-7.704` edge `1.232` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6371` n `52` status `ready` deltaP `48.2639` edge `0.398` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6371` n `52` status `ready` deltaP `48.2639` edge `0.398` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.338` n `149` status `ready` deltaP `41.5525` edge `0.387` maxDD `-0.8682`
- `news_risk_high->crypto_major_24h` score `5.3872` n `37` status `ready` deltaP `-7.6999` edge `0.9415` maxDD `-13.2931`
- `news_risk_high->crypto_alt_4h` score `3.0915` n `95` status `ready` deltaP `20.8825` edge `0.4722` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7339` n `52` status `ready` deltaP `32.235` edge `0.0479` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7339` n `52` status `ready` deltaP `32.235` edge `0.0479` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6336` n `149` status `ready` deltaP `28.7373` edge `0.0697` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0786` n `149` status `ready` deltaP `15.9115` edge `0.0215` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7107` n `95` status `ready` deltaP `12.6861` edge `0.1007` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6168` n `52` status `ready` deltaP `15.7852` edge `-0.0496` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6168` n `52` status `ready` deltaP `15.7852` edge `-0.0496` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.4819` n `149` status `ready` deltaP `13.0103` edge `-0.025` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4553` n `52` status `ready` deltaP `8.9936` edge `0.0132` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4553` n `52` status `ready` deltaP `8.9936` edge `0.0132` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.366` n `95` status `ready` deltaP `10.739` edge `0.0275` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
