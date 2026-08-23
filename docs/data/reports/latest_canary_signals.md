# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T11:22:26.214393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.4345` n `230`; crypto_major avg `0.4866` n `8`; equity avg `0.0421` n `121`; fx avg `0.0057` n `6`; index avg `-0.0032` n `25`; metal avg `0.0038` n `20`; unknown avg `1.0986` n `795`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `0.7452` n `230`; crypto_major avg `0.3724` n `8`; equity avg `0.0934` n `121`; fx avg `-0.0054` n `6`; index avg `-0.0038` n `25`; metal avg `0.0224` n `20`; unknown avg `0.2303` n `795`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `2.5723` n `230`; crypto_major avg `1.491` n `8`; equity avg `0.2996` n `121`; fx avg `-0.2005` n `6`; index avg `0.0415` n `25`; metal avg `0.0071` n `20`; unknown avg `0.5024` n `794`
- 24h: commodity avg `0.0033` n `12`; crypto_alt avg `0.7514` n `230`; crypto_major avg `1.4817` n `8`; equity avg `0.468` n `121`; fx avg `0.0296` n `6`; index avg `0.039` n `25`; metal avg `0.0763` n `20`; unknown avg `2.9043` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
