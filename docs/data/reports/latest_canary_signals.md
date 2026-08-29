# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T12:52:25.774714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.0569` n `231`; crypto_major avg `0.026` n `8`; equity avg `0.002` n `127`; fx avg `0.0002` n `6`; index avg `-0.0027` n `26`; metal avg `0.0072` n `20`; unknown avg `0.1663` n `793`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.18` n `231`; crypto_major avg `-0.0111` n `8`; equity avg `-0.0492` n `127`; fx avg `-0.0047` n `6`; index avg `-0.0044` n `26`; metal avg `0.0013` n `20`; unknown avg `1.7013` n `785`
- 4h: commodity avg `0.0389` n `12`; crypto_alt avg `0.2346` n `231`; crypto_major avg `0.1166` n `8`; equity avg `0.0013` n `127`; fx avg `-0.0202` n `6`; index avg `-0.003` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.1335` n `759`
- 24h: commodity avg `0.2548` n `12`; crypto_alt avg `-1.9543` n `231`; crypto_major avg `-1.9082` n `8`; equity avg `-1.4405` n `127`; fx avg `-0.0606` n `6`; index avg `-0.1623` n `26`; metal avg `-0.7521` n `20`; unknown avg `-0.4508` n `742`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
