# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T07:52:25.033356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `0.0464` n `233`; crypto_major avg `0.0223` n `8`; equity avg `0.0072` n `136`; fx avg `0.0016` n `6`; index avg `0.0003` n `26`; metal avg `0.0005` n `20`; unknown avg `0.4792` n `838`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `0.3586` n `233`; crypto_major avg `0.1474` n `8`; equity avg `0.0111` n `136`; fx avg `-0.0061` n `6`; index avg `0.0026` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.5762` n `836`
- 4h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.5687` n `233`; crypto_major avg `0.1782` n `8`; equity avg `-0.0567` n `136`; fx avg `-0.0054` n `6`; index avg `0.0074` n `26`; metal avg `0.0122` n `20`; unknown avg `0.6546` n `800`
- 24h: commodity avg `-0.4071` n `12`; crypto_alt avg `1.5829` n `233`; crypto_major avg `1.0375` n `8`; equity avg `0.2892` n `136`; fx avg `-0.1349` n `6`; index avg `0.185` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.8813` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
