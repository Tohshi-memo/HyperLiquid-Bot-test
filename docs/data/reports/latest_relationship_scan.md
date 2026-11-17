# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T16:07:39.548141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4056`

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

- `market_context_high->unknown_24h` score `1495.946` n `98` status `ready` deltaP `3.4602` edge `124.6391` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.7254` n `48` status `ready` deltaP `67.7768` edge `4.5959` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.3277` n `48` status `ready` deltaP `30.4859` edge `2.1326` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `15.3382` n `48` status `ready` deltaP `46.5447` edge `1.0585` maxDD `-5.9161`
- `market_context_high->crypto_major_24h` score `14.8857` n `98` status `ready` deltaP `44.559` edge `1.9384` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.124` n `98` status `ready` deltaP `30.6193` edge `1.819` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.3639` n `48` status `ready` deltaP `59.1263` edge `0.4165` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.0283` n `48` status `ready` deltaP `53.9792` edge `0.3925` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0431` n `48` status `ready` deltaP `16.2485` edge `1.3734` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.4851` n `48` status `ready` deltaP `46.9004` edge `0.1674` maxDD `-0.5046`
- `news_risk_high->crypto_alt_4h` score `5.1975` n `48` status `ready` deltaP `27.8455` edge `0.3611` maxDD `-7.0891`
- `news_risk_high->crypto_major_4h` score `4.7171` n `48` status `ready` deltaP `21.2906` edge `0.3438` maxDD `-5.7447`
- `news_risk_high->equity_1h` score `3.7505` n `48` status `ready` deltaP `21.8937` edge `0.2296` maxDD `-3.7082`
- `news_risk_high->index_4h` score `3.451` n `48` status `ready` deltaP `31.4024` edge `0.1068` maxDD `-0.6184`
- `news_risk_high->commodity_4h` score `3.3786` n `48` status `ready` deltaP `32.7744` edge `0.0884` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3544` n `48` status `ready` deltaP `26.6467` edge `0.044` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3506` n `48` status `ready` deltaP `18.0264` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7898` n `48` status `ready` deltaP `18.6347` edge `0.1943` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.4198` n `48` status `ready` deltaP `16.6791` edge `0.0478` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.4161` n `48` status `ready` deltaP `15.6437` edge `0.047` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
