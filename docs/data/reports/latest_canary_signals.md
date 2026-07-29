# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T05:52:35.578459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.0677` n `8`; equity avg `-0.1162` n `102`; fx avg `0.0205` n `6`; index avg `-0.0435` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0852` n `777`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `0.3907` n `230`; crypto_major avg `0.519` n `8`; equity avg `1.0021` n `102`; fx avg `0.048` n `6`; index avg `0.178` n `25`; metal avg `0.113` n `20`; unknown avg `0.2723` n `777`
- 4h: commodity avg `-0.1489` n `12`; crypto_alt avg `-0.7673` n `230`; crypto_major avg `0.4357` n `8`; equity avg `-0.1145` n `102`; fx avg `-0.0871` n `6`; index avg `-0.1748` n `25`; metal avg `0.1115` n `20`; unknown avg `-0.0689` n `777`
- 24h: commodity avg `-0.2422` n `12`; crypto_alt avg `-1.4722` n `230`; crypto_major avg `0.7104` n `8`; equity avg `-1.7832` n `102`; fx avg `-0.141` n `6`; index avg `-0.3714` n `25`; metal avg `0.0161` n `20`; unknown avg `0.4307` n `758`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
