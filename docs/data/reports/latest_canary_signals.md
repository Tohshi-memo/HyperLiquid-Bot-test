# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T11:07:38.963653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `-0.314` n `230`; crypto_major avg `-0.2639` n `8`; equity avg `-0.3393` n `102`; fx avg `-0.0015` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0471` n `774`
- 1h: commodity avg `0.0888` n `12`; crypto_alt avg `-0.2691` n `230`; crypto_major avg `-0.2156` n `8`; equity avg `-0.5497` n `102`; fx avg `-0.0009` n `6`; index avg `-0.0685` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0741` n `774`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.588` n `230`; crypto_major avg `-0.5529` n `8`; equity avg `-0.6726` n `102`; fx avg `-0.0384` n `6`; index avg `-0.1235` n `25`; metal avg `-0.2451` n `20`; unknown avg `-0.0605` n `774`
- 24h: commodity avg `-0.5375` n `12`; crypto_alt avg `-3.8714` n `230`; crypto_major avg `-4.0273` n `8`; equity avg `-4.7051` n `102`; fx avg `-0.1822` n `6`; index avg `-0.959` n `25`; metal avg `-0.6667` n `20`; unknown avg `996.7928` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
