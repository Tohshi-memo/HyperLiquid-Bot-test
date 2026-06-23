# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T10:22:36.331177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.079` n `12`; crypto_alt avg `-0.11` n `228`; crypto_major avg `-0.1216` n `8`; equity avg `-0.0931` n `86`; fx avg `-0.0063` n `6`; index avg `-0.0035` n `23`; metal avg `0.0` n `20`; unknown avg `-0.0395` n `764`
- 1h: commodity avg `0.017` n `12`; crypto_alt avg `-0.0073` n `228`; crypto_major avg `-0.0595` n `8`; equity avg `0.0506` n `86`; fx avg `-0.0318` n `6`; index avg `-0.0051` n `23`; metal avg `0.1831` n `20`; unknown avg `-0.088` n `764`
- 4h: commodity avg `0.0768` n `12`; crypto_alt avg `-0.1871` n `228`; crypto_major avg `-0.8975` n `8`; equity avg `0.3364` n `86`; fx avg `-0.1215` n `6`; index avg `0.0125` n `23`; metal avg `0.0614` n `20`; unknown avg `-0.5356` n `620`
- 24h: commodity avg `-0.6307` n `12`; crypto_alt avg `-3.7504` n `228`; crypto_major avg `-4.0587` n `8`; equity avg `-4.3053` n `85`; fx avg `-0.1457` n `6`; index avg `-0.8384` n `23`; metal avg `-1.3338` n `18`; unknown avg `0.7306` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
