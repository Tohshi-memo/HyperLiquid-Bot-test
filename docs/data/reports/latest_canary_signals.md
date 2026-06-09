# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T12:37:26.394408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.042` n `12`; crypto_alt avg `0.0191` n `228`; crypto_major avg `-0.0725` n `8`; equity avg `0.1133` n `74`; fx avg `0.0266` n `6`; index avg `0.0379` n `23`; metal avg `0.053` n `18`; unknown avg `0.0409` n `547`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.4587` n `228`; crypto_major avg `0.1686` n `8`; equity avg `-0.0594` n `74`; fx avg `0.0465` n `6`; index avg `0.0052` n `23`; metal avg `0.1759` n `18`; unknown avg `0.133` n `547`
- 4h: commodity avg `0.0459` n `12`; crypto_alt avg `0.0951` n `228`; crypto_major avg `-0.3823` n `8`; equity avg `0.2264` n `74`; fx avg `0.166` n `6`; index avg `0.1558` n `23`; metal avg `0.3849` n `18`; unknown avg `-0.1389` n `547`
- 24h: commodity avg `-0.3051` n `12`; crypto_alt avg `-0.9064` n `228`; crypto_major avg `-0.5312` n `8`; equity avg `1.1627` n `74`; fx avg `0.1811` n `6`; index avg `0.6041` n `23`; metal avg `0.3281` n `18`; unknown avg `-0.5326` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
