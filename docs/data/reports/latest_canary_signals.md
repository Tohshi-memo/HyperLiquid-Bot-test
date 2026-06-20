# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T23:22:25.382194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.1389` n `228`; crypto_major avg `0.0224` n `8`; equity avg `0.0267` n `78`; fx avg `-0.0038` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0069` n `18`; unknown avg `0.1132` n `701`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `0.3153` n `228`; crypto_major avg `0.2187` n `8`; equity avg `0.1108` n `78`; fx avg `-0.0014` n `6`; index avg `0.0206` n `23`; metal avg `-0.0077` n `18`; unknown avg `71.0575` n `701`
- 4h: commodity avg `0.0211` n `12`; crypto_alt avg `0.8724` n `228`; crypto_major avg `0.9713` n `8`; equity avg `0.2893` n `78`; fx avg `0.002` n `6`; index avg `0.0382` n `23`; metal avg `-0.0049` n `18`; unknown avg `0.4732` n `701`
- 24h: commodity avg `0.3468` n `12`; crypto_alt avg `1.4514` n `228`; crypto_major avg `1.9182` n `8`; equity avg `0.5557` n `78`; fx avg `0.0796` n `6`; index avg `0.0949` n `23`; metal avg `-0.0402` n `18`; unknown avg `-0.462` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
