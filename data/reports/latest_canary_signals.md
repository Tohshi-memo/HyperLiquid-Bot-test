# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T09:22:21.173100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0605` n `12`; crypto_alt avg `0.2444` n `228`; crypto_major avg `0.1557` n `8`; equity avg `0.1216` n `67`; fx avg `-0.0208` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0541` n `18`; unknown avg `-0.0812` n `386`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0425` n `228`; crypto_major avg `0.2051` n `8`; equity avg `-0.5541` n `67`; fx avg `-0.0226` n `6`; index avg `-0.1486` n `23`; metal avg `-0.3538` n `18`; unknown avg `-0.4108` n `386`
- 4h: commodity avg `0.4603` n `12`; crypto_alt avg `0.02` n `228`; crypto_major avg `0.2854` n `8`; equity avg `-0.5014` n `67`; fx avg `-0.0078` n `6`; index avg `-0.0596` n `23`; metal avg `-0.6156` n `18`; unknown avg `-0.5663` n `376`
- 24h: commodity avg `0.1293` n `12`; crypto_alt avg `1.6319` n `228`; crypto_major avg `0.0365` n `8`; equity avg `0.7888` n `67`; fx avg `0.1115` n `6`; index avg `0.5231` n `23`; metal avg `-0.163` n `18`; unknown avg `0.9114` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0365`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0329`, n `668`, weak_sample_signal
