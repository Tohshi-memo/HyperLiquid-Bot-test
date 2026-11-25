# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T13:52:30.462320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1219` n `13`; crypto_alt avg `-0.2877` n `239`; crypto_major avg `-0.4063` n `8`; equity avg `-0.2524` n `168`; fx avg `0.0003` n `6`; index avg `-0.0128` n `27`; metal avg `-0.0559` n `20`; unknown avg `0.1001` n `1265`
- 1h: commodity avg `0.1713` n `13`; crypto_alt avg `-0.5917` n `239`; crypto_major avg `-0.9747` n `8`; equity avg `-0.686` n `168`; fx avg `-0.0036` n `6`; index avg `-0.0715` n `27`; metal avg `-0.2809` n `20`; unknown avg `-0.1882` n `1257`
- 4h: commodity avg `0.1553` n `13`; crypto_alt avg `-1.1724` n `239`; crypto_major avg `-0.8531` n `8`; equity avg `-0.878` n `168`; fx avg `0.0289` n `6`; index avg `-0.141` n `27`; metal avg `-0.3121` n `20`; unknown avg `92.5039` n `1189`
- 24h: commodity avg `0.4152` n `13`; crypto_alt avg `-2.4882` n `239`; crypto_major avg `-3.6219` n `8`; equity avg `-5.5058` n `168`; fx avg `-0.0406` n `6`; index avg `-0.4786` n `27`; metal avg `-1.2528` n `20`; unknown avg `444.295` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
