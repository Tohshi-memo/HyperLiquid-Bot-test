# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T12:21:35.839750+00:00`
- Price records: `549`
- Market context records: `645`
- Flow alert records: `1829`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `795`

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

- `market_context_high->crypto_major_24h` score `6.9835` n `146` status `ready` deltaP `18.7124` edge `0.4906` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.987` n `146` status `ready` deltaP `8.8074` edge `0.445` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1775` n `146` status `ready` deltaP `7.5576` edge `0.014` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3549` n `146` status `ready` deltaP `1.3964` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4427` n `146` status `ready` deltaP `2.289` edge `0.0453` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6803` n `146` status `ready` deltaP `-0.0393` edge `-0.0016` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1491` n `146` status `ready` deltaP `-4.2629` edge `-0.007` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2337` n `146` status `ready` deltaP `5.4845` edge `-0.0079` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.2838` n `146` status `ready` deltaP `-2.2574` edge `-0.0109` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7001` n `146` status `ready` deltaP `5.644` edge `-0.007` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0689` n `146` status `ready` deltaP `4.0004` edge `0.0579` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.2431` n `146` status `ready` deltaP `-0.3379` edge `-0.0324` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.3957` n `146` status `ready` deltaP `13.9441` edge `0.078` maxDD `-22.648`
- `market_context_high->index_24h` score `-2.9262` n `146` status `ready` deltaP `-8.7058` edge `0.0137` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.2555` n `146` status `ready` deltaP `-4.6948` edge `0.1101` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.4076` n `146` status `ready` deltaP `-4.1186` edge `-0.0413` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.4641` n `146` status `ready` deltaP `-5.242` edge `-0.0578` maxDD `-9.0076`
- `market_context_high->fx_24h` score `-4.4655` n `146` status `ready` deltaP `-4.8632` edge `-0.0229` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.6521` n `146` status `ready` deltaP `-11.2945` edge `-0.0519` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.8381` n `146` status `ready` deltaP `0.8468` edge `-0.221` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
