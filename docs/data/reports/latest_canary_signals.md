# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T17:22:35.580585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2683` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.1655` n `228`; crypto_major avg `-0.1596` n `8`; equity avg `0.1516` n `85`; fx avg `-0.0077` n `6`; index avg `0.0161` n `23`; metal avg `0.0089` n `20`; unknown avg `0.4811` n `717`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.2909` n `228`; crypto_major avg `-0.2101` n `8`; equity avg `0.0313` n `85`; fx avg `-0.0138` n `6`; index avg `0.0062` n `23`; metal avg `0.0899` n `20`; unknown avg `-0.1222` n `717`
- 4h: commodity avg `-0.1158` n `12`; crypto_alt avg `-1.0962` n `228`; crypto_major avg `-1.3255` n `8`; equity avg `-1.0311` n `85`; fx avg `-0.0665` n `6`; index avg `-0.0572` n `23`; metal avg `-0.2434` n `20`; unknown avg `0.2887` n `716`
- 24h: commodity avg `-0.8517` n `12`; crypto_alt avg `-0.5736` n `228`; crypto_major avg `-0.3386` n `8`; equity avg `-0.6251` n `85`; fx avg `0.0484` n `6`; index avg `0.135` n `23`; metal avg `0.2304` n `18`; unknown avg `0.87` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
