# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T13:22:22.038589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `-0.3969` n `228`; crypto_major avg `-0.2898` n `8`; equity avg `0.07` n `67`; fx avg `0.0066` n `6`; index avg `-0.0276` n `23`; metal avg `0.1863` n `18`; unknown avg `1.0443` n `418`
- 1h: commodity avg `0.5147` n `12`; crypto_alt avg `-0.278` n `228`; crypto_major avg `-0.2366` n `8`; equity avg `-0.0217` n `67`; fx avg `0.0161` n `6`; index avg `-0.0434` n `23`; metal avg `0.16` n `18`; unknown avg `-0.3525` n `417`
- 4h: commodity avg `-0.1173` n `12`; crypto_alt avg `0.8669` n `228`; crypto_major avg `0.9871` n `8`; equity avg `0.3229` n `67`; fx avg `-0.0239` n `6`; index avg `0.2154` n `23`; metal avg `0.2995` n `18`; unknown avg `1.219` n `417`
- 24h: commodity avg `0.2992` n `12`; crypto_alt avg `0.0683` n `228`; crypto_major avg `-0.6552` n `8`; equity avg `-0.2627` n `67`; fx avg `-0.1381` n `6`; index avg `0.0876` n `23`; metal avg `-0.2232` n `18`; unknown avg `0.8033` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1851`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.18`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1703`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1701`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1301`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.13`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1296`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1276`, n `669`, weak_sample_signal
