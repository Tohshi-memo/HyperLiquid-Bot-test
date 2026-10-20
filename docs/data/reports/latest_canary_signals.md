# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T12:07:28.643255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `13`; crypto_alt avg `0.08` n `237`; crypto_major avg `0.0618` n `8`; equity avg `-0.0391` n `151`; fx avg `-0.0003` n `6`; index avg `0.0028` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.1763` n `1190`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.0713` n `237`; crypto_major avg `-0.0548` n `8`; equity avg `-0.1668` n `151`; fx avg `-0.0024` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0455` n `20`; unknown avg `-0.3601` n `1188`
- 4h: commodity avg `0.1263` n `13`; crypto_alt avg `-0.0715` n `237`; crypto_major avg `0.0427` n `8`; equity avg `-0.5983` n `151`; fx avg `0.0019` n `6`; index avg `-0.0839` n `26`; metal avg `-0.0737` n `20`; unknown avg `1.6667` n `1188`
- 24h: commodity avg `0.248` n `13`; crypto_alt avg `-0.0944` n `237`; crypto_major avg `-0.7811` n `8`; equity avg `-2.5769` n `151`; fx avg `-0.038` n `6`; index avg `-0.3152` n `26`; metal avg `-0.3373` n `20`; unknown avg `0.471` n `1045`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
