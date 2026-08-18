# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T20:36:18.409790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `0.0157` n `8`; equity avg `0.0517` n `120`; fx avg `0.0033` n `6`; index avg `0.0182` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0405` n `789`
- 1h: commodity avg `0.0931` n `12`; crypto_alt avg `-0.203` n `230`; crypto_major avg `-0.1034` n `8`; equity avg `-0.133` n `120`; fx avg `-0.0029` n `6`; index avg `-0.0274` n `25`; metal avg `-0.0951` n `20`; unknown avg `-0.015` n `789`
- 4h: commodity avg `0.0487` n `12`; crypto_alt avg `-0.4106` n `230`; crypto_major avg `0.0063` n `8`; equity avg `-0.4549` n `120`; fx avg `-0.0024` n `6`; index avg `-0.0362` n `25`; metal avg `-0.1733` n `20`; unknown avg `0.1429` n `789`
- 24h: commodity avg `0.3074` n `12`; crypto_alt avg `-0.6623` n `230`; crypto_major avg `0.2741` n `8`; equity avg `-4.2474` n `120`; fx avg `-0.0501` n `6`; index avg `-0.6724` n `25`; metal avg `-0.7607` n `20`; unknown avg `-0.2555` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
