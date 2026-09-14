# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T02:22:28.448314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `0.3874` n `233`; crypto_major avg `0.3063` n `8`; equity avg `0.0316` n `136`; fx avg `0.0052` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0166` n `20`; unknown avg `0.3905` n `894`
- 1h: commodity avg `-0.1694` n `12`; crypto_alt avg `1.1664` n `233`; crypto_major avg `0.9157` n `8`; equity avg `0.5997` n `136`; fx avg `0.0026` n `6`; index avg `0.1154` n `27`; metal avg `0.1178` n `20`; unknown avg `2.7285` n `892`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `1.3007` n `233`; crypto_major avg `0.9924` n `8`; equity avg `-0.009` n `136`; fx avg `0.015` n `6`; index avg `0.0043` n `27`; metal avg `0.1371` n `20`; unknown avg `13.1451` n `768`
- 24h: commodity avg `0.6764` n `12`; crypto_alt avg `-0.6199` n `233`; crypto_major avg `-0.7289` n `8`; equity avg `-1.3714` n `136`; fx avg `0.0652` n `6`; index avg `-0.2968` n `26`; metal avg `-0.0533` n `20`; unknown avg `1.7131` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
