# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T01:37:28.596668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.72` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6916` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0633` n `12`; crypto_alt avg `-0.0385` n `231`; crypto_major avg `0.0186` n `8`; equity avg `0.0881` n `128`; fx avg `-0.0227` n `6`; index avg `0.0286` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.1034` n `793`
- 1h: commodity avg `0.2721` n `12`; crypto_alt avg `-0.2621` n `231`; crypto_major avg `-0.4952` n `8`; equity avg `-0.413` n `128`; fx avg `-0.0755` n `6`; index avg `-0.0755` n `26`; metal avg `-0.2877` n `20`; unknown avg `-0.4947` n `791`
- 4h: commodity avg `-0.1829` n `12`; crypto_alt avg `-1.8917` n `231`; crypto_major avg `-2.0048` n `8`; equity avg `-1.1863` n `128`; fx avg `-0.0425` n `6`; index avg `-0.2848` n `26`; metal avg `-0.3132` n `20`; unknown avg `2.8576` n `791`
- 24h: commodity avg `0.3582` n `12`; crypto_alt avg `-0.5911` n `231`; crypto_major avg `-1.9336` n `8`; equity avg `-1.2191` n `128`; fx avg `-0.0276` n `6`; index avg `-0.2992` n `26`; metal avg `-0.3106` n `20`; unknown avg `-0.4698` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
