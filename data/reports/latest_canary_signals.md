# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T00:52:25.033789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.1993` n `232`; crypto_major avg `0.0683` n `8`; equity avg `0.1327` n `134`; fx avg `0.009` n `6`; index avg `0.0343` n `26`; metal avg `-0.0284` n `20`; unknown avg `0.4932` n `797`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.4101` n `232`; crypto_major avg `0.1262` n `8`; equity avg `0.3706` n `134`; fx avg `-0.0597` n `6`; index avg `0.0923` n `26`; metal avg `0.008` n `20`; unknown avg `5.4057` n `789`
- 4h: commodity avg `-0.0286` n `12`; crypto_alt avg `0.2798` n `232`; crypto_major avg `0.013` n `8`; equity avg `0.2874` n `134`; fx avg `-0.1104` n `6`; index avg `0.0543` n `26`; metal avg `0.0913` n `20`; unknown avg `5.4757` n `780`
- 24h: commodity avg `0.1396` n `12`; crypto_alt avg `0.0157` n `232`; crypto_major avg `-1.2529` n `8`; equity avg `0.661` n `134`; fx avg `-0.1429` n `6`; index avg `0.1459` n `26`; metal avg `0.1434` n `20`; unknown avg `7766.6225` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
