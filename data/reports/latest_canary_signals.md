# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T04:37:32.900022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.0055` n `233`; crypto_major avg `0.0024` n `8`; equity avg `0.0431` n `134`; fx avg `-0.0095` n `6`; index avg `0.0121` n `26`; metal avg `-0.0162` n `20`; unknown avg `2.4155` n `791`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.0782` n `233`; crypto_major avg `0.0639` n `8`; equity avg `0.1539` n `134`; fx avg `-0.0189` n `6`; index avg `0.0303` n `26`; metal avg `0.0158` n `20`; unknown avg `1.6008` n `789`
- 4h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.0618` n `233`; crypto_major avg `0.29` n `8`; equity avg `-0.0666` n `134`; fx avg `-0.0119` n `6`; index avg `0.0377` n `26`; metal avg `0.0422` n `20`; unknown avg `8.8152` n `789`
- 24h: commodity avg `0.0226` n `12`; crypto_alt avg `-3.2777` n `233`; crypto_major avg `-2.1404` n `8`; equity avg `-1.0848` n `134`; fx avg `0.0307` n `6`; index avg `-0.1698` n `26`; metal avg `0.4335` n `20`; unknown avg `1.2758` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
