# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T08:22:30.390767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0172` n `230`; crypto_major avg `0.0474` n `8`; equity avg `0.1029` n `102`; fx avg `-0.0066` n `6`; index avg `0.0052` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0174` n `782`
- 1h: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.0838` n `230`; crypto_major avg `-0.0916` n `8`; equity avg `0.2493` n `102`; fx avg `-0.004` n `6`; index avg `0.026` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.074` n `782`
- 4h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.181` n `230`; crypto_major avg `-0.1368` n `8`; equity avg `0.2238` n `102`; fx avg `-0.0332` n `6`; index avg `0.0437` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.309` n `766`
- 24h: commodity avg `-1.154` n `12`; crypto_alt avg `0.4273` n `230`; crypto_major avg `0.4051` n `8`; equity avg `0.9662` n `102`; fx avg `-0.1699` n `6`; index avg `0.2798` n `25`; metal avg `0.2407` n `20`; unknown avg `0.2785` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
