# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T13:52:27.291857+00:00`
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

- `market_context_high->equity_24h` score `4.1512` n `91` status `ready` deltaP `2.2684` edge `0.6368` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7732` n `91` status `ready` deltaP `9.7337` edge `0.2238` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4228` n `103` status `ready` deltaP `13.5241` edge `0.0957` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.4212` n `91` status `ready` deltaP `31.1508` edge `0.0612` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9674` n `103` status `ready` deltaP `11.2377` edge `0.04` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3926` n `91` status `ready` deltaP `5.5155` edge `0.1667` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4053` n `103` status `ready` deltaP `4.0478` edge `0.0221` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5094` n `103` status `ready` deltaP `1.9054` edge `-0.0056` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5852` n `103` status `ready` deltaP `-0.6616` edge `-0.0101` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8443` n `103` status `ready` deltaP `1.4799` edge `-0.0049` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0565` n `103` status `ready` deltaP `-3.2204` edge `-0.0131` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.8383` n `103` status `ready` deltaP `3.3507` edge `-0.0418` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9301` n `103` status `ready` deltaP `-10.8787` edge `-0.0254` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4289` n `103` status `ready` deltaP `-7.735` edge `-0.0512` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.8905` n `91` status `ready` deltaP `3.2013` edge `-0.1425` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.3924` n `91` status `ready` deltaP `-17.5671` edge `-0.1735` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.1432` n `103` status `ready` deltaP `-11.0363` edge `-0.1065` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.7879` n `103` status `ready` deltaP `-13.644` edge `-0.2189` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
