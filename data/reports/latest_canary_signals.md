# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T08:37:30.642308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.0348` n `8`; equity avg `0.1864` n `102`; fx avg `0.0096` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0182` n `20`; unknown avg `-0.1306` n `777`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0908` n `230`; crypto_major avg `-0.2147` n `8`; equity avg `-0.2549` n `102`; fx avg `0.0284` n `6`; index avg `-0.0963` n `25`; metal avg `-0.1303` n `20`; unknown avg `-0.2713` n `777`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `0.3327` n `230`; crypto_major avg `0.5181` n `8`; equity avg `1.7262` n `102`; fx avg `0.0935` n `6`; index avg `0.3832` n `25`; metal avg `0.1036` n `20`; unknown avg `-0.0618` n `761`
- 24h: commodity avg `0.1343` n `12`; crypto_alt avg `-1.2848` n `230`; crypto_major avg `0.9656` n `8`; equity avg `-1.4957` n `102`; fx avg `-0.096` n `6`; index avg `-0.2432` n `25`; metal avg `-0.0822` n `20`; unknown avg `-0.5346` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
