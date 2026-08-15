# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T19:52:27.792455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `12`; crypto_alt avg `0.0601` n `230`; crypto_major avg `0.0753` n `8`; equity avg `0.0037` n `114`; fx avg `0.0025` n `6`; index avg `-0.0014` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.034` n `791`
- 1h: commodity avg `0.0723` n `12`; crypto_alt avg `0.0819` n `230`; crypto_major avg `0.1831` n `8`; equity avg `0.0466` n `114`; fx avg `0.0024` n `6`; index avg `0.0029` n `25`; metal avg `0.0074` n `20`; unknown avg `-0.0533` n `791`
- 4h: commodity avg `0.1214` n `12`; crypto_alt avg `-0.0672` n `230`; crypto_major avg `0.1289` n `8`; equity avg `0.0921` n `114`; fx avg `0.0007` n `6`; index avg `0.0027` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.0154` n `791`
- 24h: commodity avg `0.0546` n `12`; crypto_alt avg `1.0548` n `230`; crypto_major avg `0.6939` n `8`; equity avg `0.2485` n `114`; fx avg `0.0182` n `6`; index avg `0.0193` n `25`; metal avg `0.0247` n `20`; unknown avg `0.1005` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
