# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T09:22:29.608420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `0.1945` n `237`; crypto_major avg `0.207` n `8`; equity avg `0.1363` n `152`; fx avg `0.006` n `6`; index avg `0.0151` n `26`; metal avg `0.0018` n `20`; unknown avg `1.5997` n `1240`
- 1h: commodity avg `-0.1301` n `13`; crypto_alt avg `0.8082` n `237`; crypto_major avg `0.527` n `8`; equity avg `0.6502` n `152`; fx avg `0.0009` n `6`; index avg `0.1086` n `26`; metal avg `-0.0015` n `20`; unknown avg `2.2007` n `1240`
- 4h: commodity avg `0.0517` n `13`; crypto_alt avg `0.0866` n `237`; crypto_major avg `0.0797` n `8`; equity avg `-0.1747` n `152`; fx avg `0.0083` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0267` n `20`; unknown avg `1.4674` n `1126`
- 24h: commodity avg `-0.529` n `13`; crypto_alt avg `0.859` n `237`; crypto_major avg `0.5544` n `8`; equity avg `-0.0206` n `152`; fx avg `0.0444` n `6`; index avg `0.0837` n `26`; metal avg `0.199` n `20`; unknown avg `-0.0611` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2565`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
