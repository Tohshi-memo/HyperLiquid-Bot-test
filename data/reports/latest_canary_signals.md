# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T07:22:35.100139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.03` n `230`; crypto_major avg `0.0123` n `8`; equity avg `0.0107` n `112`; fx avg `-0.0079` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0146` n `784`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `0.0723` n `230`; crypto_major avg `0.0392` n `8`; equity avg `0.0374` n `112`; fx avg `-0.0075` n `6`; index avg `0.0029` n `25`; metal avg `-0.0091` n `20`; unknown avg `-0.0755` n `784`
- 4h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.273` n `230`; crypto_major avg `0.2708` n `8`; equity avg `-0.1463` n `112`; fx avg `-0.0039` n `6`; index avg `-0.0439` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.1123` n `751`
- 24h: commodity avg `-0.1809` n `12`; crypto_alt avg `-0.0652` n `230`; crypto_major avg `0.6432` n `8`; equity avg `1.1477` n `112`; fx avg `-0.0529` n `6`; index avg `0.0737` n `25`; metal avg `0.0355` n `20`; unknown avg `-0.0578` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
