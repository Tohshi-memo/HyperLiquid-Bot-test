# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T00:07:28.452956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0808` n `232`; crypto_major avg `0.0244` n `8`; equity avg `0.0124` n `134`; fx avg `-0.056` n `6`; index avg `0.0091` n `26`; metal avg `0.0009` n `20`; unknown avg `0.0574` n `795`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.419` n `232`; crypto_major avg `0.1155` n `8`; equity avg `0.1399` n `134`; fx avg `-0.0818` n `6`; index avg `0.0246` n `26`; metal avg `0.0901` n `20`; unknown avg `0.3193` n `795`
- 4h: commodity avg `0.0194` n `12`; crypto_alt avg `0.2722` n `232`; crypto_major avg `0.0761` n `8`; equity avg `-0.0693` n `134`; fx avg `-0.1009` n `6`; index avg `-0.0291` n `26`; metal avg `0.0991` n `20`; unknown avg `2.5894` n `764`
- 24h: commodity avg `0.2071` n `12`; crypto_alt avg `-0.3939` n `232`; crypto_major avg `-1.5017` n `8`; equity avg `0.3183` n `134`; fx avg `-0.2589` n `6`; index avg `0.0687` n `26`; metal avg `0.174` n `20`; unknown avg `7764.7158` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
