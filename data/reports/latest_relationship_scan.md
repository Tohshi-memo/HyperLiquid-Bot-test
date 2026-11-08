# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T12:52:25.880654+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4735`

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

- `market_context_high->unknown_4h` score `69.1862` n `37` status `ready` deltaP `-4.5484` edge `5.8406` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.0921` n `37` status `ready` deltaP `15.4139` edge `0.8344` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3512` n `39` status `ready` deltaP `12.4367` edge `0.2423` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1327` n `37` status `ready` deltaP `33.7714` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.7957` n `32` status `ready` deltaP `32.9268` edge `0.022` maxDD `-0.016`
- `market_context_high->index_4h` score `2.1364` n `37` status `ready` deltaP `27.7274` edge `0.0402` maxDD `-2.4279`
- `news_risk_high->fx_1h` score `1.7741` n `32` status `ready` deltaP `22.137` edge `0.0093` maxDD `-0.0567`
- `market_context_high->crypto_alt_1h` score `1.1537` n `39` status `ready` deltaP `14.3636` edge `0.0819` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1261` n `39` status `ready` deltaP `12.1181` edge `0.0716` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8592` n `37` status `ready` deltaP `10.6982` edge `0.1019` maxDD `-2.7123`
- `market_context_high->commodity_24h` score `0.6996` n `37` status `ready` deltaP `6.7333` edge `0.1643` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.6902` n `37` status `ready` deltaP `10.9422` edge `-0.0066` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.4956` n `39` status `ready` deltaP `8.1146` edge `0.0143` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2013` n `39` status `ready` deltaP `2.33` edge `0.0373` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0808` n `39` status `ready` deltaP `8.2451` edge `0.01` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0639` n `32` status `ready` deltaP `7.2979` edge `0.002` maxDD `-0.2931`
- `market_context_high->commodity_4h` score `-0.0504` n `37` status `ready` deltaP `2.3773` edge `0.0231` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0674` n `39` status `ready` deltaP `1.2821` edge `0.0156` maxDD `-0.6226`
- `news_risk_high->equity_4h` score `-0.3105` n `32` status `ready` deltaP `-4.4207` edge `0.0775` maxDD `-4.2454`
- `news_risk_high->equity_1h` score `-0.4769` n `32` status `ready` deltaP `-5.3518` edge `0.0291` maxDD `-1.3653`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
