# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T09:52:26.963345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `-0.0755` n `230`; crypto_major avg `-0.0901` n `8`; equity avg `-0.0976` n `102`; fx avg `-0.008` n `6`; index avg `-0.0232` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0182` n `779`
- 1h: commodity avg `-0.1499` n `12`; crypto_alt avg `-0.0184` n `230`; crypto_major avg `0.1868` n `8`; equity avg `0.3487` n `102`; fx avg `-0.0195` n `6`; index avg `0.0454` n `25`; metal avg `0.1465` n `20`; unknown avg `-0.022` n `771`
- 4h: commodity avg `-0.1891` n `12`; crypto_alt avg `0.1901` n `230`; crypto_major avg `0.5283` n `8`; equity avg `0.4386` n `102`; fx avg `0.0042` n `6`; index avg `0.0238` n `25`; metal avg `0.3836` n `20`; unknown avg `-0.0069` n `739`
- 24h: commodity avg `0.6181` n `12`; crypto_alt avg `-0.3914` n `230`; crypto_major avg `-0.3484` n `8`; equity avg `-3.419` n `102`; fx avg `-0.0011` n `6`; index avg `-0.49` n `25`; metal avg `0.32` n `20`; unknown avg `-0.1775` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
