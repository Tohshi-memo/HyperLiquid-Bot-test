# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T11:07:37.398487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.2018` n `228`; crypto_major avg `-0.2087` n `8`; equity avg `0.0757` n `77`; fx avg `0.0068` n `6`; index avg `0.0351` n `23`; metal avg `-0.0786` n `18`; unknown avg `0.0649` n `687`
- 1h: commodity avg `-0.0501` n `12`; crypto_alt avg `0.1093` n `228`; crypto_major avg `0.2671` n `8`; equity avg `0.1552` n `77`; fx avg `0.0246` n `6`; index avg `0.0203` n `23`; metal avg `-0.0218` n `18`; unknown avg `0.1771` n `687`
- 4h: commodity avg `-0.6612` n `12`; crypto_alt avg `0.7293` n `228`; crypto_major avg `0.8243` n `8`; equity avg `0.516` n `77`; fx avg `0.0817` n `6`; index avg `0.1683` n `23`; metal avg `0.6815` n `18`; unknown avg `0.2725` n `687`
- 24h: commodity avg `0.1302` n `12`; crypto_alt avg `0.564` n `228`; crypto_major avg `2.4203` n `8`; equity avg `1.873` n `76`; fx avg `-0.0513` n `6`; index avg `0.5083` n `23`; metal avg `0.0767` n `18`; unknown avg `0.3769` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
