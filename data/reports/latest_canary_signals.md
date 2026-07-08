# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T07:22:31.264374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `12`; crypto_alt avg `0.1231` n `229`; crypto_major avg `-0.0329` n `8`; equity avg `0.0449` n `91`; fx avg `0.0018` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0663` n `20`; unknown avg `-0.0311` n `763`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.1165` n `229`; crypto_major avg `0.1079` n `8`; equity avg `-0.2241` n `91`; fx avg `0.0037` n `6`; index avg `-0.0564` n `25`; metal avg `-0.2176` n `20`; unknown avg `-0.1048` n `763`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.4705` n `229`; crypto_major avg `-0.8321` n `8`; equity avg `-0.8353` n `91`; fx avg `-0.0493` n `6`; index avg `-0.3236` n `25`; metal avg `-0.1621` n `20`; unknown avg `-0.2703` n `743`
- 24h: commodity avg `0.7323` n `12`; crypto_alt avg `-2.9467` n `229`; crypto_major avg `-2.7895` n `8`; equity avg `-2.0206` n `91`; fx avg `-0.2418` n `6`; index avg `-0.426` n `25`; metal avg `-0.1408` n `20`; unknown avg `-0.66` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
