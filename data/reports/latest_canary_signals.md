# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T01:07:22.806340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `13`; crypto_alt avg `-0.2509` n `239`; crypto_major avg `-0.2202` n `8`; equity avg `-0.4912` n `162`; fx avg `-0.0032` n `6`; index avg `-0.0727` n `27`; metal avg `-0.0757` n `20`; unknown avg `0.1429` n `1253`
- 1h: commodity avg `0.0185` n `13`; crypto_alt avg `-0.7767` n `239`; crypto_major avg `-0.79` n `8`; equity avg `-0.5903` n `162`; fx avg `-0.0384` n `6`; index avg `-0.1216` n `27`; metal avg `-0.1124` n `20`; unknown avg `0.341` n `1255`
- 4h: commodity avg `-0.2272` n `13`; crypto_alt avg `-0.404` n `239`; crypto_major avg `-0.2876` n `8`; equity avg `0.3933` n `162`; fx avg `-0.048` n `6`; index avg `0.0422` n `27`; metal avg `0.2208` n `20`; unknown avg `0.4066` n `1195`
- 24h: commodity avg `-0.2779` n `13`; crypto_alt avg `2.3826` n `239`; crypto_major avg `3.9156` n `8`; equity avg `1.7396` n `162`; fx avg `-0.0088` n `6`; index avg `0.1821` n `27`; metal avg `0.5554` n `20`; unknown avg `2.2473` n `1130`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
