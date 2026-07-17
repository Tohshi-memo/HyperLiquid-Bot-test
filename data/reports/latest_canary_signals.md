# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T08:52:25.165724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0514` n `12`; crypto_alt avg `0.345` n `230`; crypto_major avg `0.2718` n `8`; equity avg `0.0616` n `96`; fx avg `-0.0038` n `6`; index avg `0.0023` n `25`; metal avg `0.0678` n `20`; unknown avg `-0.0008` n `768`
- 1h: commodity avg `0.0806` n `12`; crypto_alt avg `-0.0272` n `230`; crypto_major avg `0.0127` n `8`; equity avg `-0.5161` n `96`; fx avg `0.0278` n `6`; index avg `-0.0908` n `25`; metal avg `-0.0399` n `20`; unknown avg `-0.0561` n `768`
- 4h: commodity avg `-0.0632` n `12`; crypto_alt avg `-0.8931` n `230`; crypto_major avg `-0.9193` n `8`; equity avg `-1.1902` n `96`; fx avg `0.0433` n `6`; index avg `-0.1247` n `25`; metal avg `-0.0192` n `20`; unknown avg `-0.1472` n `736`
- 24h: commodity avg `-0.1069` n `12`; crypto_alt avg `-1.6327` n `230`; crypto_major avg `-2.8965` n `8`; equity avg `-5.8164` n `94`; fx avg `-0.0382` n `6`; index avg `-0.8205` n `25`; metal avg `-0.8005` n `20`; unknown avg `-0.5103` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
