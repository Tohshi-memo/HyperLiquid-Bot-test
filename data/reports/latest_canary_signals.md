# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T23:37:23.354313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1997` n `12`; crypto_alt avg `0.0727` n `228`; crypto_major avg `0.0719` n `8`; equity avg `0.117` n `66`; fx avg `-0.0053` n `6`; index avg `0.1046` n `23`; metal avg `0.0822` n `18`; unknown avg `-0.0415` n `383`
- 1h: commodity avg `-0.1577` n `12`; crypto_alt avg `0.2705` n `228`; crypto_major avg `0.3567` n `8`; equity avg `0.2244` n `66`; fx avg `-0.0094` n `6`; index avg `0.1533` n `23`; metal avg `0.2253` n `18`; unknown avg `-0.1933` n `383`
- 4h: commodity avg `-0.2431` n `12`; crypto_alt avg `-0.153` n `228`; crypto_major avg `-0.0207` n `8`; equity avg `0.0864` n `66`; fx avg `-0.0193` n `6`; index avg `0.1013` n `23`; metal avg `0.1905` n `18`; unknown avg `-0.3765` n `383`
- 24h: commodity avg `0.9657` n `12`; crypto_alt avg `-1.051` n `228`; crypto_major avg `-0.5367` n `8`; equity avg `-0.2338` n `66`; fx avg `0.0534` n `6`; index avg `-0.61` n `23`; metal avg `-2.8893` n `18`; unknown avg `0.8466` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
