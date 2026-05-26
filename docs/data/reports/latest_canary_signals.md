# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T13:37:24.260715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `-0.1031` n `228`; crypto_major avg `0.0283` n `8`; equity avg `-0.2602` n `67`; fx avg `-0.0064` n `6`; index avg `0.2085` n `23`; metal avg `0.0405` n `18`; unknown avg `-0.143` n `418`
- 1h: commodity avg `0.5661` n `12`; crypto_alt avg `-0.3208` n `228`; crypto_major avg `-0.2182` n `8`; equity avg `-0.2786` n `67`; fx avg `0.0094` n `6`; index avg `0.2118` n `23`; metal avg `0.2133` n `18`; unknown avg `-0.4843` n `417`
- 4h: commodity avg `-0.045` n `12`; crypto_alt avg `0.9108` n `228`; crypto_major avg `1.1124` n `8`; equity avg `0.031` n `67`; fx avg `-0.0387` n `6`; index avg `0.4048` n `23`; metal avg `0.4822` n `18`; unknown avg `0.4228` n `417`
- 24h: commodity avg `0.3796` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `-0.5629` n `8`; equity avg `-0.5316` n `67`; fx avg `-0.1336` n `6`; index avg `0.3011` n `23`; metal avg `-0.3263` n `18`; unknown avg `-0.1777` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
