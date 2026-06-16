# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T10:07:39.866364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1879` n `12`; crypto_alt avg `0.0177` n `228`; crypto_major avg `-0.045` n `8`; equity avg `-0.0041` n `77`; fx avg `-0.0033` n `6`; index avg `0.0596` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.0025` n `687`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `-0.4866` n `228`; crypto_major avg `-0.3862` n `8`; equity avg `-0.1624` n `77`; fx avg `-0.0044` n `6`; index avg `-0.0404` n `23`; metal avg `-0.0302` n `18`; unknown avg `0.0946` n `687`
- 4h: commodity avg `-0.4878` n `12`; crypto_alt avg `0.9282` n `228`; crypto_major avg `1.0175` n `8`; equity avg `0.5448` n `77`; fx avg `0.0517` n `6`; index avg `0.1952` n `23`; metal avg `1.054` n `18`; unknown avg `0.3041` n `687`
- 24h: commodity avg `0.2569` n `12`; crypto_alt avg `1.2104` n `228`; crypto_major avg `3.0688` n `8`; equity avg `1.7191` n `76`; fx avg `-0.0802` n `6`; index avg `0.542` n `23`; metal avg `0.2778` n `18`; unknown avg `0.3891` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
