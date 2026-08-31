# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T17:52:23.334927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6081` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.3383` n `232`; crypto_major avg `0.3187` n `8`; equity avg `0.0904` n `129`; fx avg `0.0067` n `6`; index avg `0.0392` n `26`; metal avg `0.0423` n `20`; unknown avg `1.5609` n `793`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `0.4295` n `232`; crypto_major avg `0.42` n `8`; equity avg `0.0004` n `129`; fx avg `0.0037` n `6`; index avg `0.0085` n `26`; metal avg `0.005` n `20`; unknown avg `0.9498` n `791`
- 4h: commodity avg `-0.0311` n `12`; crypto_alt avg `1.292` n `232`; crypto_major avg `1.6378` n `8`; equity avg `0.1781` n `129`; fx avg `0.0034` n `6`; index avg `-0.0421` n `26`; metal avg `0.0297` n `20`; unknown avg `1.2801` n `789`
- 24h: commodity avg `0.5482` n `12`; crypto_alt avg `-0.8861` n `231`; crypto_major avg `-1.0381` n `8`; equity avg `-0.4431` n `129`; fx avg `-0.1032` n `6`; index avg `-0.2288` n `26`; metal avg `-0.5347` n `20`; unknown avg `1.3218` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
