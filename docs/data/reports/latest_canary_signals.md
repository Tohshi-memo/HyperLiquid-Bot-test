# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T08:52:42.484139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0475` n `13`; crypto_alt avg `0.1014` n `239`; crypto_major avg `0.2874` n `8`; equity avg `0.0524` n `166`; fx avg `-0.0049` n `6`; index avg `0.0054` n `27`; metal avg `0.0444` n `20`; unknown avg `0.4544` n `1262`
- 1h: commodity avg `-0.1008` n `13`; crypto_alt avg `-0.3089` n `239`; crypto_major avg `-0.0652` n `8`; equity avg `-0.6448` n `166`; fx avg `0.0093` n `6`; index avg `-0.0748` n `27`; metal avg `-0.1124` n `20`; unknown avg `0.8467` n `1236`
- 4h: commodity avg `0.1117` n `13`; crypto_alt avg `-0.0362` n `239`; crypto_major avg `-0.1385` n `8`; equity avg `-0.7363` n `166`; fx avg `0.0502` n `6`; index avg `-0.0916` n `27`; metal avg `-0.1774` n `20`; unknown avg `-0.0348` n `1194`
- 24h: commodity avg `-0.7919` n `13`; crypto_alt avg `-0.1085` n `239`; crypto_major avg `-0.6045` n `8`; equity avg `2.9292` n `166`; fx avg `-0.2388` n `6`; index avg `0.5028` n `27`; metal avg `-0.2685` n `20`; unknown avg `1.4389` n `1136`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
