# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T22:32:45.091207+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `8.2059` n `81` status `ready` deltaP `7.1566` edge `0.9421` maxDD `-21.1456`
- `market_context_high->metal_24h` score `4.0273` n `81` status `ready` deltaP `13.831` edge `0.301` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7248` n `81` status `ready` deltaP `33.6034` edge `0.0671` maxDD `-1.9329`
- `market_context_high->index_24h` score `1.6686` n `81` status `ready` deltaP `11.7091` edge `0.2123` maxDD `-5.7715`
- `market_context_high->commodity_4h` score `1.4553` n `103` status `ready` deltaP `15.5058` edge `0.0852` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0967` n `103` status `ready` deltaP `13.1838` edge `0.0378` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.1572` n `103` status `ready` deltaP `6.2933` edge `0.0278` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4695` n `103` status `ready` deltaP `-2.885` edge `-0.0062` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5082` n `103` status `ready` deltaP `1.9054` edge `-0.0055` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5561` n `103` status `ready` deltaP `-0.3567` edge `-0.0084` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.593` n `103` status `ready` deltaP `-3.1117` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7326` n `103` status `ready` deltaP `2.547` edge `-0.0027` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9079` n `103` status `ready` deltaP `-0.7814` edge `-0.0103` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.3602` n `103` status `ready` deltaP `5.6373` edge `-0.0172` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.6103` n `103` status `ready` deltaP `-7.5853` edge `-0.0207` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.7386` n `81` status `ready` deltaP `11.5548` edge `-0.0505` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1377` n `103` status `ready` deltaP `-5.1901` edge `-0.0439` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5646` n `81` status `ready` deltaP `-21.7785` edge `-0.1675` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.6961` n `103` status `ready` deltaP `-7.6827` edge `-0.0916` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.0399` n `103` status `ready` deltaP `-8.6135` edge `-0.1901` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
