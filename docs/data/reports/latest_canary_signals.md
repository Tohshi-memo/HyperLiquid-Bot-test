# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T21:07:29.930997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `13`; crypto_alt avg `-0.3556` n `236`; crypto_major avg `-0.1731` n `8`; equity avg `-0.6147` n `151`; fx avg `-0.0196` n `6`; index avg `-0.0714` n `26`; metal avg `0.0042` n `20`; unknown avg `0.7203` n `1128`
- 1h: commodity avg `-0.0514` n `13`; crypto_alt avg `-0.2908` n `236`; crypto_major avg `-0.2513` n `8`; equity avg `-0.5736` n `151`; fx avg `-0.0188` n `6`; index avg `-0.0724` n `26`; metal avg `-0.006` n `20`; unknown avg `0.3684` n `1074`
- 4h: commodity avg `-0.1128` n `13`; crypto_alt avg `0.287` n `236`; crypto_major avg `0.2537` n `8`; equity avg `0.9207` n `151`; fx avg `-0.0198` n `6`; index avg `0.0831` n `26`; metal avg `0.1844` n `20`; unknown avg `-0.1048` n `1052`
- 24h: commodity avg `-0.2289` n `13`; crypto_alt avg `0.639` n `236`; crypto_major avg `0.6826` n `8`; equity avg `-0.1075` n `151`; fx avg `0.1701` n `6`; index avg `-0.0827` n `26`; metal avg `0.5215` n `20`; unknown avg `23.3774` n `926`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.086`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.072`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0504`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.05`, n `666`, weak_sample_signal
