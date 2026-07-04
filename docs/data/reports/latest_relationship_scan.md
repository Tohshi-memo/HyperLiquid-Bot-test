# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T01:52:25.816105+00:00`
- Price records: `672`
- Market context records: `5616`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8757`

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

- `market_context_high->equity_24h` score `3.1591` n `174` status `ready` deltaP `15.0084` edge `0.6711` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3148` n `174` status `ready` deltaP `22.1325` edge `0.0594` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.2636` n `228` status `ready` deltaP `13.1017` edge `0.2472` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `0.5615` n `228` status `ready` deltaP `7.8413` edge `0.1586` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4152` n `228` status `ready` deltaP `6.3543` edge `0.1561` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2961` n `237` status `ready` deltaP `1.2999` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3235` n `237` status `ready` deltaP `5.9148` edge `0.0343` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5083` n `237` status `ready` deltaP `0.2924` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5438` n `237` status `ready` deltaP `4.7298` edge `0.0477` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5901` n `237` status `ready` deltaP `1.2867` edge `0.0384` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9046` n `237` status `ready` deltaP `0.878` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1387` n `237` status `ready` deltaP `-1.7762` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2942` n `228` status `ready` deltaP `1.3372` edge `0.0069` maxDD `-1.2061`
- `market_context_high->index_4h` score `-1.7412` n `228` status `ready` deltaP `0.7836` edge `0.0106` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-2.2357` n `174` status `ready` deltaP `8.4172` edge `0.2116` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3886` n `174` status `ready` deltaP `10.0874` edge `0.0252` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8455` n `228` status `ready` deltaP `-10.8526` edge `-0.0541` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1262` n `228` status `ready` deltaP `-5.3247` edge `-0.0408` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2795` n `174` status `ready` deltaP `-10.9315` edge `-0.2525` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.1342` n `174` status `ready` deltaP `-1.796` edge `-0.1295` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
