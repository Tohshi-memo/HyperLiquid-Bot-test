# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T07:52:31.556532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `-0.0111` n `8`; equity avg `0.0505` n `93`; fx avg `0.0001` n `6`; index avg `0.02` n `25`; metal avg `0.0509` n `20`; unknown avg `0.0088` n `765`
- 1h: commodity avg `0.0977` n `12`; crypto_alt avg `-0.4566` n `230`; crypto_major avg `-0.5632` n `8`; equity avg `-0.0674` n `93`; fx avg `0.0128` n `6`; index avg `-0.0285` n `25`; metal avg `-0.0295` n `20`; unknown avg `-0.0199` n `765`
- 4h: commodity avg `0.0618` n `12`; crypto_alt avg `-0.4186` n `230`; crypto_major avg `-0.3531` n `8`; equity avg `-0.1974` n `93`; fx avg `-0.0085` n `6`; index avg `-0.0853` n `25`; metal avg `-0.0521` n `20`; unknown avg `-0.0689` n `747`
- 24h: commodity avg `0.0379` n `12`; crypto_alt avg `1.3884` n `230`; crypto_major avg `3.021` n `8`; equity avg `1.5197` n `92`; fx avg `0.0633` n `6`; index avg `0.4547` n `25`; metal avg `0.2292` n `20`; unknown avg `0.2653` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
