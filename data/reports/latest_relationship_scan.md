# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T18:52:32.405098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `risk_on_high->unknown_4h` score `7.8706` n `107` status `ready` deltaP `23.7264` edge `0.5594` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8706` n `107` status `ready` deltaP `23.7264` edge `0.5594` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3234` n `159` status `ready` deltaP `20.423` edge `0.4602` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `2.7134` n `81` status `ready` deltaP `19.5988` edge `0.7894` maxDD `-36.4415`
- `risk_on_and_context->crypto_alt_24h` score `2.7134` n `81` status `ready` deltaP `19.5988` edge `0.7894` maxDD `-36.4415`
- `risk_on_high->unknown_1h` score `2.4774` n `107` status `ready` deltaP `6.9646` edge `0.2177` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.4774` n `107` status `ready` deltaP `6.9646` edge `0.2177` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2536` n `159` status `ready` deltaP `6.3063` edge `0.2088` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.9933` n `81` status `ready` deltaP `13.2909` edge `0.1763` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.9933` n `81` status `ready` deltaP `13.2909` edge `0.1763` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.5718` n `61` status `ready` deltaP `4.0689` edge `0.1385` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.5585` n `81` status `ready` deltaP `46.7206` edge `0.0286` maxDD `-2.5542`
- `risk_on_and_context->fx_24h` score `1.5585` n `81` status `ready` deltaP `46.7206` edge `0.0286` maxDD `-2.5542`
- `market_context_high->fx_24h` score `0.7047` n `124` status `ready` deltaP `30.4323` edge `0.0211` maxDD `-3.2206`
- `news_risk_high->commodity_4h` score `0.2755` n `61` status `ready` deltaP `7.7969` edge `0.025` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.221` n `159` status `ready` deltaP `9.7795` edge `0.0182` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1451` n `61` status `ready` deltaP `10.6533` edge `0.0004` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.078` n `44` status `ready` deltaP `4.0878` edge `0.0143` maxDD `-1.1904`
- `market_context_high->commodity_4h` score `0.0556` n `159` status `ready` deltaP `7.2711` edge `0.0459` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `0.0286` n `107` status `ready` deltaP `6.0706` edge `0.0154` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
