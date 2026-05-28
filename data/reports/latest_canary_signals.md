# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T21:07:25.907309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.128` n `12`; crypto_alt avg `-0.2105` n `228`; crypto_major avg `-0.2101` n `8`; equity avg `0.0019` n `69`; fx avg `0.0033` n `6`; index avg `0.0236` n `23`; metal avg `-0.0054` n `18`; unknown avg `-0.1085` n `417`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.6962` n `228`; crypto_major avg `0.4077` n `8`; equity avg `0.1804` n `69`; fx avg `0.0169` n `6`; index avg `-0.0608` n `23`; metal avg `0.0153` n `18`; unknown avg `0.2625` n `417`
- 4h: commodity avg `0.3009` n `12`; crypto_alt avg `0.705` n `228`; crypto_major avg `0.4943` n `8`; equity avg `0.5386` n `69`; fx avg `0.0104` n `6`; index avg `-0.2184` n `23`; metal avg `-0.1251` n `18`; unknown avg `0.4067` n `417`
- 24h: commodity avg `1.1225` n `12`; crypto_alt avg `-3.5398` n `228`; crypto_major avg `-1.2398` n `8`; equity avg `1.7237` n `69`; fx avg `-0.022` n `6`; index avg `0.6765` n `23`; metal avg `0.4896` n `18`; unknown avg `-0.6808` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
