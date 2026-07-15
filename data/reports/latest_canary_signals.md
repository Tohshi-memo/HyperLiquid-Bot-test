# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T00:22:29.365666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0646` n `12`; crypto_alt avg `-0.1021` n `230`; crypto_major avg `-0.2196` n `8`; equity avg `0.2327` n `92`; fx avg `0.0122` n `6`; index avg `0.0805` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0627` n `768`
- 1h: commodity avg `0.13` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `-0.0491` n `8`; equity avg `0.4309` n `92`; fx avg `0.0382` n `6`; index avg `0.0872` n `25`; metal avg `0.0364` n `20`; unknown avg `-0.3765` n `768`
- 4h: commodity avg `0.0763` n `12`; crypto_alt avg `0.3835` n `230`; crypto_major avg `0.3058` n `8`; equity avg `0.7195` n `92`; fx avg `0.0225` n `6`; index avg `0.1536` n `25`; metal avg `0.032` n `20`; unknown avg `-0.5921` n `766`
- 24h: commodity avg `-0.0313` n `12`; crypto_alt avg `1.9546` n `230`; crypto_major avg `3.2462` n `8`; equity avg `2.2332` n `92`; fx avg `0.0358` n `6`; index avg `0.6526` n `25`; metal avg `0.7479` n `20`; unknown avg `0.1805` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
