# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T22:22:25.495763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.279` n `232`; crypto_major avg `-0.2546` n `8`; equity avg `-0.0408` n `134`; fx avg `0.0178` n `6`; index avg `-0.0077` n `26`; metal avg `0.0217` n `20`; unknown avg `0.5651` n `793`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `-0.5434` n `232`; crypto_major avg `-0.6605` n `8`; equity avg `-0.0523` n `134`; fx avg `0.0189` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0716` n `20`; unknown avg `-0.0451` n `791`
- 4h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0385` n `232`; crypto_major avg `-0.2466` n `8`; equity avg `0.0191` n `134`; fx avg `0.0363` n `6`; index avg `0.0052` n `26`; metal avg `-0.0525` n `20`; unknown avg `0.4859` n `761`
- 24h: commodity avg `0.0007` n `12`; crypto_alt avg `0.6761` n `232`; crypto_major avg `-0.042` n `8`; equity avg `0.2772` n `134`; fx avg `0.0372` n `6`; index avg `-0.005` n `26`; metal avg `-0.0847` n `20`; unknown avg `153.4852` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
