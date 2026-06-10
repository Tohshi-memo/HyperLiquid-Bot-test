# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T03:07:24.490729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.3913` n `228`; crypto_major avg `0.2514` n `8`; equity avg `0.072` n `74`; fx avg `0.0008` n `6`; index avg `-0.0561` n `23`; metal avg `-0.0933` n `18`; unknown avg `-0.0114` n `547`
- 1h: commodity avg `-0.1313` n `12`; crypto_alt avg `-0.5353` n `228`; crypto_major avg `-0.6834` n `8`; equity avg `-0.2403` n `74`; fx avg `0.0211` n `6`; index avg `-0.1185` n `23`; metal avg `-0.3112` n `18`; unknown avg `-0.2234` n `547`
- 4h: commodity avg `-0.0882` n `12`; crypto_alt avg `-0.3996` n `228`; crypto_major avg `-0.9805` n `8`; equity avg `-0.3698` n `74`; fx avg `-0.0155` n `6`; index avg `-0.2379` n `23`; metal avg `-1.4979` n `18`; unknown avg `-0.3675` n `547`
- 24h: commodity avg `-0.4656` n `12`; crypto_alt avg `-0.0936` n `228`; crypto_major avg `-2.9724` n `8`; equity avg `-2.6222` n `74`; fx avg `0.1286` n `6`; index avg `-1.1169` n `23`; metal avg `-3.0187` n `18`; unknown avg `-0.3358` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0379`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
