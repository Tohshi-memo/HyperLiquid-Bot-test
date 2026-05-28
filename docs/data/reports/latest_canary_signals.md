# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T00:52:16.736796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5801` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3439` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `0.0281` n `228`; crypto_major avg `-0.0805` n `8`; equity avg `0.1886` n `67`; fx avg `-0.0271` n `6`; index avg `0.1067` n `23`; metal avg `0.0658` n `18`; unknown avg `0.0593` n `419`
- 1h: commodity avg `0.0735` n `12`; crypto_alt avg `-0.0019` n `228`; crypto_major avg `0.0868` n `8`; equity avg `0.1161` n `67`; fx avg `0.0075` n `6`; index avg `0.0493` n `23`; metal avg `0.2443` n `18`; unknown avg `0.0611` n `419`
- 4h: commodity avg `0.4002` n `12`; crypto_alt avg `-1.9338` n `228`; crypto_major avg `-1.5242` n `8`; equity avg `-0.4452` n `67`; fx avg `-0.0117` n `6`; index avg `-0.1803` n `23`; metal avg `0.0559` n `18`; unknown avg `0.709` n `419`
- 24h: commodity avg `-0.7731` n `12`; crypto_alt avg `-2.5878` n `228`; crypto_major avg `-1.8581` n `8`; equity avg `-0.659` n `67`; fx avg `-0.0923` n `6`; index avg `-0.7669` n `23`; metal avg `-1.5528` n `18`; unknown avg `-1.0066` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
