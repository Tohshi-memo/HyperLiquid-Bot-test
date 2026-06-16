# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T18:07:38.083252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.4173` n `228`; crypto_major avg `0.3723` n `8`; equity avg `0.1001` n `77`; fx avg `-0.0049` n `6`; index avg `0.0038` n `23`; metal avg `0.0861` n `18`; unknown avg `0.1188` n `687`
- 1h: commodity avg `-0.1132` n `12`; crypto_alt avg `1.011` n `228`; crypto_major avg `1.0121` n `8`; equity avg `0.2041` n `77`; fx avg `0.0048` n `6`; index avg `0.103` n `23`; metal avg `0.1201` n `18`; unknown avg `0.4002` n `687`
- 4h: commodity avg `-0.6222` n `12`; crypto_alt avg `0.3486` n `228`; crypto_major avg `0.0165` n `8`; equity avg `-0.8609` n `77`; fx avg `0.0789` n `6`; index avg `-0.6536` n `23`; metal avg `-0.0531` n `18`; unknown avg `0.5248` n `687`
- 24h: commodity avg `-1.079` n `12`; crypto_alt avg `-0.9145` n `228`; crypto_major avg `-0.3239` n `8`; equity avg `-0.7255` n `77`; fx avg `-0.0103` n `6`; index avg `-0.5532` n `23`; metal avg `0.703` n `18`; unknown avg `1.05` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
