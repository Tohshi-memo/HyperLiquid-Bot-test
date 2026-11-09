# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T00:07:25.849867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6537`

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

- `market_context_high->unknown_4h` score `8.5711` n `49` status `ready` deltaP `-0.7777` edge `0.7642` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.5204` n `37` status `ready` deltaP `11.2472` edge `0.7312` maxDD `-31.3588`
- `market_context_high->index_24h` score `1.1933` n `37` status `ready` deltaP `15.0385` edge `0.1158` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.9225` n `37` status `ready` deltaP `11.1158` edge `0.0116` maxDD `-0.0397`
- `market_context_high->fx_4h` score `0.4158` n `49` status `ready` deltaP `12.4347` edge `0.0257` maxDD `-0.4229`
- `market_context_high->commodity_4h` score `0.1976` n `49` status `ready` deltaP `4.5514` edge `0.0404` maxDD `-1.633`
- `market_context_high->equity_1h` score `0.1231` n `61` status `ready` deltaP `2.4664` edge `0.1145` maxDD `-5.2128`
- `market_context_high->metal_1h` score `0.118` n `61` status `ready` deltaP `4.5475` edge `0.0123` maxDD `-0.6226`
- `market_context_high->commodity_1h` score `0.0279` n `61` status `ready` deltaP `7.3623` edge `0.0091` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.0068` n `49` status `ready` deltaP `10.1574` edge `0.0135` maxDD `-2.4279`
- `market_context_high->commodity_24h` score `-0.2169` n `37` status `ready` deltaP `2.2195` edge `0.0769` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.4346` n `61` status `ready` deltaP `-2.4517` edge `0.0188` maxDD `-0.6537`
- `market_context_high->fx_1h` score `-0.5368` n `61` status `ready` deltaP `-5.6101` edge `0.0048` maxDD `-0.2309`
- `market_context_high->metal_4h` score `-1.3269` n `49` status `ready` deltaP `-3.6368` edge `-0.0338` maxDD `-1.2025`
- `market_context_high->crypto_alt_1h` score `-1.4808` n `61` status `ready` deltaP `3.3793` edge `-0.0231` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.5108` n `37` status `ready` deltaP `8.2208` edge `-0.1254` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-2.2391` n `61` status `ready` deltaP `-0.5056` edge `-0.0738` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-4.356` n `49` status `ready` deltaP `9.5819` edge `-0.0739` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-7.7653` n `49` status `ready` deltaP `5.7212` edge `-0.3111` maxDD `-25.2652`
- `market_context_high->crypto_major_24h` score `-8.2501` n `37` status `ready` deltaP `-9.0841` edge `-0.1509` maxDD `-32.0839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
