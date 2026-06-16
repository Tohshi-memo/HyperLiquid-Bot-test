# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T10:37:33.498607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.2221` n `228`; crypto_major avg `0.1949` n `8`; equity avg `0.0615` n `77`; fx avg `-0.0` n `6`; index avg `-0.1719` n `23`; metal avg `-0.0582` n `18`; unknown avg `0.1721` n `687`
- 1h: commodity avg `-0.0333` n `12`; crypto_alt avg `0.2801` n `228`; crypto_major avg `0.4119` n `8`; equity avg `0.0773` n `77`; fx avg `0.0216` n `6`; index avg `0.0305` n `23`; metal avg `-0.0568` n `18`; unknown avg `0.1181` n `687`
- 4h: commodity avg `-0.677` n `12`; crypto_alt avg `0.9264` n `228`; crypto_major avg `1.0817` n `8`; equity avg `0.4908` n `77`; fx avg `0.0655` n `6`; index avg `0.1463` n `23`; metal avg `0.9185` n `18`; unknown avg `0.4176` n `687`
- 24h: commodity avg `0.0275` n `12`; crypto_alt avg `1.4593` n `228`; crypto_major avg `3.3482` n `8`; equity avg `1.8484` n `76`; fx avg `-0.0683` n `6`; index avg `0.5395` n `23`; metal avg `0.1702` n `18`; unknown avg `0.3107` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
