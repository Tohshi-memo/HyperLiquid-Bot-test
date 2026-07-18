# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T06:25:26.540674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `0.1237` n `230`; crypto_major avg `0.1147` n `8`; equity avg `-0.0232` n `96`; fx avg `-0.0016` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0232` n `20`; unknown avg `-0.1146` n `769`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `-0.0794` n `8`; equity avg `-0.0844` n `96`; fx avg `-0.0112` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.0149` n `737`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `-0.3444` n `230`; crypto_major avg `-0.2971` n `8`; equity avg `-0.1514` n `96`; fx avg `-0.0047` n `6`; index avg `0.0414` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.055` n `737`
- 24h: commodity avg `0.9192` n `12`; crypto_alt avg `-0.212` n `230`; crypto_major avg `0.5056` n `8`; equity avg `1.0204` n `96`; fx avg `0.0271` n `6`; index avg `0.1534` n `25`; metal avg `0.0982` n `20`; unknown avg `0.2855` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
