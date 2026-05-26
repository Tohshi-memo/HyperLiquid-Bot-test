# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T23:52:17.822065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0499` n `12`; crypto_alt avg `-0.1556` n `228`; crypto_major avg `-0.1067` n `8`; equity avg `0.1113` n `67`; fx avg `0.0145` n `6`; index avg `0.0935` n `23`; metal avg `0.144` n `18`; unknown avg `-0.0056` n `418`
- 1h: commodity avg `-0.1107` n `12`; crypto_alt avg `0.0867` n `228`; crypto_major avg `0.1099` n `8`; equity avg `0.116` n `67`; fx avg `0.0005` n `6`; index avg `0.1703` n `23`; metal avg `0.2964` n `18`; unknown avg `-0.1799` n `418`
- 4h: commodity avg `-0.1104` n `12`; crypto_alt avg `-0.2996` n `228`; crypto_major avg `-0.4872` n `8`; equity avg `0.2173` n `67`; fx avg `0.0229` n `6`; index avg `0.0767` n `23`; metal avg `0.3823` n `18`; unknown avg `-0.5676` n `418`
- 24h: commodity avg `0.564` n `12`; crypto_alt avg `-1.5485` n `228`; crypto_major avg `-1.4878` n `8`; equity avg `0.043` n `67`; fx avg `-0.098` n `6`; index avg `0.7923` n `23`; metal avg `-0.2577` n `18`; unknown avg `0.1519` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
