# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T01:07:29.689046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0262` n `12`; crypto_alt avg `0.0865` n `230`; crypto_major avg `0.0757` n `8`; equity avg `0.029` n `112`; fx avg `0.0069` n `6`; index avg `-0.0015` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.1721` n `784`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.0407` n `230`; crypto_major avg `0.0708` n `8`; equity avg `0.0844` n `112`; fx avg `0.0038` n `6`; index avg `0.0012` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.1343` n `784`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.0625` n `230`; crypto_major avg `-0.1877` n `8`; equity avg `0.0576` n `112`; fx avg `0.0084` n `6`; index avg `-0.002` n `25`; metal avg `0.0304` n `20`; unknown avg `-0.2313` n `784`
- 24h: commodity avg `0.1544` n `12`; crypto_alt avg `1.8769` n `230`; crypto_major avg `1.2366` n `8`; equity avg `0.6` n `112`; fx avg `-0.0071` n `6`; index avg `0.0641` n `25`; metal avg `-0.0161` n `20`; unknown avg `0.2105` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
