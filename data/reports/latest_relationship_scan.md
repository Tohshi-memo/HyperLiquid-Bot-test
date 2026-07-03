# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T12:52:28.374343+00:00`
- Price records: `672`
- Market context records: `5558`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11378`

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

- `market_context_high->equity_24h` score `4.4258` n `187` status `ready` deltaP `15.1515` edge `0.7757` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.6784` n `191` status `ready` deltaP `11.3428` edge `0.2935` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `1.6306` n `187` status `ready` deltaP `15.7967` edge `0.4846` maxDD `-29.6555`
- `market_context_high->equity_4h` score `1.1937` n `191` status `ready` deltaP `7.6706` edge `0.2122` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.1794` n `191` status `ready` deltaP `6.7896` edge `0.2171` maxDD `-9.46`
- `market_context_high->fx_24h` score `0.6967` n `187` status `ready` deltaP `16.4912` edge `0.0455` maxDD `-1.457`
- `market_context_high->equity_1h` score `0.2626` n `201` status `ready` deltaP `7.742` edge `0.0668` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0043` n `201` status `ready` deltaP `5.5628` edge `0.0119` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.1265` n `201` status `ready` deltaP `2.4764` edge `0.0691` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.2661` n `201` status `ready` deltaP `4.0307` edge `0.0755` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3068` n `201` status `ready` deltaP `1.3406` edge `0.0006` maxDD `-0.5763`
- `market_context_high->fx_4h` score `-0.46` n `191` status `ready` deltaP `4.8541` edge `0.008` maxDD `-1.2957`
- `market_context_high->metal_1h` score `-0.6847` n `201` status `ready` deltaP `0.3985` edge `0.0078` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-1.4613` n `201` status `ready` deltaP `-5.0742` edge `-0.0114` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5589` n `191` status `ready` deltaP `1.7726` edge `0.0192` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.018` n `187` status `ready` deltaP `12.4146` edge `0.0572` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.058` n `191` status `ready` deltaP `-12.6748` edge `-0.0551` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.7292` n `191` status `ready` deltaP `-9.9572` edge `-0.0602` maxDD `-14.0684`
- `market_context_high->metal_24h` score `-7.5808` n `187` status `ready` deltaP `-5.1498` edge `-0.1998` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.7481` n `187` status `ready` deltaP `6.6362` edge `0.1798` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
