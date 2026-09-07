# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T08:22:25.529097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0466` n `12`; crypto_alt avg `0.2771` n `232`; crypto_major avg `0.0629` n `8`; equity avg `0.056` n `134`; fx avg `-0.0932` n `6`; index avg `-0.0064` n `26`; metal avg `0.0603` n `20`; unknown avg `1.2727` n `796`
- 1h: commodity avg `-0.1804` n `12`; crypto_alt avg `-0.1351` n `232`; crypto_major avg `-0.2191` n `8`; equity avg `0.0034` n `134`; fx avg `-0.1199` n `6`; index avg `0.0081` n `26`; metal avg `0.1739` n `20`; unknown avg `1.4931` n `794`
- 4h: commodity avg `-0.1952` n `12`; crypto_alt avg `-0.1624` n `232`; crypto_major avg `-0.2348` n `8`; equity avg `0.0382` n `134`; fx avg `-0.1786` n `6`; index avg `0.0506` n `26`; metal avg `0.2042` n `20`; unknown avg `1.7219` n `758`
- 24h: commodity avg `-0.1513` n `12`; crypto_alt avg `0.2255` n `232`; crypto_major avg `-0.6724` n `8`; equity avg `0.4469` n `134`; fx avg `-0.1486` n `6`; index avg `0.0556` n `26`; metal avg `0.0292` n `20`; unknown avg `383.1848` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
