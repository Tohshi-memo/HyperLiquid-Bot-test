# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T15:07:30.614525+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4119`

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

- `market_context_high->unknown_4h` score `158.8181` n `36` status `ready` deltaP `-6.9444` edge `13.3205` maxDD `-0.8159`
- `market_context_high->fx_4h` score `3.4008` n `36` status `ready` deltaP `36.8224` edge `0.0469` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1227` n `37` status `ready` deltaP `9.0104` edge `0.2461` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.986` n `36` status `ready` deltaP `25.9824` edge `0.0393` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.2774` n `54` status `ready` deltaP `5.9028` edge `0.0892` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8628` n `54` status `ready` deltaP `6.7976` edge `0.1392` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.668` n `37` status `ready` deltaP `9.0023` edge `0.0542` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.532` n `37` status `ready` deltaP `8.4197` edge `0.0153` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.4231` n `54` status `ready` deltaP `12.0935` edge `0.0214` maxDD `-0.4888`
- `market_context_high->crypto_alt_1h` score `0.4031` n `37` status `ready` deltaP `10.7987` edge `0.0612` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2107` n `54` status `ready` deltaP `7.2338` edge `0.1456` maxDD `-6.6786`
- `market_context_high->commodity_1h` score `0.135` n `37` status `ready` deltaP `9.3179` edge `0.0098` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0847` n `36` status `ready` deltaP `4.9458` edge `0.0233` maxDD `-1.633`
- `news_risk_high->fx_4h` score `0.084` n `54` status `ready` deltaP `7.1928` edge `0.0067` maxDD `-0.1772`
- `news_risk_high->index_1h` score `0.0799` n `54` status `ready` deltaP `7.8565` edge `0.0032` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0832` n `37` status `ready` deltaP `0.9023` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1813` n `54` status `ready` deltaP `1.8131` edge `0.0032` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.2019` n `54` status `ready` deltaP `-2.301` edge `0.0444` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.805` n `36` status `ready` deltaP `21.6124` edge `0.0807` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
