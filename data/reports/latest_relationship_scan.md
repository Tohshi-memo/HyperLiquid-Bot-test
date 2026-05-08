# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T11:07:18.055675+00:00`
- Price records: `640`
- Market context records: `748`
- Flow alert records: `2112`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1117`

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

- `market_context_high->crypto_major_24h` score `12.9785` n `146` status `ready` deltaP `30.9352` edge `0.9087` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6334` n `146` status `ready` deltaP `7.5872` edge `0.507` maxDD `-0.0508`
- `market_context_high->index_24h` score `0.3389` n `146` status `ready` deltaP `2.2882` edge `0.2125` maxDD `-5.9609`
- `market_context_high->equity_24h` score `-0.2835` n `146` status `ready` deltaP `0.7129` edge `0.2321` maxDD `-10.5047`
- `market_context_high->fx_1h` score `-0.3435` n `166` status `ready` deltaP `3.9424` edge `0.0029` maxDD `-0.291`
- `market_context_high->fx_4h` score `-0.4629` n `156` status `ready` deltaP `5.9057` edge `0.0092` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.5536` n `166` status `ready` deltaP `1.832` edge `0.0391` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9574` n `166` status `ready` deltaP `0.4004` edge `0.0029` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.0444` n `166` status `ready` deltaP `6.0752` edge `-0.0021` maxDD `-11.4508`
- `market_context_high->equity_1h` score `-1.1019` n `166` status `ready` deltaP `-1.4984` edge `-0.0008` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3818` n `166` status `ready` deltaP `4.8931` edge `-0.0163` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.5377` n `166` status `ready` deltaP `-4.1657` edge `-0.0232` maxDD `-3.5069`
- `market_context_high->crypto_major_4h` score `-1.6378` n `156` status `ready` deltaP `17.1474` edge `0.1198` maxDD `-22.648`
- `market_context_high->index_4h` score `-1.7829` n `156` status `ready` deltaP `1.5136` edge `-0.0064` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-2.0024` n `166` status `ready` deltaP `-3.749` edge `-0.0358` maxDD `-9.0076`
- `market_context_high->crypto_alt_4h` score `-2.2322` n `156` status `ready` deltaP `2.2436` edge `0.056` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.6276` n `156` status `ready` deltaP `-1.3896` edge `0.0055` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.7346` n `156` status `ready` deltaP `-5.8685` edge `0.078` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.7964` n `156` status `ready` deltaP `4.8077` edge `-0.1606` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.4239` n `146` status `ready` deltaP `-16.0477` edge `-0.0712` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
