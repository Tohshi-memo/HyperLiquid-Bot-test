# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T01:22:33.413023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.2007` n `232`; crypto_major avg `0.1336` n `8`; equity avg `-0.0207` n `134`; fx avg `-0.0244` n `6`; index avg `0.0059` n `26`; metal avg `0.0775` n `20`; unknown avg `1.1601` n `797`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `0.7344` n `232`; crypto_major avg `0.4394` n `8`; equity avg `0.0978` n `134`; fx avg `-0.0329` n `6`; index avg `0.0218` n `26`; metal avg `0.0586` n `20`; unknown avg `121.9818` n `789`
- 4h: commodity avg `-0.0492` n `12`; crypto_alt avg `0.3744` n `232`; crypto_major avg `0.2082` n `8`; equity avg `0.1857` n `134`; fx avg `-0.1364` n `6`; index avg `0.0354` n `26`; metal avg `0.1763` n `20`; unknown avg `8.21` n `788`
- 24h: commodity avg `0.1272` n `12`; crypto_alt avg `1.0895` n `232`; crypto_major avg `-0.5309` n `8`; equity avg `0.6725` n `134`; fx avg `-0.1733` n `6`; index avg `0.1263` n `26`; metal avg `0.4077` n `20`; unknown avg `7921.8585` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
