# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T23:22:29.202386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.0142` n `228`; crypto_major avg `0.0566` n `8`; equity avg `-0.03` n `88`; fx avg `0.0009` n `6`; index avg `0.0189` n `23`; metal avg `-0.1285` n `20`; unknown avg `-0.1084` n `764`
- 1h: commodity avg `-0.0857` n `12`; crypto_alt avg `-0.1336` n `228`; crypto_major avg `-0.0002` n `8`; equity avg `-0.0329` n `88`; fx avg `0.0096` n `6`; index avg `-0.0047` n `23`; metal avg `-0.014` n `20`; unknown avg `0.1865` n `762`
- 4h: commodity avg `-0.4192` n `12`; crypto_alt avg `-0.6512` n `228`; crypto_major avg `-0.3676` n `8`; equity avg `0.2135` n `88`; fx avg `-0.0291` n `6`; index avg `0.1114` n `23`; metal avg `-0.1892` n `20`; unknown avg `0.807` n `762`
- 24h: commodity avg `-0.2246` n `12`; crypto_alt avg `-0.6328` n `228`; crypto_major avg `-0.9166` n `8`; equity avg `0.3291` n `88`; fx avg `-0.0973` n `6`; index avg `0.1211` n `23`; metal avg `-0.1753` n `20`; unknown avg `15.2774` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
