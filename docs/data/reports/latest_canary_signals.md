# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T14:07:28.255178+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `0.6559` n `230`; crypto_major avg `0.6611` n `8`; equity avg `1.262` n `96`; fx avg `0.0056` n `6`; index avg `0.1807` n `25`; metal avg `0.1095` n `20`; unknown avg `0.1389` n `769`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `1.0787` n `230`; crypto_major avg `0.9526` n `8`; equity avg `1.2904` n `96`; fx avg `0.0048` n `6`; index avg `0.164` n `25`; metal avg `0.2218` n `20`; unknown avg `0.3761` n `769`
- 4h: commodity avg `0.3326` n `12`; crypto_alt avg `-0.0871` n `230`; crypto_major avg `-0.0904` n `8`; equity avg `0.5451` n `96`; fx avg `0.0055` n `6`; index avg `0.0816` n `25`; metal avg `-0.0305` n `20`; unknown avg `0.2905` n `769`
- 24h: commodity avg `0.2346` n `12`; crypto_alt avg `-1.8475` n `230`; crypto_major avg `-2.8347` n `8`; equity avg `-3.266` n `94`; fx avg `-0.0573` n `6`; index avg `-0.5255` n `25`; metal avg `-0.3986` n `20`; unknown avg `-0.3053` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
