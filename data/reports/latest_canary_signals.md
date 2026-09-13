# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T12:07:29.319385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0293` n `12`; crypto_alt avg `-0.1443` n `233`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0748` n `136`; fx avg `-0.0055` n `6`; index avg `-0.0082` n `27`; metal avg `0.0011` n `20`; unknown avg `0.0215` n `832`
- 1h: commodity avg `0.0972` n `12`; crypto_alt avg `-0.0491` n `233`; crypto_major avg `0.0673` n `8`; equity avg `-0.0959` n `136`; fx avg `-0.0053` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0066` n `20`; unknown avg `0.1756` n `832`
- 4h: commodity avg `0.1811` n `12`; crypto_alt avg `-0.7969` n `233`; crypto_major avg `-0.8988` n `8`; equity avg `-0.8262` n `136`; fx avg `0.0108` n `6`; index avg `-0.1451` n `27`; metal avg `-0.0472` n `20`; unknown avg `0.6504` n `826`
- 24h: commodity avg `0.2704` n `12`; crypto_alt avg `-0.801` n `233`; crypto_major avg `-1.9853` n `8`; equity avg `-1.8519` n `136`; fx avg `0.0026` n `6`; index avg `-0.2941` n `26`; metal avg `-0.0807` n `20`; unknown avg `-0.2085` n `704`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
