# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T13:07:28.250445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0113` n `230`; crypto_major avg `0.0042` n `8`; equity avg `-0.1104` n `102`; fx avg `-0.0115` n `6`; index avg `0.0263` n `25`; metal avg `0.016` n `20`; unknown avg `0.0957` n `777`
- 1h: commodity avg `0.3662` n `12`; crypto_alt avg `-0.1713` n `230`; crypto_major avg `-0.1416` n `8`; equity avg `-0.2306` n `102`; fx avg `0.0047` n `6`; index avg `-0.0416` n `25`; metal avg `-0.0943` n `20`; unknown avg `0.1258` n `777`
- 4h: commodity avg `0.5038` n `12`; crypto_alt avg `-0.4942` n `230`; crypto_major avg `-0.324` n `8`; equity avg `-0.3372` n `102`; fx avg `-0.0117` n `6`; index avg `-0.0182` n `25`; metal avg `-0.1589` n `20`; unknown avg `0.6802` n `777`
- 24h: commodity avg `0.4948` n `12`; crypto_alt avg `-1.7747` n `230`; crypto_major avg `0.777` n `8`; equity avg `-0.7704` n `102`; fx avg `-0.0797` n `6`; index avg `-0.1462` n `25`; metal avg `-0.1554` n `20`; unknown avg `0.0577` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
