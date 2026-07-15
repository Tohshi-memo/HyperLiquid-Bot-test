# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T00:52:24.379477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0684` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `0.0399` n `8`; equity avg `0.094` n `92`; fx avg `-0.0062` n `6`; index avg `0.039` n `25`; metal avg `0.0374` n `20`; unknown avg `-0.0097` n `768`
- 1h: commodity avg `0.156` n `12`; crypto_alt avg `-0.0786` n `230`; crypto_major avg `-0.2028` n `8`; equity avg `0.1492` n `92`; fx avg `0.0461` n `6`; index avg `0.0155` n `25`; metal avg `0.0483` n `20`; unknown avg `-0.2889` n `768`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.3249` n `230`; crypto_major avg `0.2684` n `8`; equity avg `0.539` n `92`; fx avg `0.0332` n `6`; index avg `0.1229` n `25`; metal avg `0.0843` n `20`; unknown avg `-0.5744` n `766`
- 24h: commodity avg `0.0921` n `12`; crypto_alt avg `1.8388` n `230`; crypto_major avg `3.1777` n `8`; equity avg `1.7706` n `92`; fx avg `0.038` n `6`; index avg `0.5553` n `25`; metal avg `0.6599` n `20`; unknown avg `0.1402` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
