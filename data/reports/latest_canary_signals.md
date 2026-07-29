# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T10:37:29.535000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `-0.0752` n `230`; crypto_major avg `-0.1068` n `8`; equity avg `-0.2179` n `102`; fx avg `0.0078` n `6`; index avg `-0.0344` n `25`; metal avg `0.0049` n `20`; unknown avg `0.0127` n `777`
- 1h: commodity avg `0.1203` n `12`; crypto_alt avg `-0.183` n `230`; crypto_major avg `-0.14` n `8`; equity avg `-0.0815` n `102`; fx avg `-0.0048` n `6`; index avg `0.0271` n `25`; metal avg `-0.059` n `20`; unknown avg `0.0372` n `777`
- 4h: commodity avg `0.1482` n `12`; crypto_alt avg `-0.0811` n `230`; crypto_major avg `-0.1848` n `8`; equity avg `0.7344` n `102`; fx avg `0.044` n `6`; index avg `0.1859` n `25`; metal avg `-0.1569` n `20`; unknown avg `-0.1483` n `777`
- 24h: commodity avg `0.1416` n `12`; crypto_alt avg `-1.187` n `230`; crypto_major avg `1.2176` n `8`; equity avg `-0.4896` n `102`; fx avg `-0.0556` n `6`; index avg `0.0018` n `25`; metal avg `0.0926` n `20`; unknown avg `-0.5212` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
