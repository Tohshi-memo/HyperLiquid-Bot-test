# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T07:22:15.572518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0418` n `12`; crypto_alt avg `0.1331` n `228`; crypto_major avg `0.0454` n `8`; equity avg `0.1257` n `66`; fx avg `0.0007` n `6`; index avg `0.037` n `23`; metal avg `0.0646` n `18`; unknown avg `0.0006` n `384`
- 1h: commodity avg `-0.0643` n `12`; crypto_alt avg `0.2222` n `228`; crypto_major avg `0.0849` n `8`; equity avg `0.285` n `66`; fx avg `-0.0335` n `6`; index avg `0.0261` n `23`; metal avg `0.2638` n `18`; unknown avg `0.0185` n `384`
- 4h: commodity avg `-0.2922` n `12`; crypto_alt avg `1.2836` n `228`; crypto_major avg `0.8877` n `8`; equity avg `0.8708` n `66`; fx avg `-0.019` n `6`; index avg `0.3621` n `23`; metal avg `0.9893` n `18`; unknown avg `0.3053` n `374`
- 24h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.0641` n `228`; crypto_major avg `-0.2489` n `8`; equity avg `0.4262` n `66`; fx avg `-0.1641` n `6`; index avg `-0.4633` n `23`; metal avg `-1.1308` n `18`; unknown avg `0.0648` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
