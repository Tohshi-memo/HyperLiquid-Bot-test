# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T19:22:32.558860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0694` n `12`; crypto_alt avg `-0.2143` n `228`; crypto_major avg `-0.2421` n `8`; equity avg `-0.1805` n `86`; fx avg `0.0041` n `6`; index avg `-0.032` n `23`; metal avg `0.032` n `20`; unknown avg `-0.1461` n `765`
- 1h: commodity avg `0.0632` n `12`; crypto_alt avg `-0.7796` n `228`; crypto_major avg `-0.7019` n `8`; equity avg `-0.4935` n `86`; fx avg `0.0047` n `6`; index avg `-0.0865` n `23`; metal avg `-0.0462` n `20`; unknown avg `-0.1812` n `765`
- 4h: commodity avg `0.1409` n `12`; crypto_alt avg `-0.2004` n `228`; crypto_major avg `0.4591` n `8`; equity avg `-0.2333` n `86`; fx avg `0.0384` n `6`; index avg `-0.0011` n `23`; metal avg `-0.0884` n `20`; unknown avg `-0.0397` n `765`
- 24h: commodity avg `0.5487` n `12`; crypto_alt avg `-0.0618` n `228`; crypto_major avg `0.0112` n `8`; equity avg `0.2988` n `86`; fx avg `0.0836` n `6`; index avg `0.4852` n `23`; metal avg `0.8402` n `20`; unknown avg `0.4731` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
