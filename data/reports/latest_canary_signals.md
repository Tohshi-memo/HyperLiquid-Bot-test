# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T00:25:19.252824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.1561` n `232`; crypto_major avg `-0.1982` n `8`; equity avg `0.1945` n `134`; fx avg `-0.0018` n `6`; index avg `0.048` n `26`; metal avg `0.0351` n `20`; unknown avg `-0.0974` n `797`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.2745` n `232`; crypto_major avg `-0.0133` n `8`; equity avg `0.3603` n `134`; fx avg `-0.0668` n `6`; index avg `0.0822` n `26`; metal avg `0.1109` n `20`; unknown avg `0.3638` n `795`
- 4h: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.0038` n `232`; crypto_major avg `-0.1039` n `8`; equity avg `0.1545` n `134`; fx avg `-0.1016` n `6`; index avg `0.0155` n `26`; metal avg `0.1215` n `20`; unknown avg `11.6078` n `780`
- 24h: commodity avg `0.2096` n `12`; crypto_alt avg `-0.6033` n `232`; crypto_major avg `-1.533` n `8`; equity avg `0.4769` n `134`; fx avg `-0.2121` n `6`; index avg `0.1045` n `26`; metal avg `0.2075` n `20`; unknown avg `7765.3952` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
