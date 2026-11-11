# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T18:07:36.795623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `13`; crypto_alt avg `-0.2419` n `239`; crypto_major avg `-0.193` n `8`; equity avg `-0.2273` n `161`; fx avg `0.0053` n `6`; index avg `-0.0205` n `27`; metal avg `-0.0323` n `20`; unknown avg `-0.0091` n `1258`
- 1h: commodity avg `-0.1248` n `13`; crypto_alt avg `-0.4135` n `239`; crypto_major avg `0.0498` n `8`; equity avg `0.1284` n `161`; fx avg `-0.0057` n `6`; index avg `0.002` n `27`; metal avg `-0.0879` n `20`; unknown avg `-0.2591` n `1256`
- 4h: commodity avg `0.0273` n `13`; crypto_alt avg `0.074` n `239`; crypto_major avg `0.729` n `8`; equity avg `1.7487` n `161`; fx avg `0.013` n `6`; index avg `0.1598` n `27`; metal avg `-0.3831` n `20`; unknown avg `-0.4736` n `1225`
- 24h: commodity avg `0.4531` n `13`; crypto_alt avg `1.3009` n `239`; crypto_major avg `2.2537` n `8`; equity avg `6.7472` n `161`; fx avg `-0.1517` n `6`; index avg `0.6222` n `27`; metal avg `0.1594` n `20`; unknown avg `4.8409` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
