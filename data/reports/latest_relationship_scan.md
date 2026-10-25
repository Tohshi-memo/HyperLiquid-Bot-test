# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T01:36:03.555693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7250`

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

- `market_context_high->unknown_4h` score `21.5409` n `95` status `ready` deltaP `0.8408` edge `1.823` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.5896` n `52` status `ready` deltaP `21.3408` edge `0.0811` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.6684` n `95` status `ready` deltaP `9.2891` edge `0.05` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2278` n `107` status `ready` deltaP `3.1171` edge `0.0103` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.2898` n `107` status `ready` deltaP `-0.6128` edge `0.0024` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.6729` n `95` status `ready` deltaP `-4.4977` edge `0.0041` maxDD `-0.4972`
- `market_context_high->metal_1h` score `-0.9244` n `107` status `ready` deltaP `1.1836` edge `-0.0055` maxDD `-1.6873`
- `market_context_high->index_1h` score `-0.9633` n `107` status `ready` deltaP `-1.2116` edge `-0.007` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.3517` n `52` status `ready` deltaP `-3.2852` edge `-0.0017` maxDD `-1.4567`
- `market_context_high->crypto_major_1h` score `-1.5178` n `107` status `ready` deltaP `1.4746` edge `-0.0332` maxDD `-10.3646`
- `market_context_high->crypto_major_24h` score `-1.735` n `52` status `ready` deltaP `2.4706` edge `-0.0136` maxDD `-13.358`
- `market_context_high->equity_1h` score `-2.6041` n `107` status `ready` deltaP `-1.1347` edge `-0.0934` maxDD `-12.6316`
- `market_context_high->metal_4h` score `-3.1026` n `95` status `ready` deltaP `-7.4021` edge `-0.0314` maxDD `-5.8908`
- `market_context_high->metal_24h` score `-3.1651` n `52` status `ready` deltaP `-10.1362` edge `0.0034` maxDD `-6.9668`
- `market_context_high->crypto_alt_1h` score `-3.3234` n `107` status `ready` deltaP `-0.277` edge `-0.0591` maxDD `-14.2805`
- `market_context_high->index_4h` score `-4.6448` n `95` status `ready` deltaP `-20.7734` edge `-0.0515` maxDD `-5.0996`
- `market_context_high->crypto_alt_24h` score `-5.7809` n `52` status `ready` deltaP `5.5823` edge `-0.1623` maxDD `-42.9511`
- `market_context_high->index_24h` score `-7.51` n `52` status `ready` deltaP `-37.2329` edge `-0.1799` maxDD `-6.4838`
- `market_context_high->unknown_1h` score `-8.0233` n `107` status `ready` deltaP `-0.1973` edge `-0.6184` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-12.512` n `95` status `ready` deltaP `-20.9258` edge `-0.3077` maxDD `-40.9703`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
