# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T06:22:28.160119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `0.0906` n `237`; crypto_major avg `-0.0411` n `8`; equity avg `-0.047` n `151`; fx avg `0.014` n `6`; index avg `-0.0246` n `26`; metal avg `-0.0612` n `20`; unknown avg `0.018` n `1200`
- 1h: commodity avg `0.0188` n `13`; crypto_alt avg `-0.0603` n `237`; crypto_major avg `-0.2086` n `8`; equity avg `-0.0686` n `151`; fx avg `0.0207` n `6`; index avg `-0.0379` n `26`; metal avg `-0.1383` n `20`; unknown avg `-0.082` n `1180`
- 4h: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.0264` n `237`; crypto_major avg `-0.1937` n `8`; equity avg `-0.2606` n `151`; fx avg `-0.0583` n `6`; index avg `-0.0917` n `26`; metal avg `-0.1466` n `20`; unknown avg `0.52` n `1173`
- 24h: commodity avg `0.0334` n `13`; crypto_alt avg `2.6042` n `237`; crypto_major avg `1.7104` n `8`; equity avg `2.5499` n `151`; fx avg `-0.0212` n `6`; index avg `0.3128` n `26`; metal avg `-0.2082` n `20`; unknown avg `5261.1943` n `992`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
