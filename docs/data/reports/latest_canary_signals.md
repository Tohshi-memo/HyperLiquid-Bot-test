# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T16:37:38.403939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0366` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0408` n `12`; crypto_alt avg `-0.1833` n `228`; crypto_major avg `-0.1596` n `8`; equity avg `-0.1733` n `85`; fx avg `-0.0046` n `6`; index avg `-0.0194` n `23`; metal avg `0.0591` n `20`; unknown avg `0.0523` n `717`
- 1h: commodity avg `0.0949` n `12`; crypto_alt avg `-0.616` n `228`; crypto_major avg `-0.7356` n `8`; equity avg `-0.4014` n `85`; fx avg `-0.0041` n `6`; index avg `0.0041` n `23`; metal avg `-0.0671` n `20`; unknown avg `0.2218` n `716`
- 4h: commodity avg `-0.127` n `12`; crypto_alt avg `-0.9916` n `228`; crypto_major avg `-1.0991` n `8`; equity avg `-1.1445` n `85`; fx avg `-0.0791` n `6`; index avg `-0.0625` n `23`; metal avg `-0.2362` n `20`; unknown avg `0.2664` n `716`
- 24h: commodity avg `-0.8075` n `12`; crypto_alt avg `-0.2174` n `228`; crypto_major avg `0.0499` n `8`; equity avg `-0.8051` n `85`; fx avg `-0.0255` n `6`; index avg `0.0924` n `23`; metal avg `0.1943` n `18`; unknown avg `1.0976` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
