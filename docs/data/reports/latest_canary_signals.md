# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T00:37:26.577413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0752` n `12`; crypto_alt avg `-0.312` n `228`; crypto_major avg `-0.3706` n `8`; equity avg `-0.372` n `88`; fx avg `0.0026` n `6`; index avg `-0.0861` n `23`; metal avg `0.0142` n `20`; unknown avg `0.0182` n `764`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.7646` n `228`; crypto_major avg `-1.0531` n `8`; equity avg `-1.0001` n `88`; fx avg `0.0528` n `6`; index avg `-0.3059` n `23`; metal avg `-0.112` n `20`; unknown avg `1.7135` n `764`
- 4h: commodity avg `-0.1926` n `12`; crypto_alt avg `-0.9785` n `228`; crypto_major avg `-0.9673` n `8`; equity avg `-0.8049` n `88`; fx avg `0.0296` n `6`; index avg `-0.247` n `23`; metal avg `-0.3065` n `20`; unknown avg `-0.0672` n `762`
- 24h: commodity avg `-0.3281` n `12`; crypto_alt avg `-1.1664` n `228`; crypto_major avg `-1.3949` n `8`; equity avg `-0.5861` n `88`; fx avg `-0.025` n `6`; index avg `-0.1911` n `23`; metal avg `-0.316` n `20`; unknown avg `15.5217` n `690`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
