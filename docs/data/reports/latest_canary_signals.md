# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T21:07:27.009678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.004` n `228`; crypto_major avg `-0.0045` n `8`; equity avg `-0.0178` n `88`; fx avg `0.0043` n `6`; index avg `0.0085` n `23`; metal avg `-0.0086` n `20`; unknown avg `-0.6374` n `764`
- 1h: commodity avg `-0.2899` n `12`; crypto_alt avg `0.1958` n `228`; crypto_major avg `0.1342` n `8`; equity avg `0.1453` n `88`; fx avg `-0.0384` n `6`; index avg `0.0749` n `23`; metal avg `0.0477` n `20`; unknown avg `-0.7457` n `764`
- 4h: commodity avg `-0.32` n `12`; crypto_alt avg `-0.587` n `228`; crypto_major avg `-0.5504` n `8`; equity avg `0.0676` n `88`; fx avg `-0.0346` n `6`; index avg `0.0606` n `23`; metal avg `0.0425` n `20`; unknown avg `0.8194` n `764`
- 24h: commodity avg `0.1357` n `12`; crypto_alt avg `-0.603` n `228`; crypto_major avg `-1.1122` n `8`; equity avg `0.2217` n `88`; fx avg `-0.0718` n `6`; index avg `0.0066` n `23`; metal avg `0.0191` n `20`; unknown avg `15.1078` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
