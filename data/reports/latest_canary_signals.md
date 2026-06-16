# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T14:52:38.551922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1585` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0661` n `12`; crypto_alt avg `0.2726` n `228`; crypto_major avg `0.1593` n `8`; equity avg `0.1578` n `77`; fx avg `0.0316` n `6`; index avg `-0.0106` n `23`; metal avg `0.028` n `18`; unknown avg `0.0649` n `687`
- 1h: commodity avg `-0.2985` n `12`; crypto_alt avg `-0.9841` n `228`; crypto_major avg `-0.8706` n `8`; equity avg `-1.2102` n `77`; fx avg `0.0275` n `6`; index avg `-0.5979` n `23`; metal avg `-0.4201` n `18`; unknown avg `0.0307` n `687`
- 4h: commodity avg `-0.1903` n `12`; crypto_alt avg `-1.906` n `228`; crypto_major avg `-1.6379` n `8`; equity avg `-1.2529` n `77`; fx avg `-0.0052` n `6`; index avg `-0.4794` n `23`; metal avg `-0.3436` n `18`; unknown avg `0.4101` n `687`
- 24h: commodity avg `-0.4782` n `12`; crypto_alt avg `-2.3054` n `228`; crypto_major avg `-0.5359` n `8`; equity avg `-0.067` n `77`; fx avg `-0.0464` n `6`; index avg `-0.1276` n `23`; metal avg `-0.4092` n `18`; unknown avg `-0.209` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
