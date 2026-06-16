# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T16:22:48.786165+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3681` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0118` n `228`; crypto_major avg `-0.2288` n `8`; equity avg `0.163` n `77`; fx avg `-0.0023` n `6`; index avg `0.0493` n `23`; metal avg `0.1043` n `18`; unknown avg `-0.0119` n `687`
- 1h: commodity avg `-0.3651` n `12`; crypto_alt avg `0.4442` n `228`; crypto_major avg `0.0761` n `8`; equity avg `0.2449` n `77`; fx avg `0.0302` n `6`; index avg `0.0945` n `23`; metal avg `0.3671` n `18`; unknown avg `0.0302` n `687`
- 4h: commodity avg `-0.1189` n `12`; crypto_alt avg `-1.6287` n `228`; crypto_major avg `-1.9032` n `8`; equity avg `-0.8795` n `77`; fx avg `0.0723` n `6`; index avg `-0.5351` n `23`; metal avg `0.1117` n `18`; unknown avg `1.2891` n `687`
- 24h: commodity avg `-0.683` n `12`; crypto_alt avg `-2.4435` n `228`; crypto_major avg `-1.3207` n `8`; equity avg `-0.7776` n `77`; fx avg `-0.0104` n `6`; index avg `-0.663` n `23`; metal avg `0.0985` n `18`; unknown avg `0.3147` n `623`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
