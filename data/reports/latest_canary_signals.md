# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T12:37:27.908446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0789` n `12`; crypto_alt avg `0.0856` n `228`; crypto_major avg `0.2127` n `8`; equity avg `0.0672` n `79`; fx avg `0.0068` n `6`; index avg `0.0148` n `23`; metal avg `-0.0885` n `20`; unknown avg `0.0106` n `722`
- 1h: commodity avg `-0.1723` n `12`; crypto_alt avg `0.2428` n `228`; crypto_major avg `0.2121` n `8`; equity avg `0.1492` n `79`; fx avg `0.0354` n `6`; index avg `0.0186` n `23`; metal avg `-0.0375` n `20`; unknown avg `0.0002` n `722`
- 4h: commodity avg `-0.3074` n `12`; crypto_alt avg `1.3186` n `228`; crypto_major avg `1.0966` n `8`; equity avg `0.5371` n `79`; fx avg `0.061` n `6`; index avg `0.1491` n `23`; metal avg `0.095` n `18`; unknown avg `0.6705` n `701`
- 24h: commodity avg `-0.627` n `12`; crypto_alt avg `1.1144` n `228`; crypto_major avg `1.4275` n `8`; equity avg `0.3056` n `79`; fx avg `0.0371` n `6`; index avg `0.1556` n `23`; metal avg `0.4721` n `18`; unknown avg `0.7398` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
