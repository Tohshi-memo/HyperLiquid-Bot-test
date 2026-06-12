# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T21:18:52.888828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1641` n `12`; crypto_alt avg `0.3553` n `228`; crypto_major avg `0.2172` n `8`; equity avg `0.0323` n `74`; fx avg `-0.0085` n `6`; index avg `-0.0148` n `23`; metal avg `-0.0577` n `18`; unknown avg `51.6237` n `643`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.023` n `228`; crypto_major avg `0.0084` n `8`; equity avg `-0.0312` n `74`; fx avg `-0.0226` n `6`; index avg `-0.0345` n `23`; metal avg `-0.0604` n `18`; unknown avg `0.6048` n `643`
- 4h: commodity avg `-0.1133` n `12`; crypto_alt avg `-0.2254` n `228`; crypto_major avg `-0.414` n `8`; equity avg `-0.548` n `74`; fx avg `-0.0344` n `6`; index avg `-0.1574` n `23`; metal avg `0.1448` n `18`; unknown avg `-0.04` n `643`
- 24h: commodity avg `-0.6383` n `12`; crypto_alt avg `-0.4609` n `228`; crypto_major avg `0.376` n `8`; equity avg `-0.373` n `74`; fx avg `-0.0768` n `6`; index avg `0.4394` n `23`; metal avg `0.4729` n `18`; unknown avg `40.5371` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
