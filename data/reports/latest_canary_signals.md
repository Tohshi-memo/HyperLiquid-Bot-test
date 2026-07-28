# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T21:07:37.192345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1131` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.036` n `8`; equity avg `0.1154` n `102`; fx avg `0.0109` n `6`; index avg `0.0108` n `25`; metal avg `0.012` n `20`; unknown avg `0.0349` n `776`
- 1h: commodity avg `0.0714` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `0.0488` n `8`; equity avg `0.6221` n `102`; fx avg `-0.0033` n `6`; index avg `0.0563` n `25`; metal avg `0.0219` n `20`; unknown avg `0.0297` n `776`
- 4h: commodity avg `0.174` n `12`; crypto_alt avg `-0.2446` n `230`; crypto_major avg `-0.1692` n `8`; equity avg `0.4641` n `102`; fx avg `-0.0305` n `6`; index avg `-0.0897` n `25`; metal avg `-0.1139` n `20`; unknown avg `0.7653` n `774`
- 24h: commodity avg `-0.8094` n `12`; crypto_alt avg `-2.131` n `230`; crypto_major avg `-1.6984` n `8`; equity avg `-2.7146` n `102`; fx avg `-0.0891` n `6`; index avg `-0.3855` n `25`; metal avg `-0.4281` n `20`; unknown avg `1.088` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
