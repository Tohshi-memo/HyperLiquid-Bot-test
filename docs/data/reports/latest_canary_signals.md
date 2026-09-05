# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T07:52:41.287023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1245` n `232`; crypto_major avg `-0.0708` n `8`; equity avg `-0.0023` n `134`; fx avg `0.0093` n `6`; index avg `-0.0217` n `26`; metal avg `0.0033` n `20`; unknown avg `0.0064` n `792`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `0.0671` n `232`; crypto_major avg `0.344` n `8`; equity avg `-0.0223` n `134`; fx avg `0.0028` n `6`; index avg `-0.0042` n `26`; metal avg `0.008` n `20`; unknown avg `0.2592` n `788`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.8384` n `232`; crypto_major avg `0.5838` n `8`; equity avg `0.1113` n `134`; fx avg `-0.0215` n `6`; index avg `0.0139` n `26`; metal avg `0.0224` n `20`; unknown avg `5.7452` n `744`
- 24h: commodity avg `0.1969` n `12`; crypto_alt avg `1.1698` n `232`; crypto_major avg `-1.0024` n `8`; equity avg `1.0648` n `134`; fx avg `-0.1382` n `6`; index avg `0.0694` n `26`; metal avg `-0.2103` n `20`; unknown avg `16.3476` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
