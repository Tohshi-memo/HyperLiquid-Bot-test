# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T13:25:50.010211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `-0.3373` n `228`; crypto_major avg `-0.3002` n `8`; equity avg `0.0681` n `67`; fx avg `0.0063` n `6`; index avg `0.0196` n `23`; metal avg `0.1991` n `18`; unknown avg `1.0455` n `418`
- 1h: commodity avg `0.5323` n `12`; crypto_alt avg `-0.2182` n `228`; crypto_major avg `-0.2471` n `8`; equity avg `-0.0234` n `67`; fx avg `0.0158` n `6`; index avg `0.0038` n `23`; metal avg `0.1727` n `18`; unknown avg `-0.3481` n `417`
- 4h: commodity avg `-0.0999` n `12`; crypto_alt avg `0.9273` n `228`; crypto_major avg `0.9766` n `8`; equity avg `0.3216` n `67`; fx avg `-0.0243` n `6`; index avg `0.2628` n `23`; metal avg `0.3122` n `18`; unknown avg `1.2049` n `417`
- 24h: commodity avg `0.3168` n `12`; crypto_alt avg `0.1298` n `228`; crypto_major avg `-0.6656` n `8`; equity avg `-0.2643` n `67`; fx avg `-0.1384` n `6`; index avg `0.1352` n `23`; metal avg `-0.2105` n `18`; unknown avg `0.8164` n `395`

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
