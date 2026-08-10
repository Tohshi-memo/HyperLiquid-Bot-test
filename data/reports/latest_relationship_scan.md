# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T01:07:26.982590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.3847` n `155` status `ready` deltaP `15.7032` edge `0.078` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8251` n `167` status `ready` deltaP `10.7785` edge `0.0312` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4333` n `134` status `ready` deltaP `18.2576` edge `0.0205` maxDD `-1.9329`
- `market_context_high->fx_1h` score `-0.2526` n `167` status `ready` deltaP `2.8443` edge `-0.0018` maxDD `-0.9639`
- `market_context_high->metal_24h` score `-0.4732` n `134` status `ready` deltaP `-1.0857` edge `0.0504` maxDD `-2.2743`
- `market_context_high->fx_4h` score `-0.5708` n `155` status `ready` deltaP `4.1935` edge `-0.0002` maxDD `-1.6928`
- `market_context_high->index_24h` score `-0.5768` n `134` status `ready` deltaP `1.6765` edge `0.0939` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.6034` n `167` status `ready` deltaP `-3.5928` edge `-0.0057` maxDD `-0.8168`
- `market_context_high->equity_24h` score `-0.6429` n `134` status `ready` deltaP `0.9614` edge `0.246` maxDD `-21.1456`
- `market_context_high->metal_1h` score `-0.7873` n `167` status `ready` deltaP `-4.6407` edge `-0.0104` maxDD `-1.7676`
- `market_context_high->equity_1h` score `-0.8057` n `167` status `ready` deltaP `-1.9461` edge `-0.0033` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.8336` n `155` status `ready` deltaP `-3.8749` edge `-0.0113` maxDD `-1.2461`
- `market_context_high->metal_4h` score `-1.4346` n `155` status `ready` deltaP `-4.999` edge `-0.0284` maxDD `-4.442`
- `market_context_high->crypto_alt_1h` score `-1.5655` n `167` status `ready` deltaP `-8.8323` edge `-0.0397` maxDD `-5.5029`
- `market_context_high->equity_4h` score `-2.0249` n `155` status `ready` deltaP `-4.8112` edge `-0.0813` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.6725` n `167` status `ready` deltaP `-10.3293` edge `-0.0638` maxDD `-10.5372`
- `market_context_high->crypto_alt_24h` score `-4.5492` n `134` status `ready` deltaP `-11.9688` edge `-0.155` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.591` n `134` status `ready` deltaP `-0.684` edge `-0.1286` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-5.2958` n `155` status `ready` deltaP `-11.1704` edge `-0.1475` maxDD `-10.8814`
- `market_context_high->unknown_1h` score `-7.5425` n `167` status `ready` deltaP `-4.6407` edge `-0.5519` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
