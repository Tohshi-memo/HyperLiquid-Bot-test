# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T01:52:25.450133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0306` n `230`; crypto_major avg `0.0325` n `8`; equity avg `0.0288` n `112`; fx avg `0.006` n `6`; index avg `0.0042` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0874` n `784`
- 1h: commodity avg `0.0655` n `12`; crypto_alt avg `-0.0898` n `230`; crypto_major avg `-0.122` n `8`; equity avg `-0.0606` n `112`; fx avg `0.0119` n `6`; index avg `-0.0147` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.2212` n `784`
- 4h: commodity avg `0.0421` n `12`; crypto_alt avg `-0.1736` n `230`; crypto_major avg `-0.3685` n `8`; equity avg `-0.0451` n `112`; fx avg `0.0127` n `6`; index avg `-0.0009` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.1242` n `784`
- 24h: commodity avg `0.2252` n `12`; crypto_alt avg `1.5831` n `230`; crypto_major avg `0.8973` n `8`; equity avg `0.4563` n `112`; fx avg `-0.0025` n `6`; index avg `0.0294` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.1485` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
