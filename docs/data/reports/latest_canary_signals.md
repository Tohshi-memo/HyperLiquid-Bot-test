# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T08:22:27.964949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1256` n `13`; crypto_alt avg `-0.1664` n `235`; crypto_major avg `-0.2928` n `8`; equity avg `-0.153` n `151`; fx avg `-0.0001` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0471` n `20`; unknown avg `-0.0209` n `1133`
- 1h: commodity avg `0.0704` n `13`; crypto_alt avg `-0.3954` n `235`; crypto_major avg `-0.5724` n `8`; equity avg `-0.2454` n `151`; fx avg `-0.0224` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0611` n `20`; unknown avg `-0.0391` n `1059`
- 4h: commodity avg `0.2434` n `13`; crypto_alt avg `-0.0309` n `235`; crypto_major avg `0.1508` n `8`; equity avg `-0.4002` n `151`; fx avg `-0.0361` n `6`; index avg `-0.0439` n `26`; metal avg `-0.1277` n `20`; unknown avg `0.2524` n `981`
- 24h: commodity avg `-0.2505` n `13`; crypto_alt avg `2.1789` n `235`; crypto_major avg `1.4781` n `8`; equity avg `-0.7684` n `151`; fx avg `-0.1036` n `6`; index avg `-0.0559` n `26`; metal avg `-0.0074` n `20`; unknown avg `0.1269` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.21`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
