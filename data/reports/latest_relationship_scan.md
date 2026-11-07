# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T00:52:29.993058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.8475` n `71` status `ready` deltaP `6.454` edge `0.1562` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.5521` n `71` status `ready` deltaP `11.1732` edge `0.0193` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.2122` n `71` status `ready` deltaP `7.4579` edge `0.1443` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0276` n `71` status `ready` deltaP `6.6648` edge `0.0032` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0589` n `71` status `ready` deltaP `0.1054` edge `0.0467` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0876` n `71` status `ready` deltaP `4.5388` edge `0.0031` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.2003` n `71` status `ready` deltaP `-3.0345` edge `0.0478` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2503` n `71` status `ready` deltaP `0.738` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4961` n `71` status `ready` deltaP `-3.1606` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.3003` n `71` status `ready` deltaP `-5.3934` edge `-0.0402` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-2.1329` n `71` status `ready` deltaP `-7.8688` edge `-0.0314` maxDD `-4.1772`
- `news_risk_high->commodity_1h` score `-2.4896` n `71` status `ready` deltaP `-16.2857` edge `-0.0059` maxDD `-1.4399`
- `news_risk_high->crypto_alt_1h` score `-2.5627` n `71` status `ready` deltaP `-5.8615` edge `-0.0517` maxDD `-5.8225`
- `news_risk_high->crypto_major_4h` score `-2.723` n `71` status `ready` deltaP `-7.3622` edge `-0.0153` maxDD `-8.6694`
- `news_risk_high->crypto_alt_4h` score `-3.0099` n `71` status `ready` deltaP `-9.039` edge `-0.0636` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.3827` n `71` status `ready` deltaP `-0.8363` edge `-0.2385` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.4472` n `71` status `ready` deltaP `21.5987` edge `0.5727` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.3425` n `71` status `ready` deltaP `-29.3671` edge `-0.0063` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-9.8849` n `71` status `ready` deltaP `-26.5991` edge `-0.0785` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.2925` n `71` status `ready` deltaP `-29.4723` edge `-0.0609` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
