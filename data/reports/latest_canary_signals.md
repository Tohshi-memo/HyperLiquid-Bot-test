# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T19:22:26.715117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0261` n `12`; crypto_alt avg `-0.4553` n `230`; crypto_major avg `-0.3242` n `8`; equity avg `-0.3338` n `96`; fx avg `0.0097` n `6`; index avg `-0.0501` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.1414` n `769`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `-0.1909` n `230`; crypto_major avg `-0.0454` n `8`; equity avg `-0.4866` n `96`; fx avg `0.0077` n `6`; index avg `-0.0714` n `25`; metal avg `-0.0512` n `20`; unknown avg `-0.0379` n `769`
- 4h: commodity avg `0.277` n `12`; crypto_alt avg `0.4527` n `230`; crypto_major avg `0.6283` n `8`; equity avg `0.5948` n `96`; fx avg `0.0521` n `6`; index avg `0.0301` n `25`; metal avg `-0.0128` n `20`; unknown avg `0.6698` n `769`
- 24h: commodity avg `0.6932` n `12`; crypto_alt avg `-1.2357` n `230`; crypto_major avg `-1.3896` n `8`; equity avg `-1.3558` n `94`; fx avg `0.0979` n `6`; index avg `-0.2239` n `25`; metal avg `-0.1006` n `20`; unknown avg `-0.0151` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
