# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T22:37:25.118839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.064` n `233`; crypto_major avg `-0.0191` n `8`; equity avg `0.0099` n `134`; fx avg `0.006` n `6`; index avg `-0.007` n `26`; metal avg `0.0063` n `20`; unknown avg `0.0765` n `797`
- 1h: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0267` n `233`; crypto_major avg `0.1417` n `8`; equity avg `-0.0272` n `134`; fx avg `-0.0065` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0642` n `20`; unknown avg `-0.0915` n `763`
- 4h: commodity avg `0.1626` n `12`; crypto_alt avg `-0.5851` n `233`; crypto_major avg `-0.2335` n `8`; equity avg `-0.5151` n `134`; fx avg `-0.0416` n `6`; index avg `-0.1281` n `26`; metal avg `-0.2344` n `20`; unknown avg `0.4926` n `725`
- 24h: commodity avg `0.0586` n `12`; crypto_alt avg `0.1295` n `232`; crypto_major avg `0.4362` n `8`; equity avg `0.434` n `134`; fx avg `-0.1102` n `6`; index avg `-0.1514` n `26`; metal avg `-0.3254` n `20`; unknown avg `1.0586` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
