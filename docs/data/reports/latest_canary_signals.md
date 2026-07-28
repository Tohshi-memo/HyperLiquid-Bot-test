# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T19:51:05.865080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `0.03` n `8`; equity avg `-0.0156` n `102`; fx avg `0.003` n `6`; index avg `-0.0282` n `25`; metal avg `0.0115` n `20`; unknown avg `0.0208` n `776`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `0.2247` n `230`; crypto_major avg `0.338` n `8`; equity avg `0.2974` n `102`; fx avg `-0.0089` n `6`; index avg `-0.0068` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0673` n `775`
- 4h: commodity avg `0.0508` n `12`; crypto_alt avg `-0.3202` n `230`; crypto_major avg `-0.0385` n `8`; equity avg `-0.0228` n `102`; fx avg `-0.0013` n `6`; index avg `-0.1095` n `25`; metal avg `-0.1429` n `20`; unknown avg `-0.2981` n `774`
- 24h: commodity avg `-0.9019` n `12`; crypto_alt avg `-1.9509` n `230`; crypto_major avg `-1.7323` n `8`; equity avg `-3.1071` n `102`; fx avg `-0.086` n `6`; index avg `-0.3858` n `25`; metal avg `-0.4667` n `20`; unknown avg `-0.4683` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
