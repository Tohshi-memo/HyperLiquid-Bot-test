# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T03:07:24.682629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6013` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5535` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0874` n `12`; crypto_alt avg `0.4244` n `228`; crypto_major avg `0.5123` n `8`; equity avg `0.1737` n `74`; fx avg `0.0051` n `6`; index avg `0.0779` n `23`; metal avg `-0.0278` n `18`; unknown avg `0.3761` n `517`
- 1h: commodity avg `-0.16` n `12`; crypto_alt avg `-0.56` n `228`; crypto_major avg `0.0742` n `8`; equity avg `0.0775` n `74`; fx avg `0.0265` n `6`; index avg `0.067` n `23`; metal avg `-0.0216` n `18`; unknown avg `-0.3052` n `517`
- 4h: commodity avg `-0.2685` n `12`; crypto_alt avg `-2.2396` n `228`; crypto_major avg `-1.5039` n `8`; equity avg `0.0974` n `74`; fx avg `-0.0636` n `6`; index avg `0.0496` n `23`; metal avg `-0.1068` n `18`; unknown avg `0.1579` n `517`
- 24h: commodity avg `-1.1489` n `12`; crypto_alt avg `-0.906` n `228`; crypto_major avg `-0.1464` n `8`; equity avg `1.1088` n `74`; fx avg `-0.3015` n `6`; index avg `0.4873` n `23`; metal avg `0.2482` n `18`; unknown avg `-3.1886` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
