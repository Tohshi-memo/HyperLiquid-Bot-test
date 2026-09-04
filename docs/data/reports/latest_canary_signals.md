# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T09:07:27.311179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0467` n `12`; crypto_alt avg `0.3685` n `232`; crypto_major avg `0.2139` n `8`; equity avg `0.0355` n `133`; fx avg `-0.0059` n `6`; index avg `0.0062` n `26`; metal avg `-0.0383` n `20`; unknown avg `0.0939` n `791`
- 1h: commodity avg `0.0275` n `12`; crypto_alt avg `0.7252` n `232`; crypto_major avg `0.6298` n `8`; equity avg `0.0808` n `133`; fx avg `-0.0141` n `6`; index avg `0.0036` n `26`; metal avg `-0.0781` n `20`; unknown avg `0.0492` n `785`
- 4h: commodity avg `-0.059` n `12`; crypto_alt avg `0.6933` n `232`; crypto_major avg `0.2023` n `8`; equity avg `0.1072` n `133`; fx avg `-0.0295` n `6`; index avg `0.013` n `26`; metal avg `0.0492` n `20`; unknown avg `0.5902` n `749`
- 24h: commodity avg `-0.2866` n `12`; crypto_alt avg `2.7324` n `232`; crypto_major avg `4.1779` n `8`; equity avg `1.9643` n `133`; fx avg `-0.0434` n `6`; index avg `0.3452` n `26`; metal avg `0.4185` n `20`; unknown avg `1.6469` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
