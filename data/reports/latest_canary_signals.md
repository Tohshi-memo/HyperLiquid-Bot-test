# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T00:07:28.230217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.1154` n `230`; crypto_major avg `-0.0388` n `8`; equity avg `0.0027` n `94`; fx avg `0.0224` n `6`; index avg `-0.043` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.1286` n `768`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `-0.3675` n `230`; crypto_major avg `-0.2806` n `8`; equity avg `-0.2937` n `94`; fx avg `0.0306` n `6`; index avg `-0.0659` n `25`; metal avg `0.013` n `20`; unknown avg `-0.2409` n `768`
- 4h: commodity avg `0.1319` n `12`; crypto_alt avg `-0.9431` n `230`; crypto_major avg `-0.8762` n `8`; equity avg `-0.7586` n `94`; fx avg `0.0298` n `6`; index avg `-0.0779` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.2784` n `768`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `-1.9757` n `230`; crypto_major avg `-2.8896` n `8`; equity avg `-0.3955` n `20`; fx avg `0.0` n `1`; index avg `-0.1558` n `19`; metal avg `-0.1156` n `14`; unknown avg `-0.7032` n `742`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
