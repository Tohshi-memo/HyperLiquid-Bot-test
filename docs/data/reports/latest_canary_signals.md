# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T18:39:30.167922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.8464` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6916` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6736` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.2245` n `233`; crypto_major avg `-0.0472` n `8`; equity avg `-0.0219` n `136`; fx avg `0.0062` n `6`; index avg `0.0042` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.3006` n `806`
- 1h: commodity avg `0.1251` n `12`; crypto_alt avg `-0.8962` n `233`; crypto_major avg `-0.7523` n `8`; equity avg `-0.2462` n `136`; fx avg `0.0036` n `6`; index avg `-0.0305` n `26`; metal avg `-0.1012` n `20`; unknown avg `0.0655` n `804`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `-1.5995` n `233`; crypto_major avg `-1.8083` n `8`; equity avg `-0.1167` n `136`; fx avg `-0.0039` n `6`; index avg `0.0381` n `26`; metal avg `-0.1347` n `20`; unknown avg `2.9258` n `752`
- 24h: commodity avg `-0.4532` n `12`; crypto_alt avg `0.3603` n `233`; crypto_major avg `1.2357` n `8`; equity avg `0.5615` n `136`; fx avg `-0.1432` n `6`; index avg `0.3406` n `26`; metal avg `0.2045` n `20`; unknown avg `1.7811` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
