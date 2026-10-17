# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T16:52:31.566490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.0581` n `236`; crypto_major avg `-0.0098` n `8`; equity avg `-0.0158` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0094` n `26`; metal avg `0.0023` n `20`; unknown avg `1.5599` n `1193`
- 1h: commodity avg `-0.0129` n `13`; crypto_alt avg `-0.0857` n `236`; crypto_major avg `-0.036` n `8`; equity avg `-0.0036` n `151`; fx avg `-0.0066` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0196` n `20`; unknown avg `0.6994` n `1177`
- 4h: commodity avg `0.0857` n `13`; crypto_alt avg `-0.819` n `236`; crypto_major avg `-0.4337` n `8`; equity avg `-0.2143` n `151`; fx avg `-0.0281` n `6`; index avg `-0.0508` n `26`; metal avg `-0.0401` n `20`; unknown avg `2.2482` n `1159`
- 24h: commodity avg `0.0893` n `13`; crypto_alt avg `-2.0363` n `236`; crypto_major avg `-0.6724` n `8`; equity avg `-1.2822` n `151`; fx avg `-0.0103` n `6`; index avg `-0.2355` n `26`; metal avg `-0.0439` n `20`; unknown avg `4.4775` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1714`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1464`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
