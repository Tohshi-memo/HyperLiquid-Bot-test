# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T00:22:15.901698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.3665` n `228`; crypto_major avg `0.2467` n `8`; equity avg `0.0136` n `65`; fx avg `-0.0297` n `5`; index avg `-0.0008` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.0927` n `376`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.1065` n `228`; crypto_major avg `0.0769` n `8`; equity avg `0.0611` n `65`; fx avg `0.0008` n `5`; index avg `0.0059` n `23`; metal avg `0.0323` n `18`; unknown avg `-0.2448` n `376`
- 4h: commodity avg `-0.0708` n `12`; crypto_alt avg `-0.3165` n `228`; crypto_major avg `-0.0892` n `8`; equity avg `0.2379` n `65`; fx avg `-0.0127` n `5`; index avg `0.1176` n `23`; metal avg `0.1008` n `18`; unknown avg `-0.2455` n `376`
- 24h: commodity avg `0.5003` n `12`; crypto_alt avg `-0.5127` n `228`; crypto_major avg `0.1086` n `8`; equity avg `0.7917` n `65`; fx avg `-0.0157` n `5`; index avg `0.4114` n `23`; metal avg `0.3834` n `18`; unknown avg `-0.0355` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
