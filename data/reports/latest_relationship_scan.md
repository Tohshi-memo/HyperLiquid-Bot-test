# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T04:52:10.871202+00:00`
- Price records: `519`
- Market context records: `614`
- Flow alert records: `1737`
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

- `market_context_high->crypto_alt_24h` score `5.1743` n `146` status `ready` deltaP `7.5893` edge `0.3854` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `4.6969` n `146` status `ready` deltaP `13.5302` edge `0.3346` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0567` n `146` status `ready` deltaP `9.5218` edge `0.0164` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3285` n `146` status `ready` deltaP `1.8591` edge `0.0033` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6374` n `146` status `ready` deltaP `1.1742` edge `0.0365` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6809` n `146` status `ready` deltaP `0.0978` edge `-0.0026` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.0305` n `146` status `ready` deltaP `-3.3063` edge `-0.0035` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.0715` n `146` status `ready` deltaP `6.1312` edge `0.0013` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2544` n `146` status `ready` deltaP `-2.0548` edge `-0.0098` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.4895` n `146` status `ready` deltaP `5.3174` edge `0.0974` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.6407` n `146` status `ready` deltaP `5.9968` edge `-0.0044` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2243` n `146` status `ready` deltaP `14.6613` edge `0.0875` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.277` n `146` status `ready` deltaP `-0.4626` edge `-0.0344` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7083` n `146` status `ready` deltaP `-7.5571` edge `0.0242` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.1855` n `146` status `ready` deltaP `-3.0678` edge `-0.0298` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2558` n `146` status `ready` deltaP `-4.1535` edge `-0.0477` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7019` n `146` status `ready` deltaP `-6.4348` edge `0.0845` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2606` n `146` status `ready` deltaP `-2.4978` edge `-0.0124` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6689` n `146` status `ready` deltaP `2.466` edge `-0.2177` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7012` n `146` status `ready` deltaP `-11.0537` edge `-0.0576` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
