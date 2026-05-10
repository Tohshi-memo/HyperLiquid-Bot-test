# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T04:07:16.047813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `12`; crypto_alt avg `-0.0606` n `228`; crypto_major avg `-0.0466` n `8`; equity avg `0.0446` n `65`; fx avg `0.0` n `5`; index avg `0.0272` n `23`; metal avg `0.0532` n `18`; unknown avg `-0.0097` n `376`
- 1h: commodity avg `-0.1064` n `12`; crypto_alt avg `-0.0622` n `228`; crypto_major avg `0.0732` n `8`; equity avg `0.1497` n `65`; fx avg `0.0026` n `5`; index avg `0.0247` n `23`; metal avg `0.1166` n `18`; unknown avg `-0.3691` n `376`
- 4h: commodity avg `-0.1338` n `12`; crypto_alt avg `0.0656` n `228`; crypto_major avg `0.0918` n `8`; equity avg `0.2757` n `65`; fx avg `-0.027` n `5`; index avg `0.0954` n `23`; metal avg `0.1692` n `18`; unknown avg `-0.564` n `376`
- 24h: commodity avg `0.2352` n `12`; crypto_alt avg `-1.7237` n `228`; crypto_major avg `-1.0444` n `8`; equity avg `0.9243` n `65`; fx avg `-0.0074` n `5`; index avg `0.2969` n `23`; metal avg `0.2963` n `18`; unknown avg `-0.5912` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
