# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T14:52:25.932770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0838` n `12`; crypto_alt avg `0.1207` n `230`; crypto_major avg `0.2661` n `8`; equity avg `0.2658` n `114`; fx avg `0.0037` n `6`; index avg `0.0347` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0092` n `792`
- 1h: commodity avg `-0.0979` n `12`; crypto_alt avg `0.0329` n `230`; crypto_major avg `0.1906` n `8`; equity avg `0.3573` n `114`; fx avg `-0.0001` n `6`; index avg `0.0461` n `25`; metal avg `0.0936` n `20`; unknown avg `-0.0199` n `792`
- 4h: commodity avg `-0.0049` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `0.0352` n `8`; equity avg `0.1535` n `114`; fx avg `0.0358` n `6`; index avg `0.0586` n `25`; metal avg `0.1124` n `20`; unknown avg `0.0808` n `792`
- 24h: commodity avg `-0.0818` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `0.935` n `8`; equity avg `1.5282` n `114`; fx avg `0.0072` n `6`; index avg `0.2169` n `25`; metal avg `0.3023` n `20`; unknown avg `0.0707` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
