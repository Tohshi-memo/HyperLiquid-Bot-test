# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T17:22:19.335206+00:00`
- Price records: `672`
- Market context records: `1443`
- Flow alert records: `6069`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `12.5717` n `154` status `ready` deltaP `28.7811` edge `1.0574` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1852` n `154` status `ready` deltaP `13.8979` edge `1.0895` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6192` n `154` status `ready` deltaP `27.3539` edge `0.8991` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.2333` n `154` status `ready` deltaP `19.3813` edge `0.3322` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.7155` n `154` status `ready` deltaP `12.5271` edge `0.4588` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3502` n `216` status `ready` deltaP `6.9162` edge `0.1494` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2255` n `154` status `ready` deltaP `10.5745` edge `0.0532` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1511` n `225` status `ready` deltaP `3.5117` edge `0.0105` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1714` n `225` status `ready` deltaP `2.0006` edge `0.0324` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.6371` n `216` status `ready` deltaP `0.2258` edge `0.0543` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6835` n `225` status `ready` deltaP `-0.6713` edge `0.009` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7237` n `225` status `ready` deltaP `0.7977` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.7496` n `225` status `ready` deltaP `1.2143` edge `0.0318` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.8274` n `216` status `ready` deltaP `9.7956` edge `0.1977` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0821` n `216` status `ready` deltaP `-4.7651` edge `-0.0099` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.2066` n `216` status `ready` deltaP `5.166` edge `0.1359` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.2178` n `225` status `ready` deltaP `4.7698` edge `0.0003` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.7465` n `225` status `ready` deltaP `-1.4478` edge `-0.0002` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.2902` n `216` status `ready` deltaP `6.6509` edge `0.034` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-2.7635` n `216` status `ready` deltaP `-10.6538` edge `-0.0286` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
