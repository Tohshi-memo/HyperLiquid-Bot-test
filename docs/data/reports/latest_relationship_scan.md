# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T03:07:27.470595+00:00`
- Price records: `672`
- Market context records: `7313`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_1h` score `1.2768` n `32` status `ready` deltaP `20.0786` edge `0.0543` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2768` n `32` status `ready` deltaP `20.0786` edge `0.0543` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2576` n `32` status `ready` deltaP `4.6547` edge `0.0397` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2576` n `32` status `ready` deltaP `4.6547` edge `0.0397` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2151` n `32` status `ready` deltaP `3.9977` edge `0.0192` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2151` n `32` status `ready` deltaP `3.9977` edge `0.0192` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1017` n `32` status `ready` deltaP `0.0` edge `0.0501` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1017` n `32` status `ready` deltaP `0.0` edge `0.0501` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.2089` n `129` status `ready` deltaP `3.3382` edge `-0.0001` maxDD `-0.5821`
- `market_context_high->commodity_1h` score `-0.7362` n `129` status `ready` deltaP `-3.4151` edge `-0.0144` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7437` n `129` status `ready` deltaP `-4.26` edge `-0.0061` maxDD `-1.868`
- `market_context_high->fx_24h` score `-0.7769` n `111` status `ready` deltaP `3.0877` edge `0.0026` maxDD `-2.1564`
- `market_context_high->crypto_major_1h` score `-0.8122` n `129` status `ready` deltaP `3.2424` edge `0.0153` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.9301` n `123` status `ready` deltaP `-0.6756` edge `-0.0179` maxDD `-2.4139`
- `risk_on_high->index_1h` score `-0.9477` n `32` status `ready` deltaP `-14.0953` edge `0.0053` maxDD `-0.2932`
- `risk_on_and_context->index_1h` score `-0.9477` n `32` status `ready` deltaP `-14.0953` edge `0.0053` maxDD `-0.2932`
- `market_context_high->unknown_4h` score `-1.0275` n `123` status `ready` deltaP `6.1722` edge `0.1091` maxDD `-6.2031`
- `market_context_high->crypto_alt_1h` score `-1.102` n `129` status `ready` deltaP `-1.1628` edge `0.0198` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-1.1247` n `123` status `ready` deltaP `1.2844` edge `0.0073` maxDD `-1.4707`
- `risk_on_high->fx_1h` score `-1.1983` n `32` status `ready` deltaP `-9.5252` edge `-0.008` maxDD `-0.2687`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
