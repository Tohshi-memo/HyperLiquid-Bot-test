# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T05:52:26.653851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0521` n `12`; crypto_alt avg `-0.1573` n `232`; crypto_major avg `-0.1135` n `8`; equity avg `0.0187` n `134`; fx avg `-0.0005` n `6`; index avg `0.0063` n `26`; metal avg `-0.0423` n `20`; unknown avg `1.135` n `796`
- 1h: commodity avg `0.0668` n `12`; crypto_alt avg `0.3866` n `232`; crypto_major avg `0.3689` n `8`; equity avg `0.0124` n `134`; fx avg `-0.029` n `6`; index avg `0.0145` n `26`; metal avg `0.0555` n `20`; unknown avg `1.1759` n `792`
- 4h: commodity avg `0.2204` n `12`; crypto_alt avg `0.3477` n `232`; crypto_major avg `0.1083` n `8`; equity avg `0.2507` n `134`; fx avg `0.025` n `6`; index avg `0.0056` n `26`; metal avg `-0.1061` n `20`; unknown avg `0.5673` n `758`
- 24h: commodity avg `0.1365` n `12`; crypto_alt avg `0.0098` n `232`; crypto_major avg `-0.7643` n `8`; equity avg `0.4227` n `134`; fx avg `-0.0125` n `6`; index avg `0.0161` n `26`; metal avg `-0.1817` n `20`; unknown avg `73.3127` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
