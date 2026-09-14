# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T17:07:28.990652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0717` n `12`; crypto_alt avg `-0.1628` n `233`; crypto_major avg `-0.2697` n `8`; equity avg `-0.1297` n `136`; fx avg `0.0271` n `6`; index avg `-0.0413` n `27`; metal avg `-0.0544` n `20`; unknown avg `0.1095` n `906`
- 1h: commodity avg `-0.1292` n `12`; crypto_alt avg `0.6767` n `233`; crypto_major avg `0.5418` n `8`; equity avg `0.447` n `136`; fx avg `0.0217` n `6`; index avg `0.0738` n `27`; metal avg `0.1424` n `20`; unknown avg `1.0653` n `878`
- 4h: commodity avg `-0.3441` n `12`; crypto_alt avg `1.3969` n `233`; crypto_major avg `1.3782` n `8`; equity avg `1.554` n `136`; fx avg `-0.0027` n `6`; index avg `0.2124` n `27`; metal avg `0.2563` n `20`; unknown avg `1.4382` n `864`
- 24h: commodity avg `0.2582` n `12`; crypto_alt avg `-0.0776` n `233`; crypto_major avg `1.5123` n `8`; equity avg `-0.2131` n `136`; fx avg `0.0616` n `6`; index avg `-0.1373` n `27`; metal avg `-0.2873` n `20`; unknown avg `1.0971` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
