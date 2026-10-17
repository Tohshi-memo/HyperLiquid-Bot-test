# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T21:07:31.579166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `13`; crypto_alt avg `0.0768` n `236`; crypto_major avg `0.0312` n `8`; equity avg `-0.0217` n `151`; fx avg `-0.0031` n `6`; index avg `0.0029` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.5416` n `1185`
- 1h: commodity avg `-0.0685` n `13`; crypto_alt avg `0.0459` n `236`; crypto_major avg `0.1117` n `8`; equity avg `-0.0641` n `151`; fx avg `0.0027` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.6374` n `1185`
- 4h: commodity avg `-0.0011` n `13`; crypto_alt avg `1.4496` n `236`; crypto_major avg `0.9524` n `8`; equity avg `0.1429` n `151`; fx avg `-0.0146` n `6`; index avg `0.0219` n `26`; metal avg `0.0178` n `20`; unknown avg `1.0552` n `1131`
- 24h: commodity avg `-0.0417` n `13`; crypto_alt avg `-0.8172` n `236`; crypto_major avg `-0.0837` n `8`; equity avg `-0.2697` n `151`; fx avg `-0.0363` n `6`; index avg `-0.0369` n `26`; metal avg `-0.0366` n `20`; unknown avg `5.4047` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
