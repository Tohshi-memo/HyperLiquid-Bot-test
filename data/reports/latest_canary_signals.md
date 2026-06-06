# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T17:52:26.936103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `-0.3173` n `228`; crypto_major avg `-0.2623` n `8`; equity avg `-0.0741` n `74`; fx avg `0.116` n `6`; index avg `-0.015` n `23`; metal avg `-0.0194` n `18`; unknown avg `3.6427` n `515`
- 1h: commodity avg `0.1208` n `12`; crypto_alt avg `-0.8734` n `228`; crypto_major avg `-0.6794` n `8`; equity avg `-0.2551` n `74`; fx avg `0.1005` n `6`; index avg `-0.0553` n `23`; metal avg `0.025` n `18`; unknown avg `0.1598` n `515`
- 4h: commodity avg `0.246` n `12`; crypto_alt avg `-1.01` n `228`; crypto_major avg `-0.9132` n `8`; equity avg `-0.1115` n `74`; fx avg `0.1785` n `6`; index avg `0.0161` n `23`; metal avg `-0.1474` n `18`; unknown avg `4.6748` n `515`
- 24h: commodity avg `0.6262` n `12`; crypto_alt avg `-2.4964` n `228`; crypto_major avg `-1.7635` n `8`; equity avg `-2.0264` n `74`; fx avg `0.1329` n `6`; index avg `-1.0349` n `23`; metal avg `-1.1582` n `18`; unknown avg `0.4157` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
