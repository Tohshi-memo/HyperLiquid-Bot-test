# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T11:49:35.086286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `5.7933` n `83` status `ready` deltaP `2.4243` edge `0.7726` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7324` n `83` status `ready` deltaP `14.0144` edge `0.2752` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.5436` n `83` status `ready` deltaP `31.8482` edge `0.0639` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4276` n `103` status `ready` deltaP `13.5241` edge `0.0961` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1527` n `83` status `ready` deltaP `7.7059` edge `0.196` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9926` n `103` status `ready` deltaP `11.5371` edge `0.0401` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.4017` n `103` status `ready` deltaP `4.0478` edge `0.0224` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5772` n `103` status `ready` deltaP `-0.5091` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6646` n `103` status `ready` deltaP `-4.459` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8517` n `103` status `ready` deltaP `1.3275` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7607` n `103` status `ready` deltaP `3.9605` edge `-0.0394` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8451` n `103` status `ready` deltaP `-10.1302` edge `-0.0233` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.381` n `103` status `ready` deltaP `-7.2859` edge `-0.0502` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6039` n `83` status `ready` deltaP `7.3482` edge `-0.1334` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.725` n `83` status `ready` deltaP `-21.8039` edge `-0.1879` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.9568` n `103` status `ready` deltaP `-9.8168` edge `-0.0991` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.6136` n `103` status `ready` deltaP `-12.4245` edge `-0.2125` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
