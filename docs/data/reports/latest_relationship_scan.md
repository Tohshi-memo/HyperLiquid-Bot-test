# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T04:52:19.556284+00:00`
- Price records: `672`
- Market context records: `1702`
- Flow alert records: `6806`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->unknown_24h` score `8.6451` n `139` status `ready` deltaP `18.7748` edge `1.1273` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.3762` n `139` status `ready` deltaP `25.3578` edge `0.6049` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.9852` n `195` status `ready` deltaP `21.3376` edge `0.5396` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9601` n `195` status `ready` deltaP `22.5437` edge `0.4506` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.7816` n `139` status `ready` deltaP `16.6251` edge `0.3421` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.0023` n `195` status `ready` deltaP `16.0858` edge `0.2524` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.6913` n `139` status `ready` deltaP `15.4775` edge `0.5276` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7794` n `197` status `ready` deltaP `7.1127` edge `0.1199` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4388` n `195` status `ready` deltaP `7.8392` edge `0.0932` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.3704` n `139` status `ready` deltaP `23.8468` edge `1.0528` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1342` n `197` status `ready` deltaP `4.9067` edge `0.0861` maxDD `-3.9439`
- `market_context_high->equity_1h` score `-0.0172` n `197` status `ready` deltaP `4.203` edge `0.0514` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.4592` n `195` status `ready` deltaP `12.6469` edge `0.126` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.5335` n `197` status `ready` deltaP `0.3177` edge `0.0166` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6231` n `197` status `ready` deltaP `5.5055` edge `0.017` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6612` n `197` status `ready` deltaP `-2.8572` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8621` n `139` status `ready` deltaP `4.3601` edge `0.004` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.8676` n `139` status `ready` deltaP `22.0433` edge `0.6004` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.8764` n `195` status `ready` deltaP `-7.6016` edge `-0.0128` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1332` n `197` status `ready` deltaP `0.1299` edge `-0.0289` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
