# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T04:07:26.243151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `0.0506` n `230`; crypto_major avg `-0.0285` n `8`; equity avg `-0.143` n `102`; fx avg `-0.0158` n `6`; index avg `-0.0373` n `25`; metal avg `0.0212` n `20`; unknown avg `0.2092` n `784`
- 1h: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.1186` n `230`; crypto_major avg `-0.1385` n `8`; equity avg `-0.0366` n `102`; fx avg `-0.0156` n `6`; index avg `-0.0117` n `25`; metal avg `0.0137` n `20`; unknown avg `0.612` n `784`
- 4h: commodity avg `-0.1461` n `12`; crypto_alt avg `-0.6566` n `230`; crypto_major avg `-0.6988` n `8`; equity avg `0.5652` n `102`; fx avg `-0.2362` n `6`; index avg `0.0198` n `25`; metal avg `-0.0491` n `20`; unknown avg `0.1538` n `784`
- 24h: commodity avg `-0.1474` n `12`; crypto_alt avg `-0.6703` n `230`; crypto_major avg `-0.5284` n `8`; equity avg `0.8639` n `102`; fx avg `-0.2466` n `6`; index avg `0.0038` n `25`; metal avg `-0.0191` n `20`; unknown avg `1.2817` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
