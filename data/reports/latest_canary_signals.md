# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T01:37:28.553835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.1724` n `237`; crypto_major avg `0.0174` n `8`; equity avg `0.0728` n `151`; fx avg `0.0132` n `6`; index avg `0.0274` n `26`; metal avg `0.0763` n `20`; unknown avg `-0.1797` n `1199`
- 1h: commodity avg `0.0606` n `13`; crypto_alt avg `-0.1302` n `237`; crypto_major avg `-0.2033` n `8`; equity avg `-0.1905` n `151`; fx avg `0.0411` n `6`; index avg `-0.0475` n `26`; metal avg `-0.0288` n `20`; unknown avg `0.6103` n `1197`
- 4h: commodity avg `0.0999` n `13`; crypto_alt avg `0.0874` n `237`; crypto_major avg `0.0222` n `8`; equity avg `0.4362` n `151`; fx avg `0.0105` n `6`; index avg `0.0389` n `26`; metal avg `-0.0525` n `20`; unknown avg `-0.0162` n `1119`
- 24h: commodity avg `-0.0459` n `13`; crypto_alt avg `3.0048` n `237`; crypto_major avg `2.1351` n `8`; equity avg `2.669` n `151`; fx avg `0.0581` n `6`; index avg `0.3196` n `26`; metal avg `0.2028` n `20`; unknown avg `212.1621` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
