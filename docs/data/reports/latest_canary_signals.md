# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T18:22:35.871512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `13`; crypto_alt avg `0.0171` n `239`; crypto_major avg `0.0051` n `8`; equity avg `0.0199` n `168`; fx avg `0.0018` n `6`; index avg `0.0038` n `27`; metal avg `-0.009` n `20`; unknown avg `-0.205` n `1243`
- 1h: commodity avg `0.0563` n `13`; crypto_alt avg `0.3832` n `239`; crypto_major avg `0.1916` n `8`; equity avg `-0.0206` n `168`; fx avg `0.0007` n `6`; index avg `0.0125` n `27`; metal avg `-0.0311` n `20`; unknown avg `-0.2219` n `1237`
- 4h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.0563` n `239`; crypto_major avg `-0.2729` n `8`; equity avg `-0.1077` n `168`; fx avg `-0.0298` n `6`; index avg `0.0061` n `27`; metal avg `-0.0542` n `20`; unknown avg `-0.4485` n `1217`
- 24h: commodity avg `0.0515` n `13`; crypto_alt avg `2.2874` n `239`; crypto_major avg `1.4499` n `8`; equity avg `2.3864` n `168`; fx avg `-0.0181` n `6`; index avg `0.1757` n `27`; metal avg `0.5349` n `20`; unknown avg `10.4575` n `1045`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
