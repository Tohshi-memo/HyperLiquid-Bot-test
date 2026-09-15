# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T11:37:34.938457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0741` n `12`; crypto_alt avg `-0.3072` n `233`; crypto_major avg `-0.1964` n `8`; equity avg `-0.0845` n `136`; fx avg `-0.0137` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0218` n `20`; unknown avg `1.4042` n `908`
- 1h: commodity avg `-0.1849` n `12`; crypto_alt avg `-0.4138` n `233`; crypto_major avg `-0.2557` n `8`; equity avg `0.0887` n `136`; fx avg `-0.0122` n `6`; index avg `0.0504` n `27`; metal avg `0.081` n `20`; unknown avg `1.8097` n `906`
- 4h: commodity avg `-0.2641` n `12`; crypto_alt avg `-0.6587` n `233`; crypto_major avg `-0.1731` n `8`; equity avg `0.331` n `136`; fx avg `0.0031` n `6`; index avg `0.1049` n `27`; metal avg `0.0928` n `20`; unknown avg `1.7008` n `898`
- 24h: commodity avg `-0.2719` n `12`; crypto_alt avg `-1.7272` n `233`; crypto_major avg `-1.0763` n `8`; equity avg `0.4666` n `136`; fx avg `0.1657` n `6`; index avg `0.0708` n `27`; metal avg `0.0553` n `20`; unknown avg `-0.8165` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
