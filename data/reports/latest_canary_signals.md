# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T05:39:21.772394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.7323` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.0549` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2521` n `12`; crypto_alt avg `0.2084` n `228`; crypto_major avg `0.164` n `8`; equity avg `0.1946` n `74`; fx avg `-0.0058` n `6`; index avg `0.0695` n `23`; metal avg `0.106` n `18`; unknown avg `0.541` n `425`
- 1h: commodity avg `0.0855` n `12`; crypto_alt avg `1.9078` n `228`; crypto_major avg `1.8136` n `8`; equity avg `0.471` n `74`; fx avg `-0.0136` n `6`; index avg `0.0657` n `23`; metal avg `0.0813` n `18`; unknown avg `22.9602` n `425`
- 4h: commodity avg `-0.1286` n `12`; crypto_alt avg `-2.98` n `228`; crypto_major avg `-1.7432` n `8`; equity avg `-1.0964` n `74`; fx avg `-0.0122` n `6`; index avg `-0.6883` n `23`; metal avg `-0.5726` n `18`; unknown avg `-0.2514` n `425`
- 24h: commodity avg `-1.3642` n `12`; crypto_alt avg `-7.2186` n `228`; crypto_major avg `-5.2281` n `8`; equity avg `-7.0381` n `74`; fx avg `-0.1787` n `6`; index avg `-4.3318` n `23`; metal avg `-4.2397` n `18`; unknown avg `-0.9003` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
