# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T05:22:10.663299+00:00`
- Price records: `521`
- Market context records: `616`
- Flow alert records: `1743`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.1808` n `146` status `ready` deltaP `7.5504` edge `0.3862` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.8235` n `146` status `ready` deltaP `13.8984` edge `0.3427` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0681` n `146` status `ready` deltaP `9.317` edge `0.0163` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3267` n `146` status `ready` deltaP `1.8785` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6397` n `146` status `ready` deltaP `1.1616` edge `0.0364` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6897` n `146` status `ready` deltaP `-0.0547` edge `-0.0027` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0776` n `146` status `ready` deltaP `-3.4895` edge `-0.0062` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1277` n `146` status `ready` deltaP `5.9697` edge `-0.0023` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2695` n `146` status `ready` deltaP `-2.199` edge `-0.0101` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.5397` n `146` status `ready` deltaP `5.1851` edge `0.0941` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.667` n `146` status `ready` deltaP `5.8172` edge `-0.0054` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2184` n `146` status `ready` deltaP `14.6901` edge `0.0878` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.2917` n `146` status `ready` deltaP `-0.6002` edge `-0.0347` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7377` n `146` status `ready` deltaP `-7.6546` edge `0.0224` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2173` n `146` status `ready` deltaP `-3.195` edge `-0.0316` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2704` n `146` status `ready` deltaP `-4.3203` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6841` n `146` status `ready` deltaP `-6.2724` edge `0.0849` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2692` n `146` status `ready` deltaP `-2.5868` edge `-0.0129` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.669` n `146` status `ready` deltaP `2.5105` edge `-0.218` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7268` n `146` status `ready` deltaP `-11.1183` edge `-0.0593` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
