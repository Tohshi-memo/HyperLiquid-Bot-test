# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T04:22:32.289462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2599` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `0.0775` n `230`; crypto_major avg `0.0747` n `8`; equity avg `0.0139` n `102`; fx avg `-0.0134` n `6`; index avg `-0.0017` n `25`; metal avg `0.0426` n `20`; unknown avg `-0.0993` n `782`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0086` n `230`; crypto_major avg `0.0975` n `8`; equity avg `0.0737` n `102`; fx avg `-0.0482` n `6`; index avg `0.0519` n `25`; metal avg `0.061` n `20`; unknown avg `-0.0919` n `782`
- 4h: commodity avg `-1.0297` n `12`; crypto_alt avg `0.8601` n `230`; crypto_major avg `1.2302` n `8`; equity avg `0.736` n `102`; fx avg `-0.0432` n `6`; index avg `0.2205` n `25`; metal avg `0.211` n `20`; unknown avg `2.7079` n `782`
- 24h: commodity avg `-1.1381` n `12`; crypto_alt avg `-0.0071` n `230`; crypto_major avg `0.3469` n `8`; equity avg `0.8464` n `102`; fx avg `-0.0923` n `6`; index avg `0.2153` n `25`; metal avg `0.274` n `20`; unknown avg `-0.0019` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
