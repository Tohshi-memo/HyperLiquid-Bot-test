# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T03:07:27.288255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `0.1233` n `228`; crypto_major avg `0.0502` n `8`; equity avg `0.0352` n `88`; fx avg `-0.0001` n `6`; index avg `-0.0176` n `23`; metal avg `0.0092` n `20`; unknown avg `0.0776` n `764`
- 1h: commodity avg `-0.0915` n `12`; crypto_alt avg `-0.1331` n `228`; crypto_major avg `-0.1832` n `8`; equity avg `0.024` n `88`; fx avg `-0.0048` n `6`; index avg `-0.0298` n `23`; metal avg `0.0054` n `20`; unknown avg `15.875` n `722`
- 4h: commodity avg `0.3251` n `12`; crypto_alt avg `-0.0811` n `228`; crypto_major avg `-0.458` n `8`; equity avg `-0.1062` n `88`; fx avg `-0.0424` n `6`; index avg `-0.0762` n `23`; metal avg `0.0281` n `20`; unknown avg `15.514` n `722`
- 24h: commodity avg `0.3735` n `12`; crypto_alt avg `-0.8078` n `228`; crypto_major avg `-1.1616` n `8`; equity avg `0.0438` n `88`; fx avg `-0.0185` n `6`; index avg `-0.1504` n `23`; metal avg `-0.0485` n `20`; unknown avg `6.0614` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2169`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
