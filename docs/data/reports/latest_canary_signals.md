# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T05:22:28.239915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `0.0017` n `8`; equity avg `0.1071` n `102`; fx avg `-0.001` n `6`; index avg `0.0331` n `25`; metal avg `0.0549` n `20`; unknown avg `-0.0313` n `777`
- 1h: commodity avg `-0.0869` n `12`; crypto_alt avg `0.3869` n `230`; crypto_major avg `0.3931` n `8`; equity avg `1.1105` n `102`; fx avg `-0.0218` n `6`; index avg `0.1345` n `25`; metal avg `0.1176` n `20`; unknown avg `-0.1032` n `777`
- 4h: commodity avg `-0.1164` n `12`; crypto_alt avg `-1.3326` n `230`; crypto_major avg `-0.1745` n `8`; equity avg `-1.2551` n `102`; fx avg `-0.1247` n `6`; index avg `-0.4434` n `25`; metal avg `0.09` n `20`; unknown avg `0.2608` n `777`
- 24h: commodity avg `-0.1316` n `12`; crypto_alt avg `-1.6335` n `230`; crypto_major avg `0.308` n `8`; equity avg `-2.158` n `102`; fx avg `-0.1971` n `6`; index avg `-0.4504` n `25`; metal avg `-0.029` n `20`; unknown avg `0.4225` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
