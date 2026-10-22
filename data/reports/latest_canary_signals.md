# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T14:07:29.627091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `0.4059` n `237`; crypto_major avg `0.2811` n `8`; equity avg `0.2013` n `151`; fx avg `0.0178` n `6`; index avg `0.0257` n `26`; metal avg `0.0089` n `20`; unknown avg `0.7085` n `1133`
- 1h: commodity avg `-0.1255` n `13`; crypto_alt avg `0.0972` n `237`; crypto_major avg `0.1985` n `8`; equity avg `0.1277` n `151`; fx avg `0.0019` n `6`; index avg `0.0456` n `26`; metal avg `-0.1136` n `20`; unknown avg `0.5928` n `1131`
- 4h: commodity avg `0.0375` n `13`; crypto_alt avg `-0.2589` n `237`; crypto_major avg `-0.0747` n `8`; equity avg `-0.0137` n `151`; fx avg `0.0384` n `6`; index avg `0.062` n `26`; metal avg `-0.1407` n `20`; unknown avg `0.2973` n `1125`
- 24h: commodity avg `-0.3668` n `13`; crypto_alt avg `-2.3373` n `237`; crypto_major avg `-1.7711` n `8`; equity avg `-2.1446` n `151`; fx avg `-0.1408` n `6`; index avg `-0.2695` n `26`; metal avg `-0.643` n `20`; unknown avg `10.4373` n `888`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
