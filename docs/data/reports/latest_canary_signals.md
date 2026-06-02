# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T01:22:22.903958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0246` n `228`; crypto_major avg `-0.093` n `8`; equity avg `0.1203` n `69`; fx avg `0.0188` n `6`; index avg `0.0264` n `23`; metal avg `0.2705` n `18`; unknown avg `0.6748` n `422`
- 1h: commodity avg `-0.0644` n `12`; crypto_alt avg `-0.1597` n `228`; crypto_major avg `-0.2277` n `8`; equity avg `0.0396` n `69`; fx avg `-0.0074` n `6`; index avg `-0.1359` n `23`; metal avg `0.2731` n `18`; unknown avg `-0.5411` n `422`
- 4h: commodity avg `-0.2776` n `12`; crypto_alt avg `0.0438` n `228`; crypto_major avg `0.2101` n `8`; equity avg `-0.7104` n `69`; fx avg `-0.0067` n `6`; index avg `-0.4582` n `23`; metal avg `0.4512` n `18`; unknown avg `0.7853` n `422`
- 24h: commodity avg `-0.4378` n `12`; crypto_alt avg `-0.6383` n `228`; crypto_major avg `-1.3496` n `8`; equity avg `-0.7559` n `69`; fx avg `-0.0059` n `6`; index avg `-0.4236` n `23`; metal avg `0.0351` n `18`; unknown avg `2.3243` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
