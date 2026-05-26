# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T14:52:19.675930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1441` n `12`; crypto_alt avg `-0.2092` n `228`; crypto_major avg `-0.1638` n `8`; equity avg `0.0295` n `67`; fx avg `0.005` n `6`; index avg `-0.044` n `23`; metal avg `-0.1056` n `18`; unknown avg `1.3096` n `418`
- 1h: commodity avg `-0.2232` n `12`; crypto_alt avg `-0.0212` n `228`; crypto_major avg `-0.0301` n `8`; equity avg `0.3175` n `67`; fx avg `-0.0129` n `6`; index avg `0.0483` n `23`; metal avg `0.0541` n `18`; unknown avg `1.2857` n `416`
- 4h: commodity avg `0.7345` n `12`; crypto_alt avg `0.1864` n `228`; crypto_major avg `0.3437` n `8`; equity avg `0.2127` n `67`; fx avg `-0.0235` n `6`; index avg `0.3915` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.0019` n `415`
- 24h: commodity avg `0.9374` n `12`; crypto_alt avg `-0.0921` n `228`; crypto_major avg `-0.3302` n `8`; equity avg `-0.2014` n `67`; fx avg `-0.1658` n `6`; index avg `0.4883` n `23`; metal avg `-0.7247` n `18`; unknown avg `0.8368` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
