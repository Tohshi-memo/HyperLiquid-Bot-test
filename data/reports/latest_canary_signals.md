# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T23:37:26.199714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0121` n `229`; crypto_major avg `0.0225` n `8`; equity avg `0.1647` n `91`; fx avg `0.0079` n `6`; index avg `0.0453` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0323` n `764`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.0068` n `229`; crypto_major avg `0.0027` n `8`; equity avg `0.0247` n `91`; fx avg `-0.0107` n `6`; index avg `0.0115` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.0414` n `764`
- 4h: commodity avg `0.0976` n `12`; crypto_alt avg `0.0639` n `229`; crypto_major avg `0.017` n `8`; equity avg `0.3257` n `91`; fx avg `0.0121` n `6`; index avg `0.0337` n `25`; metal avg `-0.0973` n `20`; unknown avg `-0.2886` n `764`
- 24h: commodity avg `0.311` n `12`; crypto_alt avg `-1.6107` n `229`; crypto_major avg `-2.3292` n `8`; equity avg `1.6553` n `91`; fx avg `-0.015` n `6`; index avg `0.0335` n `25`; metal avg `-0.7` n `20`; unknown avg `-0.0982` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
