# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T00:52:25.088603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `0.052` n `230`; crypto_major avg `0.0372` n `8`; equity avg `-0.1317` n `98`; fx avg `0.0138` n `6`; index avg `-0.0425` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0171` n `771`
- 1h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.2639` n `230`; crypto_major avg `0.3701` n `8`; equity avg `0.0436` n `98`; fx avg `-0.0053` n `6`; index avg `0.0024` n `25`; metal avg `0.079` n `20`; unknown avg `0.2097` n `771`
- 4h: commodity avg `0.0117` n `12`; crypto_alt avg `0.2358` n `230`; crypto_major avg `0.4085` n `8`; equity avg `0.3029` n `98`; fx avg `-0.0185` n `6`; index avg `0.0372` n `25`; metal avg `0.1075` n `20`; unknown avg `-0.0418` n `771`
- 24h: commodity avg `0.4432` n `12`; crypto_alt avg `0.7434` n `230`; crypto_major avg `0.7191` n `8`; equity avg `4.1717` n `98`; fx avg `0.0282` n `6`; index avg `0.6078` n `25`; metal avg `0.7181` n `20`; unknown avg `0.3608` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0947`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.056`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.05`, n `666`, weak_sample_signal
