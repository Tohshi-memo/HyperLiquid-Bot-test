# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T06:22:27.229003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.2454` n `228`; crypto_major avg `-0.3552` n `8`; equity avg `-0.1034` n `88`; fx avg `0.0219` n `6`; index avg `-0.0054` n `23`; metal avg `0.021` n `20`; unknown avg `3.8111` n `765`
- 1h: commodity avg `-0.1506` n `12`; crypto_alt avg `-0.5424` n `228`; crypto_major avg `-0.6621` n `8`; equity avg `-0.2052` n `88`; fx avg `0.0285` n `6`; index avg `-0.0238` n `23`; metal avg `-0.0768` n `20`; unknown avg `0.0354` n `745`
- 4h: commodity avg `-0.1128` n `12`; crypto_alt avg `0.43` n `228`; crypto_major avg `-0.1418` n `8`; equity avg `0.1208` n `88`; fx avg `-0.016` n `6`; index avg `0.0294` n `23`; metal avg `-0.1632` n `20`; unknown avg `0.1945` n `745`
- 24h: commodity avg `0.0714` n `12`; crypto_alt avg `-0.7003` n `228`; crypto_major avg `-0.4856` n `8`; equity avg `0.3675` n `88`; fx avg `0.1234` n `6`; index avg `-0.0416` n `23`; metal avg `-0.4715` n `20`; unknown avg `-0.1732` n `745`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
