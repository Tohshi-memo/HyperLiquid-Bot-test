# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T05:52:24.277966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.001` n `230`; crypto_major avg `0.0055` n `8`; equity avg `-0.0839` n `94`; fx avg `0.0128` n `6`; index avg `-0.018` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.2191` n `768`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `0.1152` n `230`; crypto_major avg `0.4479` n `8`; equity avg `0.0392` n `94`; fx avg `0.0058` n `6`; index avg `-0.0015` n `25`; metal avg `-0.042` n `20`; unknown avg `0.1719` n `768`
- 4h: commodity avg `-0.1401` n `12`; crypto_alt avg `-0.0376` n `230`; crypto_major avg `0.2485` n `8`; equity avg `0.0122` n `94`; fx avg `-0.0439` n `6`; index avg `-0.0075` n `25`; metal avg `0.0161` n `20`; unknown avg `-0.6123` n `768`
- 24h: commodity avg `-0.0756` n `12`; crypto_alt avg `0.3189` n `230`; crypto_major avg `0.4042` n `8`; equity avg `-2.2678` n `93`; fx avg `0.1447` n `6`; index avg `-0.4691` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.2114` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
