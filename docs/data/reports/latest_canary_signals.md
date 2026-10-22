# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T20:37:29.590385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `13`; crypto_alt avg `-0.3274` n `237`; crypto_major avg `-0.2211` n `8`; equity avg `-0.1754` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0098` n `20`; unknown avg `4.8343` n `1221`
- 1h: commodity avg `-0.0611` n `13`; crypto_alt avg `-0.492` n `237`; crypto_major avg `-0.4067` n `8`; equity avg `0.0914` n `151`; fx avg `-0.0149` n `6`; index avg `0.035` n `26`; metal avg `-0.0004` n `20`; unknown avg `9.2644` n `1173`
- 4h: commodity avg `0.1266` n `13`; crypto_alt avg `-0.7367` n `237`; crypto_major avg `-0.7877` n `8`; equity avg `-0.8611` n `151`; fx avg `-0.0292` n `6`; index avg `-0.0992` n `26`; metal avg `-0.1276` n `20`; unknown avg `0.7424` n `1173`
- 24h: commodity avg `0.5218` n `13`; crypto_alt avg `-5.7051` n `237`; crypto_major avg `-4.2238` n `8`; equity avg `-5.8175` n `151`; fx avg `-0.1836` n `6`; index avg `-0.6962` n `26`; metal avg `-1.0095` n `20`; unknown avg `60.5531` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
