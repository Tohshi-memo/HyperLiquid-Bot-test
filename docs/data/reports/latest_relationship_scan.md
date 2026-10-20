# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T15:22:37.256755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8855`

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

- `risk_on_high->equity_1h` score `0.6515` n `37` status `ready` deltaP `15.4475` edge `0.0229` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6515` n `37` status `ready` deltaP `15.4475` edge `0.0229` maxDD `-0.7219`
- `market_context_high->commodity_24h` score `0.6467` n `73` status `ready` deltaP `14.9615` edge `0.0393` maxDD `-1.8119`
- `risk_on_high->index_1h` score `0.5364` n `37` status `ready` deltaP `13.5014` edge `0.0058` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5364` n `37` status `ready` deltaP `13.5014` edge `0.0058` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1267` n `37` status `ready` deltaP `14.147` edge `0.0017` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1267` n `37` status `ready` deltaP `14.147` edge `0.0017` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.023` n `37` status `ready` deltaP `4.2038` edge `0.0008` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.023` n `37` status `ready` deltaP `4.2038` edge `0.0008` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0107` n `78` status `ready` deltaP `5.324` edge `0.0014` maxDD `-0.5082`
- `risk_on_high->index_4h` score `-0.0203` n `37` status `ready` deltaP `9.7355` edge `0.017` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0203` n `37` status `ready` deltaP `9.7355` edge `0.017` maxDD `-0.7604`
- `risk_on_high->equity_4h` score `-0.0353` n `37` status `ready` deltaP `6.6166` edge `0.0768` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0353` n `37` status `ready` deltaP `6.6166` edge `0.0768` maxDD `-4.0351`
- `risk_on_high->fx_4h` score `-0.17` n `37` status `ready` deltaP `0.7827` edge `-0.0006` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.17` n `37` status `ready` deltaP `0.7827` edge `-0.0006` maxDD `-0.1126`
- `market_context_high->commodity_1h` score `-0.2235` n `78` status `ready` deltaP `4.0611` edge `0.0108` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.3616` n `78` status `ready` deltaP `7.0825` edge `0.0096` maxDD `-2.9203`
- `risk_on_high->commodity_1h` score `-0.6533` n `37` status `ready` deltaP `0.1456` edge `-0.0182` maxDD `-0.9891`
- `risk_on_and_context->commodity_1h` score `-0.6533` n `37` status `ready` deltaP `0.1456` edge `-0.0182` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
