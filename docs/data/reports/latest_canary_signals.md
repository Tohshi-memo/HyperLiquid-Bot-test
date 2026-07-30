# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T13:52:27.596135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.8739` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.7806` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `0.5265` n `230`; crypto_major avg `0.47` n `8`; equity avg `1.3282` n `102`; fx avg `-0.0362` n `6`; index avg `0.1002` n `25`; metal avg `0.0865` n `20`; unknown avg `-0.0033` n `779`
- 1h: commodity avg `-0.0571` n `12`; crypto_alt avg `0.3964` n `230`; crypto_major avg `0.3066` n `8`; equity avg `2.0872` n `102`; fx avg `-0.2678` n `6`; index avg `0.1973` n `25`; metal avg `0.2268` n `20`; unknown avg `0.0341` n `779`
- 4h: commodity avg `-0.2336` n `12`; crypto_alt avg `0.4057` n `230`; crypto_major avg `0.4267` n `8`; equity avg `4.3006` n `102`; fx avg `-0.3221` n `6`; index avg `0.4997` n `25`; metal avg `0.262` n `20`; unknown avg `0.1265` n `779`
- 24h: commodity avg `-0.1725` n `12`; crypto_alt avg `0.5489` n `230`; crypto_major avg `0.6034` n `8`; equity avg `2.6311` n `102`; fx avg `-0.3331` n `6`; index avg `0.1954` n `25`; metal avg `0.7974` n `20`; unknown avg `-0.1941` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
