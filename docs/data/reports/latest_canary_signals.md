# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T18:22:03.221456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0439` n `228`; crypto_major avg `0.0831` n `8`; equity avg `0.0452` n `74`; fx avg `0.0362` n `6`; index avg `0.0084` n `23`; metal avg `-0.287` n `18`; unknown avg `-0.0459` n `644`
- 1h: commodity avg `-0.1891` n `12`; crypto_alt avg `-0.1619` n `228`; crypto_major avg `0.031` n `8`; equity avg `0.1185` n `74`; fx avg `0.033` n `6`; index avg `-0.1069` n `23`; metal avg `-0.2779` n `18`; unknown avg `0.0587` n `644`
- 4h: commodity avg `-0.2921` n `12`; crypto_alt avg `0.1742` n `228`; crypto_major avg `-0.2571` n `8`; equity avg `0.1398` n `74`; fx avg `0.0393` n `6`; index avg `-0.055` n `23`; metal avg `-0.1958` n `18`; unknown avg `-1.9966` n `644`
- 24h: commodity avg `-0.8819` n `12`; crypto_alt avg `2.1926` n `228`; crypto_major avg `0.2241` n `8`; equity avg `0.2585` n `74`; fx avg `0.0467` n `6`; index avg `0.5376` n `23`; metal avg `-0.1033` n `18`; unknown avg `-1.8363` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
