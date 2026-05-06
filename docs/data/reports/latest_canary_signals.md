# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T21:07:15.201710+00:00`
- Correlation status: `ready`
- Asset price records: `488`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1129` n `12`; crypto_alt avg `0.374` n `228`; crypto_major avg `0.2244` n `8`; equity avg `-0.0495` n `65`; fx avg `-0.021` n `4`; index avg `-0.0012` n `23`; metal avg `0.0579` n `18`; unknown avg `0.0769` n `356`
- 1h: commodity avg `0.3195` n `12`; crypto_alt avg `-0.0553` n `228`; crypto_major avg `-0.2449` n `8`; equity avg `-0.3214` n `65`; fx avg `-0.0278` n `4`; index avg `-0.1598` n `23`; metal avg `-0.0784` n `18`; unknown avg `0.0081` n `356`
- 4h: commodity avg `0.348` n `12`; crypto_alt avg `-0.2078` n `228`; crypto_major avg `-0.2486` n `8`; equity avg `0.3753` n `65`; fx avg `-0.0374` n `4`; index avg `0.2875` n `23`; metal avg `0.2198` n `18`; unknown avg `-0.0239` n `356`
- 24h: commodity avg `-2.2214` n `7`; crypto_alt avg `1.7559` n `223`; crypto_major avg `0.0908` n `7`; equity avg `2.6949` n `47`; fx avg `-0.5002` n `4`; index avg `1.5118` n `6`; metal avg `3.4542` n `7`; unknown avg `3.7506` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1629`, n `480`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1509`, n `480`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1349`, n `480`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `484`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.125`, n `480`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `484`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `480`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `484`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `480`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `480`, weak_sample_signal
