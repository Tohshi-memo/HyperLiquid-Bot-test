# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T11:52:29.169211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `0.0179` n `8`; equity avg `-0.0463` n `79`; fx avg `0.0008` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0384` n `20`; unknown avg `-0.0564` n `722`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `0.7385` n `228`; crypto_major avg `0.7088` n `8`; equity avg `0.1394` n `79`; fx avg `-0.0236` n `6`; index avg `0.0528` n `23`; metal avg `-0.0751` n `20`; unknown avg `0.2378` n `722`
- 4h: commodity avg `-0.2057` n `12`; crypto_alt avg `0.8719` n `228`; crypto_major avg `0.6899` n `8`; equity avg `0.2623` n `79`; fx avg `0.0233` n `6`; index avg `0.1094` n `23`; metal avg `0.0474` n `18`; unknown avg `0.392` n `701`
- 24h: commodity avg `-0.2551` n `12`; crypto_alt avg `0.9657` n `228`; crypto_major avg `1.0844` n `8`; equity avg `0.0872` n `79`; fx avg `0.0371` n `6`; index avg `0.1177` n `23`; metal avg `0.444` n `18`; unknown avg `0.8093` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
