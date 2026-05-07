# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T23:52:13.828507+00:00`
- Price records: `595`
- Market context records: `698`
- Flow alert records: `1972`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `10.4395` n `146` status `ready` deltaP `25.4481` edge `0.7337` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6054` n `146` status `ready` deltaP `8.3331` edge `0.4997` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1846` n `149` status `ready` deltaP `7.6311` edge `0.0126` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2528` n `149` status `ready` deltaP `3.374` edge `0.0029` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.513` n `149` status `ready` deltaP `2.1449` edge `0.0404` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.591` n `149` status `ready` deltaP `0.7775` edge `0.0044` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1285` n `149` status `ready` deltaP `-1.4269` edge `-0.0035` maxDD `-4.4826`
- `market_context_high->crypto_major_4h` score `-1.1856` n `149` status `ready` deltaP `15.7202` edge `0.1138` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.222` n `149` status `ready` deltaP `-4.4698` edge `-0.0117` maxDD `-2.1602`
- `market_context_high->index_24h` score `-1.3627` n `146` status `ready` deltaP `-4.0418` edge `0.1129` maxDD `-5.9609`
- `market_context_high->crypto_alt_1h` score `-1.4078` n `149` status `ready` deltaP `4.3732` edge `-0.015` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6268` n `149` status `ready` deltaP `2.7149` edge `-0.0014` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6432` n `149` status `ready` deltaP `5.9358` edge `-0.0042` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9794` n `149` status `ready` deltaP `4.1288` edge `0.0645` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.5614` n `146` status `ready` deltaP `-6.0716` edge `0.0875` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5787` n `149` status `ready` deltaP `-0.7633` edge `0.0054` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3105` n `149` status `ready` deltaP `-4.8365` edge `-0.0477` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8277` n `149` status `ready` deltaP `-6.3425` edge `0.0734` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.4034` n `149` status `ready` deltaP `2.4852` edge `-0.1957` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.9649` n `146` status `ready` deltaP `-11.0309` edge `-0.0458` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
