# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T09:52:24.725899+00:00`
- Price records: `672`
- Market context records: `2031`
- Flow alert records: `7737`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8763` n `205` status `ready` deltaP `30.7927` edge `0.5874` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3682` n `205` status `ready` deltaP `24.5427` edge `0.6482` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8919` n `205` status `ready` deltaP `18.8414` edge `0.4403` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0167` n `205` status `ready` deltaP `17.2561` edge `0.2458` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.532` n `205` status `ready` deltaP `12.4777` edge `0.1431` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4498` n `205` status `ready` deltaP `12.9269` edge `0.103` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2809` n `205` status `ready` deltaP `10.2322` edge `0.1499` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.9612` n `200` status `ready` deltaP `16.8356` edge `0.4999` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.4331` n `200` status `ready` deltaP `15.8904` edge `0.42` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.2886` n `200` status `ready` deltaP `4.2877` edge `0.1183` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.1948` n `205` status `ready` deltaP `6.7607` edge `0.05` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `-0.0118` n `205` status `ready` deltaP `3.5965` edge `0.047` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2882` n `205` status `ready` deltaP `2.7034` edge `0.017` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4784` n `200` status `ready` deltaP `10.9863` edge `0.0225` maxDD `-2.5156`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9186` n `205` status `ready` deltaP `3.5088` edge `0.0188` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1618` n `205` status `ready` deltaP `8.872` edge `0.1063` maxDD `-11.9812`
- `market_context_high->metal_24h` score `-1.4026` n `200` status `ready` deltaP `10.0616` edge `0.1398` maxDD `-19.2339`
- `market_context_high->fx_4h` score `-1.6109` n `205` status `ready` deltaP `-6.5854` edge `-0.0022` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8099` n `205` status `ready` deltaP `3.0546` edge `0.0034` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
