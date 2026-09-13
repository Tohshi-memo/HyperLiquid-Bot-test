# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T20:52:24.094340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.042` n `12`; crypto_alt avg `0.1366` n `233`; crypto_major avg `0.0713` n `8`; equity avg `0.0112` n `136`; fx avg `-0.0037` n `6`; index avg `0.0017` n `27`; metal avg `0.0137` n `20`; unknown avg `9.1054` n `816`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.3736` n `233`; crypto_major avg `0.3997` n `8`; equity avg `0.0429` n `136`; fx avg `0.0078` n `6`; index avg `0.0262` n `27`; metal avg `-0.0082` n `20`; unknown avg `14.0236` n `802`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.3673` n `233`; crypto_major avg `0.3653` n `8`; equity avg `0.0556` n `136`; fx avg `0.0039` n `6`; index avg `-0.014` n `27`; metal avg `-0.0207` n `20`; unknown avg `5.0837` n `736`
- 24h: commodity avg `0.3626` n `12`; crypto_alt avg `0.23` n `233`; crypto_major avg `-0.3632` n `8`; equity avg `-1.1765` n `136`; fx avg `0.0178` n `6`; index avg `-0.2361` n `26`; metal avg `-0.0866` n `20`; unknown avg `3.0462` n `690`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
