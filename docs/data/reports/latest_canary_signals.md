# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T20:39:48.169724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.106` n `230`; crypto_major avg `0.0734` n `8`; equity avg `-0.0408` n `102`; fx avg `-0.0039` n `6`; index avg `0.0671` n `25`; metal avg `0.1139` n `20`; unknown avg `0.0262` n `778`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.7917` n `230`; crypto_major avg `-0.3652` n `8`; equity avg `-1.5243` n `102`; fx avg `0.0029` n `6`; index avg `-0.3308` n `25`; metal avg `-0.1634` n `20`; unknown avg `-0.1105` n `778`
- 4h: commodity avg `0.109` n `12`; crypto_alt avg `-0.6227` n `230`; crypto_major avg `-0.2485` n `8`; equity avg `-0.9649` n `102`; fx avg `0.089` n `6`; index avg `-0.196` n `25`; metal avg `0.3293` n `20`; unknown avg `-0.5126` n `778`
- 24h: commodity avg `1.3566` n `12`; crypto_alt avg `-2.8618` n `230`; crypto_major avg `-0.8577` n `8`; equity avg `-3.8699` n `102`; fx avg `0.0106` n `6`; index avg `-0.6741` n `25`; metal avg `0.1594` n `20`; unknown avg `-0.7235` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
