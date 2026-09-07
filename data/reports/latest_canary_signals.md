# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T11:52:30.167961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `-0.0733` n `232`; crypto_major avg `-0.1089` n `8`; equity avg `0.0003` n `134`; fx avg `-0.0062` n `6`; index avg `0.0103` n `26`; metal avg `0.0563` n `20`; unknown avg `0.5988` n `796`
- 1h: commodity avg `0.1676` n `12`; crypto_alt avg `-0.143` n `232`; crypto_major avg `-0.1424` n `8`; equity avg `-0.1082` n `134`; fx avg `0.0281` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0466` n `20`; unknown avg `0.5437` n `794`
- 4h: commodity avg `0.228` n `12`; crypto_alt avg `0.9199` n `232`; crypto_major avg `0.2513` n `8`; equity avg `0.0156` n `134`; fx avg `-0.0601` n `6`; index avg `-0.0532` n `26`; metal avg `-0.0697` n `20`; unknown avg `0.6674` n `784`
- 24h: commodity avg `0.2159` n `12`; crypto_alt avg `-0.2147` n `232`; crypto_major avg `-0.9466` n `8`; equity avg `0.1992` n `134`; fx avg `-0.0749` n `6`; index avg `-0.0018` n `26`; metal avg `-0.1685` n `20`; unknown avg `75.5041` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
