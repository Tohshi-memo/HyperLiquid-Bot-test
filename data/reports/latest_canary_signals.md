# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T17:22:27.492565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `0.0433` n `8`; equity avg `0.0199` n `112`; fx avg `0.0027` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0149` n `20`; unknown avg `0.0904` n `784`
- 1h: commodity avg `0.1123` n `12`; crypto_alt avg `0.1174` n `230`; crypto_major avg `0.0235` n `8`; equity avg `0.075` n `112`; fx avg `0.0105` n `6`; index avg `0.0004` n `25`; metal avg `0.0093` n `20`; unknown avg `3.2211` n `784`
- 4h: commodity avg `0.0242` n `12`; crypto_alt avg `0.9198` n `230`; crypto_major avg `0.698` n `8`; equity avg `0.1092` n `112`; fx avg `-0.0009` n `6`; index avg `0.0004` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0394` n `784`
- 24h: commodity avg `-0.1362` n `12`; crypto_alt avg `1.681` n `230`; crypto_major avg `1.8733` n `8`; equity avg `0.7966` n `112`; fx avg `0.0199` n `6`; index avg `0.0575` n `25`; metal avg `0.1562` n `20`; unknown avg `0.1712` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
