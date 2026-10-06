# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T16:08:13.383719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0841` n `13`; crypto_alt avg `-0.2451` n `235`; crypto_major avg `-0.0808` n `8`; equity avg `-0.219` n `150`; fx avg `-0.0069` n `6`; index avg `-0.0316` n `26`; metal avg `0.0036` n `20`; unknown avg `0.4546` n `1068`
- 1h: commodity avg `0.2159` n `13`; crypto_alt avg `-0.4479` n `235`; crypto_major avg `-0.5597` n `8`; equity avg `-0.3602` n `150`; fx avg `0.008` n `6`; index avg `-0.0401` n `26`; metal avg `0.0937` n `20`; unknown avg `1.3284` n `1068`
- 4h: commodity avg `0.4254` n `13`; crypto_alt avg `-0.3067` n `235`; crypto_major avg `-0.3175` n `8`; equity avg `0.0251` n `150`; fx avg `-0.019` n `6`; index avg `-0.0523` n `26`; metal avg `-0.0517` n `20`; unknown avg `5.2651` n `1018`
- 24h: commodity avg `-0.2547` n `13`; crypto_alt avg `0.4161` n `235`; crypto_major avg `0.4195` n `8`; equity avg `0.7366` n `149`; fx avg `0.1176` n `6`; index avg `0.1303` n `26`; metal avg `0.0742` n `20`; unknown avg `381.3096` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
