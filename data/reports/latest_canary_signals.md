# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T17:37:26.010315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.075` n `239`; crypto_major avg `-0.0786` n `8`; equity avg `-0.0489` n `166`; fx avg `-0.0054` n `6`; index avg `-0.0051` n `27`; metal avg `-0.0111` n `20`; unknown avg `1.4094` n `1256`
- 1h: commodity avg `0.0325` n `13`; crypto_alt avg `0.1731` n `239`; crypto_major avg `0.2732` n `8`; equity avg `0.0133` n `166`; fx avg `0.006` n `6`; index avg `0.0172` n `27`; metal avg `0.0439` n `20`; unknown avg `159.7211` n `1252`
- 4h: commodity avg `0.0158` n `13`; crypto_alt avg `0.0754` n `239`; crypto_major avg `0.028` n `8`; equity avg `0.0054` n `166`; fx avg `0.0042` n `6`; index avg `-0.0047` n `27`; metal avg `-0.0453` n `20`; unknown avg `162.0206` n `1240`
- 24h: commodity avg `0.5049` n `13`; crypto_alt avg `1.308` n `239`; crypto_major avg `1.8811` n `8`; equity avg `0.3097` n `166`; fx avg `-0.1289` n `6`; index avg `0.0001` n `27`; metal avg `0.1928` n `20`; unknown avg `0.2093` n `1134`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
