# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T07:52:31.559193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `-0.1181` n `228`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0192` n `86`; fx avg `0.002` n `6`; index avg `0.0025` n `23`; metal avg `-0.0689` n `20`; unknown avg `0.0354` n `765`
- 1h: commodity avg `-0.1261` n `12`; crypto_alt avg `0.5551` n `228`; crypto_major avg `0.7895` n `8`; equity avg `0.0936` n `86`; fx avg `0.0131` n `6`; index avg `0.0229` n `23`; metal avg `0.0202` n `20`; unknown avg `0.0381` n `757`
- 4h: commodity avg `-0.0323` n `12`; crypto_alt avg `1.305` n `228`; crypto_major avg `1.5693` n `8`; equity avg `0.8741` n `86`; fx avg `-0.066` n `6`; index avg `0.2285` n `23`; metal avg `0.6005` n `20`; unknown avg `0.3631` n `733`
- 24h: commodity avg `0.0328` n `12`; crypto_alt avg `-1.487` n `228`; crypto_major avg `-1.3194` n `8`; equity avg `-3.7097` n `86`; fx avg `0.0405` n `6`; index avg `-0.5305` n `23`; metal avg `0.5074` n `20`; unknown avg `0.6205` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
