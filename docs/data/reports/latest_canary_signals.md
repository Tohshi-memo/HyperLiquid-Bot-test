# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T13:52:32.191412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0925` n `12`; crypto_alt avg `0.5613` n `230`; crypto_major avg `0.5886` n `8`; equity avg `0.7478` n `96`; fx avg `-0.0076` n `6`; index avg `0.0901` n `25`; metal avg `0.1318` n `20`; unknown avg `0.1236` n `769`
- 1h: commodity avg `0.2694` n `12`; crypto_alt avg `-0.3154` n `230`; crypto_major avg `-0.2933` n `8`; equity avg `-0.1588` n `96`; fx avg `0.0076` n `6`; index avg `-0.066` n `25`; metal avg `0.1057` n `20`; unknown avg `0.1894` n `769`
- 4h: commodity avg `0.3811` n `12`; crypto_alt avg `-0.6377` n `230`; crypto_major avg `-0.6749` n `8`; equity avg `-0.4367` n `96`; fx avg `-0.0192` n `6`; index avg `-0.0672` n `25`; metal avg `-0.1473` n `20`; unknown avg `0.2774` n `769`
- 24h: commodity avg `0.2079` n `12`; crypto_alt avg `-2.3747` n `230`; crypto_major avg `-3.303` n `8`; equity avg `-4.0389` n `94`; fx avg `-0.0579` n `6`; index avg `-0.6154` n `25`; metal avg `-0.5185` n `20`; unknown avg `-0.3541` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
