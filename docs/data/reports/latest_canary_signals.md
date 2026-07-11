# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T01:52:23.847252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `12`; crypto_alt avg `-0.1556` n `229`; crypto_major avg `-0.2581` n `8`; equity avg `-0.1002` n `92`; fx avg `0.0037` n `6`; index avg `-0.0121` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.0473` n `765`
- 1h: commodity avg `-0.0872` n `12`; crypto_alt avg `0.0329` n `229`; crypto_major avg `-0.1179` n `8`; equity avg `-0.0739` n `92`; fx avg `0.0026` n `6`; index avg `-0.0107` n `25`; metal avg `-0.0078` n `20`; unknown avg `0.1244` n `765`
- 4h: commodity avg `-0.0589` n `12`; crypto_alt avg `0.0334` n `229`; crypto_major avg `-0.1311` n `8`; equity avg `-0.0231` n `92`; fx avg `0.0003` n `6`; index avg `-0.028` n `25`; metal avg `-0.0067` n `20`; unknown avg `3.1869` n `765`
- 24h: commodity avg `-0.3717` n `12`; crypto_alt avg `0.1087` n `229`; crypto_major avg `-0.3722` n `8`; equity avg `-0.8976` n `92`; fx avg `-0.203` n `6`; index avg `0.011` n `25`; metal avg `0.0907` n `20`; unknown avg `3.7288` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
