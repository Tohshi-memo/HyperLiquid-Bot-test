# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T15:37:31.026052+00:00`
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

- `market_context_high->unknown_4h` score `39.997` n `149` status `ready` deltaP `-0.4634` edge `3.3595` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `15.7946` n `37` status `ready` deltaP `25.7742` edge `1.2823` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `13.8757` n `52` status `ready` deltaP `-7.704` edge `1.2302` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.8757` n `52` status `ready` deltaP `-7.704` edge `1.2302` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6582` n `52` status `ready` deltaP `48.4375` edge `0.3986` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6582` n `52` status `ready` deltaP `48.4375` edge `0.3986` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3591` n `149` status `ready` deltaP `41.7261` edge `0.3876` maxDD `-0.8682`
- `news_risk_high->crypto_major_24h` score `5.4938` n `37` status `ready` deltaP `-7.5263` edge `0.954` maxDD `-13.2931`
- `news_risk_high->crypto_alt_4h` score `3.1439` n `95` status `ready` deltaP `21.0349` edge `0.4779` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.7375` n `52` status `ready` deltaP `32.235` edge `0.0482` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7375` n `52` status `ready` deltaP `32.235` edge `0.0482` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6372` n `149` status `ready` deltaP `28.7373` edge `0.07` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.0798` n `149` status `ready` deltaP `15.9115` edge `0.0216` maxDD `-0.3491`
- `news_risk_high->equity_4h` score `0.7122` n `95` status `ready` deltaP `12.6861` edge `0.1009` maxDD `-4.1995`
- `risk_on_high->fx_24h` score `0.6355` n `52` status `ready` deltaP `15.9588` edge `-0.0492` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.6355` n `52` status `ready` deltaP `15.9588` edge `-0.0492` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.5006` n `149` status `ready` deltaP `13.1839` edge `-0.0246` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4565` n `52` status `ready` deltaP `8.9936` edge `0.0133` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4565` n `52` status `ready` deltaP `8.9936` edge `0.0133` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.3567` n `95` status `ready` deltaP `10.5893` edge `0.0273` maxDD `-1.8403`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
