# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T08:37:27.215309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5970`

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

- `market_context_high->unknown_4h` score `42.6171` n `85` status `ready` deltaP `-12.9484` edge `3.6958` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5175` n `67` status `ready` deltaP `37.2616` edge `0.5876` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.1379` n `67` status `ready` deltaP `10.1912` edge `1.162` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.6217` n `85` status `ready` deltaP `22.7259` edge `0.012` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.5933` n `67` status `ready` deltaP `14.5626` edge `0.109` maxDD `-1.4011`
- `market_context_high->fx_1h` score `0.1645` n `97` status `ready` deltaP `6.4665` edge `0.0022` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.0182` n `85` status `ready` deltaP `7.1934` edge `0.0069` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.0665` n `97` status `ready` deltaP `2.5094` edge `0.007` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.3806` n `97` status `ready` deltaP `1.3797` edge `0.0309` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.4742` n `97` status `ready` deltaP `-0.3997` edge `0.0014` maxDD `-0.7626`
- `market_context_high->crypto_major_4h` score `-0.5371` n `85` status `ready` deltaP `2.4606` edge `0.1171` maxDD `-10.5224`
- `market_context_high->fx_24h` score `-0.6801` n `67` status `ready` deltaP `5.5711` edge `0.007` maxDD `-1.5065`
- `market_context_high->metal_24h` score `-0.9574` n `67` status `ready` deltaP `-3.2468` edge `0.0474` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.9718` n `97` status `ready` deltaP `-4.3907` edge `0.0206` maxDD `-4.9401`
- `market_context_high->index_4h` score `-1.2606` n `85` status `ready` deltaP `-10.3049` edge `0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.5695` n `97` status `ready` deltaP `-6.2689` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.624` n `97` status `ready` deltaP `-6.221` edge `-0.0069` maxDD `-2.2898`
- `market_context_high->metal_4h` score `-1.7522` n `85` status `ready` deltaP `-10.6761` edge `0.0141` maxDD `-1.1153`
- `market_context_high->crypto_alt_24h` score `-1.9663` n `67` status `ready` deltaP `-4.4932` edge `0.3891` maxDD `-35.5652`
- `market_context_high->equity_4h` score `-2.7266` n `85` status `ready` deltaP `-9.1912` edge `-0.0067` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
