# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T06:22:35.122172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8827`

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

- `market_context_high->equity_24h` score `3.63` n `103` status `ready` deltaP `4.5729` edge `0.578` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7103` n `103` status `ready` deltaP `13.2535` edge `0.1951` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3425` n `139` status `ready` deltaP `15.8208` edge `0.0737` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8912` n `143` status `ready` deltaP `11.2904` edge `0.0333` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8172` n `103` status `ready` deltaP `21.575` edge `0.0476` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5524` n `103` status `ready` deltaP `9.1002` edge `0.1633` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2798` n `143` status `ready` deltaP `4.445` edge `-0.0034` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3255` n `139` status `ready` deltaP `7.5298` edge `-0.002` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.4712` n `143` status `ready` deltaP `-2.2915` edge `-0.0062` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.7111` n `143` status `ready` deltaP `-5.1871` edge `-0.007` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9852` n `143` status `ready` deltaP `-0.4868` edge `0.004` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9995` n `139` status `ready` deltaP `-1.8117` edge `-0.0107` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0429` n `139` status `ready` deltaP `-2.178` edge `-0.0183` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9576` n `143` status `ready` deltaP `-10.433` edge `-0.0294` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6344` n `139` status `ready` deltaP `-2.2207` edge `-0.071` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1855` n `143` status `ready` deltaP `-10.6874` edge `-0.062` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.2131` n `103` status `ready` deltaP `6.2197` edge `-0.0598` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.7293` n `139` status `ready` deltaP `-7.2195` edge `-0.097` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.6054` n `103` status `ready` deltaP `-12.4461` edge `-0.1565` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.9457` n `143` status `ready` deltaP `-6.0938` edge `-0.5768` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
