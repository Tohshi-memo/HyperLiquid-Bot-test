# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T02:22:23.763000+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6569`

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

- `market_context_high->equity_24h` score `8.1211` n `34` status `ready` deltaP `15.2574` edge `0.8891` maxDD `-22.7914`
- `market_context_high->index_24h` score `1.205` n `34` status `ready` deltaP `14.8795` edge `0.1134` maxDD `-2.6491`
- `market_context_high->commodity_24h` score `1.1333` n `34` status `ready` deltaP `6.5768` edge `0.169` maxDD `-2.4036`
- `market_context_high->metal_1h` score `0.8994` n `67` status `ready` deltaP `10.8946` edge `0.0351` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.7472` n `34` status `ready` deltaP `11.009` edge `-0.0023` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.7008` n `67` status `ready` deltaP `3.8855` edge `0.1522` maxDD `-5.5762`
- `market_context_high->metal_4h` score `0.2122` n `55` status `ready` deltaP `6.6796` edge `0.0352` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.0757` n `55` status `ready` deltaP `-0.0166` edge `0.0453` maxDD `-1.1102`
- `market_context_high->index_4h` score `-0.1564` n `55` status `ready` deltaP `9.3902` edge `0.0102` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `-0.3414` n `67` status `ready` deltaP `3.423` edge `0.0075` maxDD `-1.7019`
- `market_context_high->index_1h` score `-0.4846` n `67` status `ready` deltaP `-0.4424` edge `0.0209` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.5789` n `67` status `ready` deltaP `10.4634` edge `0.0453` maxDD `-10.1421`
- `market_context_high->fx_4h` score `-0.6988` n `55` status `ready` deltaP `0.5598` edge `0.0053` maxDD `-0.8896`
- `market_context_high->fx_1h` score `-0.7134` n `67` status `ready` deltaP `-7.9229` edge `-0.0007` maxDD `-0.3682`
- `market_context_high->crypto_major_1h` score `-1.8292` n `67` status `ready` deltaP `2.6968` edge `-0.0426` maxDD `-11.7911`
- `market_context_high->metal_24h` score `-1.9587` n `34` status `ready` deltaP `4.1667` edge `-0.1357` maxDD `-1.4245`
- `market_context_high->equity_4h` score `-5.3108` n `55` status `ready` deltaP `4.2628` edge `-0.093` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.2397` n `34` status `ready` deltaP `-6.6993` edge `-0.0639` maxDD `-26.9129`
- `market_context_high->crypto_alt_4h` score `-9.1574` n `55` status `ready` deltaP `1.4329` edge `-0.2976` maxDD `-31.3386`
- `market_context_high->crypto_alt_24h` score `-11.1749` n `34` status `ready` deltaP `-20.0368` edge `-0.2646` maxDD `-35.9782`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
