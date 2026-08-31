# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T00:37:25.881408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0223` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8857` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `0.2604` n `231`; crypto_major avg `0.1207` n `8`; equity avg `0.1548` n `128`; fx avg `0.0167` n `6`; index avg `0.0496` n `26`; metal avg `0.0718` n `20`; unknown avg `0.2131` n `793`
- 1h: commodity avg `-0.1855` n `12`; crypto_alt avg `0.7226` n `231`; crypto_major avg `0.5489` n `8`; equity avg `0.0439` n `128`; fx avg `0.022` n `6`; index avg `-0.0203` n `26`; metal avg `0.0864` n `20`; unknown avg `0.741` n `791`
- 4h: commodity avg `-0.4028` n `12`; crypto_alt avg `-1.9924` n `231`; crypto_major avg `-2.0972` n `8`; equity avg `-0.8526` n `128`; fx avg `0.0372` n `6`; index avg `-0.2115` n `26`; metal avg `-0.0749` n `20`; unknown avg `7.2677` n `789`
- 24h: commodity avg `0.0779` n `12`; crypto_alt avg `-0.7191` n `231`; crypto_major avg `-1.6898` n `8`; equity avg `-0.8138` n `128`; fx avg `0.0482` n `6`; index avg `-0.2132` n `26`; metal avg `-0.0174` n `20`; unknown avg `-0.3819` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
