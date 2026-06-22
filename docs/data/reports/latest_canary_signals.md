# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T13:07:30.211589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0923` n `12`; crypto_alt avg `-0.1521` n `228`; crypto_major avg `-0.1561` n `8`; equity avg `0.0115` n `79`; fx avg `-0.0211` n `6`; index avg `0.0033` n `23`; metal avg `-0.0203` n `20`; unknown avg `-0.0143` n `722`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1385` n `228`; crypto_major avg `0.3131` n `8`; equity avg `0.1443` n `79`; fx avg `0.0047` n `6`; index avg `0.0213` n `23`; metal avg `-0.1318` n `20`; unknown avg `-0.02` n `722`
- 4h: commodity avg `-0.1423` n `12`; crypto_alt avg `1.0079` n `228`; crypto_major avg `0.9293` n `8`; equity avg `0.3351` n `79`; fx avg `0.0253` n `6`; index avg `0.1061` n `23`; metal avg `-0.1446` n `18`; unknown avg `0.7997` n `701`
- 24h: commodity avg `-0.3586` n `12`; crypto_alt avg `0.7591` n `228`; crypto_major avg `1.1837` n `8`; equity avg `0.2137` n `79`; fx avg `0.1192` n `6`; index avg `0.1566` n `23`; metal avg `0.393` n `18`; unknown avg `0.61` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
