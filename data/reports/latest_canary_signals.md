# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T05:22:25.043690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0171` n `230`; crypto_major avg `0.005` n `8`; equity avg `0.0066` n `112`; fx avg `0.0039` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0141` n `783`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.0154` n `230`; crypto_major avg `0.0229` n `8`; equity avg `-0.0675` n `112`; fx avg `0.0047` n `6`; index avg `-0.0245` n `25`; metal avg `-0.0239` n `20`; unknown avg `0.3118` n `783`
- 4h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.3875` n `230`; crypto_major avg `0.3867` n `8`; equity avg `-0.0793` n `112`; fx avg `0.0028` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.0901` n `783`
- 24h: commodity avg `-0.279` n `12`; crypto_alt avg `0.0652` n `230`; crypto_major avg `0.9575` n `8`; equity avg `1.488` n `112`; fx avg `-0.0807` n `6`; index avg `0.1233` n `25`; metal avg `0.2943` n `20`; unknown avg `0.0038` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
