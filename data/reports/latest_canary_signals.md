# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T04:07:29.888547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0436` n `230`; crypto_major avg `0.015` n `8`; equity avg `0.0216` n `94`; fx avg `-0.0024` n `6`; index avg `0.0244` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.3442` n `768`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.2101` n `230`; crypto_major avg `-0.2296` n `8`; equity avg `-0.0919` n `94`; fx avg `-0.0074` n `6`; index avg `-0.0069` n `25`; metal avg `0.0442` n `20`; unknown avg `-0.2515` n `768`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `-0.0779` n `230`; crypto_major avg `-0.3702` n `8`; equity avg `0.0301` n `20`; fx avg `0.0` n `1`; index avg `0.0074` n `19`; metal avg `-0.0372` n `14`; unknown avg `-0.6358` n `764`
- 24h: commodity avg `-0.0983` n `12`; crypto_alt avg `0.0706` n `230`; crypto_major avg `-0.0166` n `8`; equity avg `-2.4314` n `93`; fx avg `0.1104` n `6`; index avg `-0.4525` n `25`; metal avg `0.0701` n `20`; unknown avg `-0.1645` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
