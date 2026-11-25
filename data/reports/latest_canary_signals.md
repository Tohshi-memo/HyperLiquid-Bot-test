# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T05:07:30.931742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `0.3663` n `239`; crypto_major avg `0.2378` n `8`; equity avg `0.0421` n `168`; fx avg `-0.0123` n `6`; index avg `0.0088` n `27`; metal avg `-0.0453` n `20`; unknown avg `4.1256` n `1255`
- 1h: commodity avg `0.0642` n `13`; crypto_alt avg `0.6741` n `239`; crypto_major avg `0.034` n `8`; equity avg `-0.1633` n `168`; fx avg `-0.0197` n `6`; index avg `0.0064` n `27`; metal avg `0.0042` n `20`; unknown avg `0.0073` n `1255`
- 4h: commodity avg `-0.2132` n `13`; crypto_alt avg `0.818` n `239`; crypto_major avg `-0.3626` n `8`; equity avg `-0.5875` n `168`; fx avg `-0.0656` n `6`; index avg `-0.0109` n `27`; metal avg `0.0008` n `20`; unknown avg `1.4065` n `1245`
- 24h: commodity avg `0.5809` n `13`; crypto_alt avg `-2.7996` n `239`; crypto_major avg `-3.1345` n `8`; equity avg `-5.4646` n `167`; fx avg `0.154` n `6`; index avg `-0.5214` n `27`; metal avg `-1.014` n `20`; unknown avg `701.9534` n `1029`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
