# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T19:22:26.373738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0099` n `230`; crypto_major avg `0.0171` n `8`; equity avg `0.0153` n `96`; fx avg `0.0013` n `6`; index avg `0.0035` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0678` n `770`
- 1h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.0374` n `230`; crypto_major avg `0.0987` n `8`; equity avg `0.0009` n `96`; fx avg `-0.0066` n `6`; index avg `-0.0056` n `25`; metal avg `0.0143` n `20`; unknown avg `-0.1323` n `770`
- 4h: commodity avg `0.252` n `12`; crypto_alt avg `0.1006` n `230`; crypto_major avg `0.4872` n `8`; equity avg `-0.0261` n `96`; fx avg `-0.073` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0391` n `20`; unknown avg `-0.0141` n `770`
- 24h: commodity avg `0.527` n `12`; crypto_alt avg `-0.4478` n `230`; crypto_major avg `0.5256` n `8`; equity avg `-0.3372` n `96`; fx avg `-0.1467` n `6`; index avg `0.0118` n `25`; metal avg `0.0494` n `20`; unknown avg `-0.0824` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
