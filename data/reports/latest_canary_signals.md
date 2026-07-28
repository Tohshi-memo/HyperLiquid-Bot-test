# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T20:07:34.977849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.0013` n `230`; crypto_major avg `0.043` n `8`; equity avg `-0.0012` n `102`; fx avg `-0.0151` n `6`; index avg `-0.0383` n `25`; metal avg `-0.0386` n `20`; unknown avg `0.9558` n `776`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `0.0912` n `230`; crypto_major avg `0.1803` n `8`; equity avg `0.0818` n `102`; fx avg `-0.016` n `6`; index avg `-0.083` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.8797` n `776`
- 4h: commodity avg `0.1281` n `12`; crypto_alt avg `-0.3815` n `230`; crypto_major avg `-0.0697` n `8`; equity avg `-0.0895` n `102`; fx avg `-0.0224` n `6`; index avg `-0.1541` n `25`; metal avg `-0.1889` n `20`; unknown avg `0.765` n `774`
- 24h: commodity avg `-0.8539` n `12`; crypto_alt avg `-2.0318` n `230`; crypto_major avg `-1.6731` n `8`; equity avg `-3.2545` n `102`; fx avg `-0.0936` n `6`; index avg `-0.4498` n `25`; metal avg `-0.4742` n `20`; unknown avg `1.0848` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
