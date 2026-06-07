# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T04:37:24.253509+00:00`
- Price records: `672`
- Market context records: `3144`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8008`

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

- `market_context_high->commodity_24h` score `14.2618` n `109` status `ready` deltaP `47.5965` edge `0.914` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `11.9339` n `109` status `ready` deltaP `22.1537` edge `0.8956` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.4223` n `109` status `ready` deltaP `12.046` edge `2.3817` maxDD `-71.142`
- `market_context_high->index_24h` score `6.5857` n `109` status `ready` deltaP `31.2563` edge `0.8914` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6738` n `109` status `ready` deltaP `12.4395` edge `1.3579` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.762` n `146` status `ready` deltaP `17.875` edge `0.1568` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1534` n `146` status `ready` deltaP `4.1322` edge `0.0275` maxDD `-1.7142`
- `market_context_high->crypto_alt_1h` score `-0.3588` n `146` status `ready` deltaP `6.5048` edge `0.1236` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.4045` n `109` status `ready` deltaP `6.0079` edge `-0.001` maxDD `-0.4876`
- `market_context_high->index_1h` score `-0.5164` n `146` status `ready` deltaP `3.5518` edge `0.0164` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.8168` n `146` status `ready` deltaP `3.4882` edge `0.0206` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-0.9453` n `146` status `ready` deltaP `3.5251` edge `0.0816` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.107` n `146` status `ready` deltaP `12.1764` edge `0.0678` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.1431` n `146` status `ready` deltaP `-10.9179` edge `-0.0055` maxDD `-0.7941`
- `market_context_high->fx_4h` score `-1.4804` n `146` status `ready` deltaP `-13.9221` edge `-0.0085` maxDD `-1.4115`
- `market_context_high->unknown_4h` score `-1.5625` n `146` status `ready` deltaP `6.0015` edge `0.052` maxDD `-14.7778`
- `market_context_high->metal_1h` score `-2.0552` n `146` status `ready` deltaP `-4.1547` edge `-0.0042` maxDD `-7.4828`
- `market_context_high->equity_4h` score `-2.7667` n `146` status `ready` deltaP `13.9283` edge `0.083` maxDD `-36.7784`
- `market_context_high->crypto_alt_4h` score `-2.7968` n `146` status `ready` deltaP `19.5769` edge `0.4409` maxDD `-58.6918`
- `market_context_high->unknown_1h` score `-3.1681` n `146` status `ready` deltaP `1.6098` edge `-0.0721` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
