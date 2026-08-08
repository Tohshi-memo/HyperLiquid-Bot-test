# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:07:30.330956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.0819` n `8`; equity avg `-0.0091` n `112`; fx avg `0.001` n `6`; index avg `0.002` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.0251` n `784`
- 1h: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.1064` n `230`; crypto_major avg `-0.1953` n `8`; equity avg `0.0155` n `112`; fx avg `0.0026` n `6`; index avg `0.0064` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0492` n `784`
- 4h: commodity avg `0.0376` n `12`; crypto_alt avg `-0.0512` n `230`; crypto_major avg `-0.2218` n `8`; equity avg `0.1437` n `112`; fx avg `0.004` n `6`; index avg `0.0141` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.209` n `784`
- 24h: commodity avg `0.2236` n `12`; crypto_alt avg `1.7307` n `230`; crypto_major avg `1.0952` n `8`; equity avg `0.6922` n `112`; fx avg `-0.0105` n `6`; index avg `0.036` n `25`; metal avg `0.0027` n `20`; unknown avg `0.1891` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
