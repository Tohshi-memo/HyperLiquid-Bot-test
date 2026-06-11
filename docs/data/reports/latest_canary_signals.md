# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T00:37:26.150064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0655` n `12`; crypto_alt avg `-0.144` n `228`; crypto_major avg `-0.1949` n `8`; equity avg `-0.0797` n `74`; fx avg `0.0012` n `6`; index avg `-0.0623` n `23`; metal avg `-0.0331` n `18`; unknown avg `-0.0034` n `550`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.5966` n `228`; crypto_major avg `0.2543` n `8`; equity avg `0.4175` n `74`; fx avg `0.0593` n `6`; index avg `0.0318` n `23`; metal avg `0.167` n `18`; unknown avg `0.0288` n `550`
- 4h: commodity avg `0.4337` n `12`; crypto_alt avg `0.0885` n `228`; crypto_major avg `-0.0828` n `8`; equity avg `-0.2829` n `74`; fx avg `0.0291` n `6`; index avg `-0.0673` n `23`; metal avg `-0.2727` n `18`; unknown avg `-0.1319` n `550`
- 24h: commodity avg `1.2034` n `12`; crypto_alt avg `-1.4282` n `228`; crypto_major avg `-1.6924` n `8`; equity avg `-2.1161` n `74`; fx avg `0.0678` n `6`; index avg `-1.6008` n `23`; metal avg `-1.7347` n `18`; unknown avg `-0.4353` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
