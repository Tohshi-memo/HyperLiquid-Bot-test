# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T16:52:27.658098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5999` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2011` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0415` n `12`; crypto_alt avg `0.1441` n `233`; crypto_major avg `-0.0222` n `8`; equity avg `0.0906` n `134`; fx avg `0.0041` n `6`; index avg `0.0248` n `26`; metal avg `0.0672` n `20`; unknown avg `-0.3182` n `797`
- 1h: commodity avg `-0.1126` n `12`; crypto_alt avg `0.4911` n `233`; crypto_major avg `0.2135` n `8`; equity avg `0.0159` n `134`; fx avg `0.0022` n `6`; index avg `-0.0118` n `26`; metal avg `0.0399` n `20`; unknown avg `0.4726` n `789`
- 4h: commodity avg `-0.0659` n `12`; crypto_alt avg `-1.077` n `233`; crypto_major avg `-1.2199` n `8`; equity avg `0.1775` n `134`; fx avg `0.0342` n `6`; index avg `-0.0188` n `26`; metal avg `0.38` n `20`; unknown avg `8.5828` n `767`
- 24h: commodity avg `0.4128` n `12`; crypto_alt avg `-1.1725` n `233`; crypto_major avg `-0.499` n `8`; equity avg `-0.5311` n `134`; fx avg `-0.0833` n `6`; index avg `-0.1965` n `26`; metal avg `0.4008` n `20`; unknown avg `7.3467` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
