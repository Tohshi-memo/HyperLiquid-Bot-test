# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T03:52:26.231769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `0.099` n `232`; crypto_major avg `0.0172` n `8`; equity avg `-0.0176` n `134`; fx avg `-0.0112` n `6`; index avg `-0.0073` n `26`; metal avg `0.0379` n `20`; unknown avg `0.2242` n `797`
- 1h: commodity avg `0.0753` n `12`; crypto_alt avg `0.1366` n `232`; crypto_major avg `-0.0391` n `8`; equity avg `0.2207` n `134`; fx avg `0.0037` n `6`; index avg `0.0417` n `26`; metal avg `0.1208` n `20`; unknown avg `-0.2736` n `795`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.1392` n `232`; crypto_major avg `-0.3694` n `8`; equity avg `0.5948` n `134`; fx avg `-0.1446` n `6`; index avg `0.1609` n `26`; metal avg `0.108` n `20`; unknown avg `4.8507` n `783`
- 24h: commodity avg `0.1191` n `12`; crypto_alt avg `0.8905` n `232`; crypto_major avg `-0.7948` n `8`; equity avg `0.8035` n `134`; fx avg `-0.3401` n `6`; index avg `0.2248` n `26`; metal avg `0.3828` n `20`; unknown avg `7374.5571` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
