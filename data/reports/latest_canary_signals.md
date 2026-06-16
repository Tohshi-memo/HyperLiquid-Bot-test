# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T05:40:31.918169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0605` n `228`; crypto_major avg `0.0855` n `8`; equity avg `-0.0971` n `77`; fx avg `-0.0019` n `6`; index avg `0.137` n `23`; metal avg `-0.3096` n `18`; unknown avg `0.0761` n `687`
- 1h: commodity avg `-0.107` n `12`; crypto_alt avg `0.5509` n `228`; crypto_major avg `0.6942` n `8`; equity avg `0.0209` n `77`; fx avg `-0.0231` n `6`; index avg `0.0647` n `23`; metal avg `-0.2208` n `18`; unknown avg `-0.1132` n `687`
- 4h: commodity avg `-0.4031` n `12`; crypto_alt avg `0.0412` n `228`; crypto_major avg `0.3133` n `8`; equity avg `0.3843` n `77`; fx avg `-0.0207` n `6`; index avg `0.0341` n `23`; metal avg `0.0409` n `18`; unknown avg `-0.1576` n `679`
- 24h: commodity avg `0.1687` n `12`; crypto_alt avg `0.121` n `228`; crypto_major avg `2.3728` n `8`; equity avg `1.2149` n `76`; fx avg `-0.0867` n `6`; index avg `0.5727` n `23`; metal avg `-0.5065` n `18`; unknown avg `1.0321` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
