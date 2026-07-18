# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T11:22:32.309827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0212` n `230`; crypto_major avg `0.0057` n `8`; equity avg `-0.0042` n `96`; fx avg `0.0` n `6`; index avg `0.0156` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0048` n `770`
- 1h: commodity avg `0.0307` n `12`; crypto_alt avg `0.0314` n `230`; crypto_major avg `0.0765` n `8`; equity avg `-0.0047` n `96`; fx avg `-0.0112` n `6`; index avg `0.0083` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0254` n `769`
- 4h: commodity avg `0.1552` n `12`; crypto_alt avg `-0.1234` n `230`; crypto_major avg `-0.012` n `8`; equity avg `-0.1112` n `96`; fx avg `-0.0088` n `6`; index avg `0.0684` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.1161` n `769`
- 24h: commodity avg `0.6958` n `12`; crypto_alt avg `-0.4814` n `230`; crypto_major avg `0.2403` n `8`; equity avg `0.6348` n `96`; fx avg `0.0213` n `6`; index avg `0.1818` n `25`; metal avg `0.2806` n `20`; unknown avg `0.0905` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
