# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T08:52:26.103024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `0.2369` n `229`; crypto_major avg `0.4013` n `8`; equity avg `0.1269` n `91`; fx avg `0.0111` n `6`; index avg `0.0269` n `25`; metal avg `-0.1741` n `20`; unknown avg `0.0621` n `763`
- 1h: commodity avg `0.6531` n `12`; crypto_alt avg `-0.6515` n `229`; crypto_major avg `-0.7635` n `8`; equity avg `-1.5419` n `91`; fx avg `0.0807` n `6`; index avg `-0.2903` n `25`; metal avg `-0.8002` n `20`; unknown avg `0.0408` n `763`
- 4h: commodity avg `0.6021` n `12`; crypto_alt avg `-0.687` n `229`; crypto_major avg `-0.7376` n `8`; equity avg `-1.5352` n `91`; fx avg `0.03` n `6`; index avg `-0.3407` n `25`; metal avg `-0.8531` n `20`; unknown avg `-0.3624` n `743`
- 24h: commodity avg `1.2592` n `12`; crypto_alt avg `-3.2695` n `229`; crypto_major avg `-2.7891` n `8`; equity avg `-3.0665` n `91`; fx avg `-0.1342` n `6`; index avg `-0.6377` n `25`; metal avg `-0.9246` n `20`; unknown avg `-0.7325` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
