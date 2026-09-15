# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T15:52:28.862918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `-0.0301` n `233`; crypto_major avg `0.1099` n `8`; equity avg `0.0522` n `137`; fx avg `-0.0272` n `6`; index avg `-0.0026` n `27`; metal avg `0.0561` n `20`; unknown avg `0.1785` n `909`
- 1h: commodity avg `-0.0473` n `12`; crypto_alt avg `1.0631` n `233`; crypto_major avg `1.0571` n `8`; equity avg `0.3893` n `137`; fx avg `-0.0026` n `6`; index avg `0.0406` n `27`; metal avg `0.1221` n `20`; unknown avg `0.5267` n `907`
- 4h: commodity avg `0.3313` n `12`; crypto_alt avg `-0.4512` n `233`; crypto_major avg `-0.836` n `8`; equity avg `-0.7652` n `137`; fx avg `0.0442` n `6`; index avg `-0.1393` n `27`; metal avg `0.0364` n `20`; unknown avg `1.6648` n `873`
- 24h: commodity avg `0.1702` n `12`; crypto_alt avg `-2.0148` n `233`; crypto_major avg `-2.058` n `8`; equity avg `-0.9643` n `137`; fx avg `0.2255` n `6`; index avg `-0.1114` n `27`; metal avg `0.0384` n `20`; unknown avg `0.2092` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
