# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T08:22:26.350746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.0113` n `233`; crypto_major avg `0.0102` n `8`; equity avg `-0.0037` n `136`; fx avg `0.0051` n `6`; index avg `-0.0037` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.047` n `838`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.089` n `233`; crypto_major avg `0.0768` n `8`; equity avg `-0.0019` n `136`; fx avg `0.001` n `6`; index avg `-0.0062` n `26`; metal avg `0.0021` n `20`; unknown avg `0.7927` n `836`
- 4h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.6439` n `233`; crypto_major avg `0.2947` n `8`; equity avg `-0.0379` n `136`; fx avg `-0.0021` n `6`; index avg `-0.0007` n `26`; metal avg `0.0206` n `20`; unknown avg `-0.1295` n `800`
- 24h: commodity avg `-0.3593` n `12`; crypto_alt avg `1.5491` n `233`; crypto_major avg `1.055` n `8`; equity avg `0.2904` n `136`; fx avg `-0.1238` n `6`; index avg `0.1556` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.7955` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
