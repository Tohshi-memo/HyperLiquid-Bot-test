# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T00:52:25.999797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `0.0714` n `237`; crypto_major avg `0.1242` n `8`; equity avg `0.5374` n `151`; fx avg `0.0267` n `6`; index avg `0.0834` n `26`; metal avg `0.0742` n `20`; unknown avg `0.6097` n `1233`
- 1h: commodity avg `-0.0962` n `13`; crypto_alt avg `0.214` n `237`; crypto_major avg `0.2397` n `8`; equity avg `0.8838` n `151`; fx avg `-0.055` n `6`; index avg `0.0718` n `26`; metal avg `0.0386` n `20`; unknown avg `0.7453` n `1225`
- 4h: commodity avg `-0.0521` n `13`; crypto_alt avg `0.4702` n `237`; crypto_major avg `0.5601` n `8`; equity avg `0.7067` n `151`; fx avg `-0.0574` n `6`; index avg `0.066` n `26`; metal avg `0.0356` n `20`; unknown avg `0.5792` n `1179`
- 24h: commodity avg `0.4202` n `13`; crypto_alt avg `-4.6502` n `237`; crypto_major avg `-3.2231` n `8`; equity avg `-4.4758` n `151`; fx avg `-0.2213` n `6`; index avg `-0.5108` n `26`; metal avg `-0.966` n `20`; unknown avg `54.1029` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
