# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T00:37:25.272672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.0885` n `232`; crypto_major avg `-0.0667` n `8`; equity avg `0.0863` n `133`; fx avg `0.0027` n `6`; index avg `0.0348` n `26`; metal avg `-0.009` n `20`; unknown avg `0.2003` n `792`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `0.1025` n `232`; crypto_major avg `-0.0562` n `8`; equity avg `-0.0715` n `133`; fx avg `0.0262` n `6`; index avg `-0.039` n `26`; metal avg `0.0078` n `20`; unknown avg `0.193` n `790`
- 4h: commodity avg `0.0544` n `12`; crypto_alt avg `-0.0778` n `232`; crypto_major avg `-0.2495` n `8`; equity avg `0.1726` n `133`; fx avg `0.0335` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0425` n `20`; unknown avg `-0.0514` n `784`
- 24h: commodity avg `0.0347` n `12`; crypto_alt avg `-0.1557` n `232`; crypto_major avg `-0.3581` n `8`; equity avg `0.893` n `133`; fx avg `-0.3077` n `6`; index avg `0.0586` n `26`; metal avg `0.4776` n `20`; unknown avg `-0.5813` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
