# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T00:52:23.798990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `-0.0907` n `232`; crypto_major avg `0.0429` n `8`; equity avg `-0.0033` n `134`; fx avg `-0.0078` n `6`; index avg `-0.0002` n `26`; metal avg `0.0548` n `20`; unknown avg `0.4031` n `792`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0463` n `232`; crypto_major avg `-0.1125` n `8`; equity avg `0.159` n `134`; fx avg `-0.1387` n `6`; index avg `0.0085` n `26`; metal avg `0.0402` n `20`; unknown avg `143.6941` n `784`
- 4h: commodity avg `-0.0084` n `12`; crypto_alt avg `0.63` n `232`; crypto_major avg `0.2619` n `8`; equity avg `0.1093` n `134`; fx avg `-0.095` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0478` n `20`; unknown avg `0.9904` n `779`
- 24h: commodity avg `-0.0405` n `12`; crypto_alt avg `1.1508` n `232`; crypto_major avg `0.7312` n `8`; equity avg `0.3542` n `134`; fx avg `-0.0833` n `6`; index avg `0.0068` n `26`; metal avg `-0.0545` n `20`; unknown avg `150.4948` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
