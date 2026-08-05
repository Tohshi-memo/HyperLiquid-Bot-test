# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T15:07:36.829235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.1227` n `230`; crypto_major avg `0.1842` n `8`; equity avg `0.2458` n `108`; fx avg `-0.0349` n `6`; index avg `0.0218` n `25`; metal avg `0.0682` n `20`; unknown avg `-0.0537` n `782`
- 1h: commodity avg `0.0563` n `12`; crypto_alt avg `-0.0195` n `230`; crypto_major avg `0.0907` n `8`; equity avg `-0.7202` n `108`; fx avg `-0.0169` n `6`; index avg `-0.1065` n `25`; metal avg `0.0379` n `20`; unknown avg `-0.0568` n `782`
- 4h: commodity avg `-0.3558` n `12`; crypto_alt avg `0.0265` n `230`; crypto_major avg `0.3613` n `8`; equity avg `-0.0865` n `108`; fx avg `-0.0386` n `6`; index avg `0.0261` n `25`; metal avg `0.2632` n `20`; unknown avg `-0.0257` n `782`
- 24h: commodity avg `-0.3574` n `12`; crypto_alt avg `0.8078` n `230`; crypto_major avg `0.5441` n `8`; equity avg `0.6382` n `108`; fx avg `0.0071` n `6`; index avg `0.2591` n `25`; metal avg `0.7514` n `20`; unknown avg `0.6939` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
