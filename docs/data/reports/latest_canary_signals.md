# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T19:07:17.012649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0676` n `12`; crypto_alt avg `-0.0584` n `228`; crypto_major avg `0.0222` n `8`; equity avg `-0.1905` n `66`; fx avg `-0.0007` n `6`; index avg `0.0274` n `23`; metal avg `-0.1245` n `18`; unknown avg `-0.0025` n `383`
- 1h: commodity avg `0.5056` n `12`; crypto_alt avg `-0.2622` n `228`; crypto_major avg `-0.0826` n `8`; equity avg `-0.4948` n `66`; fx avg `0.008` n `6`; index avg `-0.1402` n `23`; metal avg `-0.2152` n `18`; unknown avg `-0.0548` n `383`
- 4h: commodity avg `0.4679` n `12`; crypto_alt avg `0.3833` n `228`; crypto_major avg `0.3247` n `8`; equity avg `1.443` n `66`; fx avg `-0.0243` n `6`; index avg `0.8766` n `23`; metal avg `0.1866` n `18`; unknown avg `1.5186` n `383`
- 24h: commodity avg `1.0727` n `12`; crypto_alt avg `0.782` n `228`; crypto_major avg `0.7824` n `8`; equity avg `0.9777` n `66`; fx avg `0.0204` n `6`; index avg `-0.0039` n `23`; metal avg `-2.313` n `18`; unknown avg `1.2011` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
