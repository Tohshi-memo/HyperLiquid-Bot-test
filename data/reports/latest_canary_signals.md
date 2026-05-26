# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T14:37:23.039721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.161` n `12`; crypto_alt avg `-0.1853` n `228`; crypto_major avg `-0.3997` n `8`; equity avg `0.0519` n `67`; fx avg `-0.0207` n `6`; index avg `0.0132` n `23`; metal avg `0.1347` n `18`; unknown avg `0.2302` n `416`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `0.7224` n `228`; crypto_major avg `0.7246` n `8`; equity avg `0.4551` n `67`; fx avg `-0.0377` n `6`; index avg `0.2226` n `23`; metal avg `-0.1147` n `18`; unknown avg `0.8344` n `416`
- 4h: commodity avg `0.5878` n `12`; crypto_alt avg `0.3969` n `228`; crypto_major avg `0.5076` n `8`; equity avg `0.1913` n `67`; fx avg `-0.0284` n `6`; index avg `0.4365` n `23`; metal avg `0.0974` n `18`; unknown avg `-0.1836` n `415`
- 24h: commodity avg `0.6328` n `12`; crypto_alt avg `0.1806` n `228`; crypto_major avg `-0.2311` n `8`; equity avg `-0.1658` n `67`; fx avg `-0.1617` n `6`; index avg `0.5244` n `23`; metal avg `-0.8775` n `18`; unknown avg `-0.025` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
