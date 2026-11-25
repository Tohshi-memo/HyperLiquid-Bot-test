# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T09:37:29.953265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.154` n `13`; crypto_alt avg `-0.2129` n `239`; crypto_major avg `-0.0737` n `8`; equity avg `-0.1385` n `168`; fx avg `0.0041` n `6`; index avg `-0.0042` n `27`; metal avg `0.0095` n `20`; unknown avg `158.573` n `1263`
- 1h: commodity avg `0.3489` n `13`; crypto_alt avg `-0.4545` n `239`; crypto_major avg `-0.6284` n `8`; equity avg `-1.1043` n `168`; fx avg `-0.0084` n `6`; index avg `-0.1311` n `27`; metal avg `-0.1055` n `20`; unknown avg `0.2472` n `1257`
- 4h: commodity avg `0.2104` n `13`; crypto_alt avg `-0.1698` n `239`; crypto_major avg `-0.5978` n `8`; equity avg `-1.2184` n `168`; fx avg `-0.0181` n `6`; index avg `-0.1098` n `27`; metal avg `-0.0355` n `20`; unknown avg `3.7258` n `1205`
- 24h: commodity avg `0.3561` n `13`; crypto_alt avg `-2.1695` n `239`; crypto_major avg `-3.0098` n `8`; equity avg `-5.0905` n `167`; fx avg `0.0531` n `6`; index avg `-0.4638` n `27`; metal avg `-0.8415` n `20`; unknown avg `651.1111` n `1033`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
