# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T14:22:30.481716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `13`; crypto_alt avg `0.1758` n `237`; crypto_major avg `0.1826` n `8`; equity avg `0.604` n `151`; fx avg `-0.0161` n `6`; index avg `0.112` n `26`; metal avg `0.0162` n `20`; unknown avg `0.4473` n `1141`
- 1h: commodity avg `-0.0588` n `13`; crypto_alt avg `-0.6828` n `237`; crypto_major avg `-0.8291` n `8`; equity avg `-0.4966` n `151`; fx avg `-0.0097` n `6`; index avg `0.0317` n `26`; metal avg `-0.1076` n `20`; unknown avg `0.68` n `1139`
- 4h: commodity avg `-0.269` n `13`; crypto_alt avg `-0.4726` n `237`; crypto_major avg `-0.6414` n `8`; equity avg `0.1555` n `151`; fx avg `0.0181` n `6`; index avg `0.0857` n `26`; metal avg `-0.1615` n `20`; unknown avg `0.7767` n `1103`
- 24h: commodity avg `-0.3991` n `13`; crypto_alt avg `0.1562` n `237`; crypto_major avg `0.7884` n `8`; equity avg `3.0002` n `151`; fx avg `-0.0292` n `6`; index avg `0.6107` n `26`; metal avg `0.0853` n `20`; unknown avg `3.484` n `915`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2038`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1511`, n `667`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1375`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1288`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.074`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0641`, n `667`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
