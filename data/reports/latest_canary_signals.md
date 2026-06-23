# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T20:07:39.076561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `0.2986` n `228`; crypto_major avg `0.2787` n `8`; equity avg `0.0265` n `86`; fx avg `-0.0012` n `6`; index avg `0.0036` n `23`; metal avg `-0.0037` n `20`; unknown avg `0.1531` n `764`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `0.2938` n `228`; crypto_major avg `0.2636` n `8`; equity avg `-0.0388` n `86`; fx avg `0.0067` n `6`; index avg `-0.03` n `23`; metal avg `-0.0464` n `20`; unknown avg `0.2489` n `756`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0651` n `228`; crypto_major avg `-0.1521` n `8`; equity avg `-0.8598` n `86`; fx avg `0.0087` n `6`; index avg `-0.1192` n `23`; metal avg `-0.2551` n `20`; unknown avg `-0.0516` n `756`
- 24h: commodity avg `-0.3777` n `12`; crypto_alt avg `-2.9165` n `228`; crypto_major avg `-3.7941` n `8`; equity avg `-3.4029` n `86`; fx avg `-0.1891` n `6`; index avg `-0.9505` n `23`; metal avg `-1.1974` n `20`; unknown avg `0.1181` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
