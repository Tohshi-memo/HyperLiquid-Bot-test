# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T09:52:28.687040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0587` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `0.0365` n `8`; equity avg `0.0589` n `92`; fx avg `-0.0` n `6`; index avg `0.0127` n `25`; metal avg `0.0501` n `20`; unknown avg `0.0214` n `766`
- 1h: commodity avg `0.0431` n `12`; crypto_alt avg `-0.1392` n `230`; crypto_major avg `-0.1434` n `8`; equity avg `0.0597` n `92`; fx avg `-0.0069` n `6`; index avg `-0.0043` n `25`; metal avg `0.0494` n `20`; unknown avg `0.0574` n `766`
- 4h: commodity avg `0.3655` n `12`; crypto_alt avg `-0.2194` n `230`; crypto_major avg `-0.2632` n `8`; equity avg `0.3852` n `92`; fx avg `0.0593` n `6`; index avg `0.0048` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.0694` n `750`
- 24h: commodity avg `1.6224` n `12`; crypto_alt avg `-0.9455` n `230`; crypto_major avg `-0.8296` n `8`; equity avg `-0.5515` n `92`; fx avg `-0.021` n `6`; index avg `-0.1191` n `25`; metal avg `-0.1212` n `20`; unknown avg `-0.301` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
