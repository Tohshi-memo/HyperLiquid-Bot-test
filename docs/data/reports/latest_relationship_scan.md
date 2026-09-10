# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T22:07:30.680446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11592`

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

- `risk_on_high->crypto_alt_24h` score `20.1584` n `91` status `ready` deltaP `36.1722` edge `1.4617` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.1584` n `91` status `ready` deltaP `36.1722` edge `1.4617` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.5697` n `201` status `ready` deltaP `27.7364` edge `1.1953` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.8989` n `91` status `ready` deltaP `41.9459` edge `0.4991` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.8989` n `91` status `ready` deltaP `41.9459` edge `0.4991` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.6105` n `91` status `ready` deltaP `32.2015` edge `0.5054` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6105` n `91` status `ready` deltaP `32.2015` edge `0.5054` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2284` n `91` status `ready` deltaP `25.021` edge `1.1667` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2284` n `91` status `ready` deltaP `25.021` edge `1.1667` maxDD `-24.5429`
- `market_context_high->equity_24h` score `7.0162` n `201` status `ready` deltaP `26.5625` edge `0.4076` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.4202` n `91` status `ready` deltaP `26.5625` edge `0.2746` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.4202` n `91` status `ready` deltaP `26.5625` edge `0.2746` maxDD `0.0`
- `risk_on_high->index_24h` score `4.4159` n `91` status `ready` deltaP `42.363` edge `0.0898` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.4159` n `91` status `ready` deltaP `42.363` edge `0.0898` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.5441` n `201` status `ready` deltaP `36.7045` edge `0.09` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.2551` n `91` status `ready` deltaP `31.2115` edge `0.0725` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.2551` n `91` status `ready` deltaP `31.2115` edge `0.0725` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.1305` n `201` status `ready` deltaP `24.3721` edge `0.1006` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.5196` n `91` status `ready` deltaP `20.1356` edge `0.0202` maxDD `-0.2246`
- `risk_on_and_context->equity_1h` score `1.5196` n `91` status `ready` deltaP `20.1356` edge `0.0202` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
