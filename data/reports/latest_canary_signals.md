# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T16:22:31.630112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0934` n `231`; crypto_major avg `-0.1` n `8`; equity avg `0.0184` n `128`; fx avg `0.0` n `6`; index avg `0.0045` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.0175` n `792`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `0.0051` n `231`; crypto_major avg `-0.0251` n `8`; equity avg `0.012` n `128`; fx avg `0.0014` n `6`; index avg `0.0027` n `26`; metal avg `0.0132` n `20`; unknown avg `-0.0921` n `788`
- 4h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.7197` n `231`; crypto_major avg `0.6367` n `8`; equity avg `0.0198` n `128`; fx avg `-0.0011` n `6`; index avg `0.0025` n `26`; metal avg `0.0515` n `20`; unknown avg `0.3066` n `776`
- 24h: commodity avg `0.0891` n `12`; crypto_alt avg `1.1219` n `231`; crypto_major avg `0.7` n `8`; equity avg `0.196` n `128`; fx avg `-0.051` n `6`; index avg `0.0422` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.0719` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
