# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T19:07:23.894959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.0518` n `239`; crypto_major avg `-0.0455` n `8`; equity avg `-0.0322` n `158`; fx avg `-0.0139` n `6`; index avg `0.0032` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.1112` n `1258`
- 1h: commodity avg `0.004` n `13`; crypto_alt avg `-0.0844` n `239`; crypto_major avg `0.0005` n `8`; equity avg `0.0474` n `158`; fx avg `-0.0064` n `6`; index avg `0.0139` n `27`; metal avg `0.0055` n `20`; unknown avg `-0.1297` n `1254`
- 4h: commodity avg `0.0239` n `13`; crypto_alt avg `0.2179` n `239`; crypto_major avg `-0.0374` n `8`; equity avg `0.0582` n `158`; fx avg `-0.0226` n `6`; index avg `0.0303` n `27`; metal avg `-0.014` n `20`; unknown avg `0.4327` n `1209`
- 24h: commodity avg `0.0856` n `13`; crypto_alt avg `-1.348` n `239`; crypto_major avg `-0.5401` n `8`; equity avg `0.2672` n `158`; fx avg `-0.0162` n `6`; index avg `0.0359` n `27`; metal avg `-0.0546` n `20`; unknown avg `0.362` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
