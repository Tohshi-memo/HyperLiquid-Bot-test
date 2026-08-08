# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T04:52:29.405138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.0793` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `0.0015` n `112`; fx avg `0.0` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0148` n `20`; unknown avg `-0.0427` n `783`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.0112` n `230`; crypto_major avg `-0.0301` n `8`; equity avg `0.0004` n `112`; fx avg `-0.0051` n `6`; index avg `-0.021` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0115` n `783`
- 4h: commodity avg `0.0247` n `12`; crypto_alt avg `0.5036` n `230`; crypto_major avg `0.5152` n `8`; equity avg `-0.0583` n `112`; fx avg `-0.0006` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0345` n `20`; unknown avg `0.0354` n `783`
- 24h: commodity avg `-0.2357` n `12`; crypto_alt avg `0.3593` n `230`; crypto_major avg `0.927` n `8`; equity avg `1.8665` n `112`; fx avg `-0.0693` n `6`; index avg `0.2102` n `25`; metal avg `0.3374` n `20`; unknown avg `0.0501` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
