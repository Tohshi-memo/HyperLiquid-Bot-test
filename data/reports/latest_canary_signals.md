# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T14:22:40.501176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `0.277` n `231`; crypto_major avg `0.5192` n `8`; equity avg `0.3736` n `127`; fx avg `-0.0146` n `6`; index avg `0.0685` n `26`; metal avg `0.0626` n `20`; unknown avg `0.0602` n `792`
- 1h: commodity avg `0.2232` n `12`; crypto_alt avg `0.5005` n `231`; crypto_major avg `0.8436` n `8`; equity avg `-0.0073` n `127`; fx avg `-0.0211` n `6`; index avg `-0.0226` n `26`; metal avg `0.0444` n `20`; unknown avg `0.0735` n `792`
- 4h: commodity avg `0.3517` n `12`; crypto_alt avg `0.442` n `231`; crypto_major avg `0.3436` n `8`; equity avg `-0.3214` n `127`; fx avg `0.0285` n `6`; index avg `-0.0304` n `26`; metal avg `0.0501` n `20`; unknown avg `-0.0675` n `792`
- 24h: commodity avg `0.4937` n `12`; crypto_alt avg `2.3874` n `231`; crypto_major avg `3.1231` n `8`; equity avg `2.0026` n `127`; fx avg `-0.0435` n `6`; index avg `0.1958` n `26`; metal avg `-0.2987` n `20`; unknown avg `0.5864` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
