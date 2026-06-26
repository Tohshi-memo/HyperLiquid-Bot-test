# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T14:07:26.333440+00:00`
- Price records: `672`
- Market context records: `4834`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.7823` n `109` status `ready` deltaP `11.038` edge `1.1167` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.34` n `103` status `ready` deltaP `21.3874` edge `0.7489` maxDD `-4.0518`
- `market_context_high->unknown_24h` score `3.7178` n `96` status `ready` deltaP `19.2708` edge `0.2423` maxDD `-2.21`
- `market_context_high->index_4h` score `0.6396` n `103` status `ready` deltaP `9.0546` edge `0.0396` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.3527` n `103` status `ready` deltaP `10.9001` edge `0.1107` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.1572` n `103` status `ready` deltaP `13.4191` edge `0.0479` maxDD `-4.377`
- `market_context_high->equity_1h` score `0.1046` n `109` status `ready` deltaP `4.5775` edge `0.0398` maxDD `-2.928`
- `market_context_high->commodity_1h` score `0.0829` n `109` status `ready` deltaP `4.5006` edge `0.0288` maxDD `-1.1869`
- `market_context_high->fx_4h` score `-0.2531` n `103` status `ready` deltaP `4.8262` edge `0.0046` maxDD `-0.8707`
- `market_context_high->index_1h` score `-0.5399` n `109` status `ready` deltaP `-0.5892` edge `0.0102` maxDD `-0.7054`
- `market_context_high->crypto_alt_4h` score `-0.6502` n `103` status `ready` deltaP `12.2321` edge `0.1407` maxDD `-21.4483`
- `market_context_high->fx_1h` score `-0.7666` n `109` status `ready` deltaP `-4.3551` edge `-0.0043` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.3541` n `109` status `ready` deltaP `4.09` edge `-0.0085` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.0659` n `109` status `ready` deltaP `2.8155` edge `-0.0261` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.1691` n `109` status `ready` deltaP `0.0632` edge `-0.0682` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.173` n `96` status `ready` deltaP `-9.5486` edge `-0.0164` maxDD `-2.749`
- `market_context_high->crypto_major_4h` score `-2.3774` n `103` status `ready` deltaP `8.7497` edge `0.0721` maxDD `-31.8182`
- `market_context_high->commodity_24h` score `-2.8156` n `96` status `ready` deltaP `15.4514` edge `0.0469` maxDD `-27.5371`
- `market_context_high->metal_4h` score `-3.9955` n `103` status `ready` deltaP `8.0112` edge `-0.141` maxDD `-30.6392`
- `market_context_high->index_24h` score `-4.212` n `96` status `ready` deltaP `-4.6875` edge `-0.1179` maxDD `-23.2678`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
