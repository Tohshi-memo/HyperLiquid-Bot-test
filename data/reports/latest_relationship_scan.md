# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T15:22:25.302343+00:00`
- Price records: `672`
- Market context records: `2981`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `15.5154` n `102` status `ready` deltaP `6.1683` edge `1.6435` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.1889` n `102` status `ready` deltaP `40.1245` edge `0.683` maxDD `-0.7805`
- `market_context_high->unknown_24h` score `10.4294` n `102` status `ready` deltaP `15.9722` edge `0.8091` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.7185` n `102` status `ready` deltaP `15.7271` edge `0.6554` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.1654` n `102` status `ready` deltaP `15.7782` edge `0.34` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.9325` n `103` status `ready` deltaP `15.1374` edge `0.1824` maxDD `-0.7819`
- `market_context_high->index_4h` score `2.1558` n `103` status `ready` deltaP `19.9029` edge `0.1258` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `1.9222` n `103` status `ready` deltaP `14.9849` edge `0.125` maxDD `-2.8438`
- `market_context_high->equity_1h` score `0.8888` n `104` status `ready` deltaP `7.1972` edge `0.0611` maxDD `-1.1343`
- `market_context_high->index_1h` score `0.6512` n `104` status `ready` deltaP `8.7172` edge `0.0353` maxDD `-0.7983`
- `market_context_high->crypto_alt_4h` score `0.479` n `103` status `ready` deltaP `21.892` edge `0.3716` maxDD `-30.8239`
- `market_context_high->commodity_1h` score `-0.2611` n `104` status `ready` deltaP `-0.6852` edge `0.0109` maxDD `-1.5182`
- `market_context_high->crypto_alt_1h` score `-0.3602` n `104` status `ready` deltaP `8.8035` edge `0.0748` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.4017` n `104` status `ready` deltaP `8.1011` edge `0.0481` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.5051` n `104` status `ready` deltaP `-1.9461` edge `0.0016` maxDD `-0.1244`
- `market_context_high->fx_4h` score `-1.0587` n `103` status `ready` deltaP `-8.7097` edge `0.0002` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.2628` n `104` status `ready` deltaP `-2.3261` edge `0.0041` maxDD `-3.8394`
- `market_context_high->unknown_4h` score `-1.3039` n `103` status `ready` deltaP `-1.039` edge `0.0036` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.4009` n `102` status `ready` deltaP `-9.4975` edge `-0.0291` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.5241` n `104` status `ready` deltaP `2.7119` edge `-0.072` maxDD `-3.1801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
