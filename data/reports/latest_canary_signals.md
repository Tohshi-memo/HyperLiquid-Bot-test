# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T17:37:28.303576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8771` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.014` n `230`; crypto_major avg `-0.0004` n `8`; equity avg `0.0091` n `96`; fx avg `0.0064` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0055` n `769`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `0.2723` n `230`; crypto_major avg `0.4168` n `8`; equity avg `0.716` n `96`; fx avg `0.004` n `6`; index avg `0.0858` n `25`; metal avg `0.02` n `20`; unknown avg `0.518` n `769`
- 4h: commodity avg `0.2271` n `12`; crypto_alt avg `1.7427` n `230`; crypto_major avg `1.8551` n `8`; equity avg `3.7322` n `96`; fx avg `0.0809` n `6`; index avg `0.4923` n `25`; metal avg `0.4065` n `20`; unknown avg `1.1018` n `769`
- 24h: commodity avg `0.8025` n `12`; crypto_alt avg `-1.0335` n `230`; crypto_major avg `-1.2302` n `8`; equity avg `-0.4005` n `94`; fx avg `0.1` n `6`; index avg `-0.1721` n `25`; metal avg `-0.051` n `20`; unknown avg `-0.0579` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
