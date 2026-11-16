# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T23:37:24.780067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `-0.3831` n `239`; crypto_major avg `-0.4743` n `8`; equity avg `-0.3083` n `162`; fx avg `0.0073` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0195` n `20`; unknown avg `0.6236` n `1266`
- 1h: commodity avg `-0.0174` n `13`; crypto_alt avg `-0.6943` n `239`; crypto_major avg `-0.6249` n `8`; equity avg `-0.5498` n `162`; fx avg `-0.0067` n `6`; index avg `-0.0346` n `27`; metal avg `-0.026` n `20`; unknown avg `0.1131` n `1232`
- 4h: commodity avg `-0.0973` n `13`; crypto_alt avg `-0.3016` n `239`; crypto_major avg `0.3252` n `8`; equity avg `-0.9551` n `162`; fx avg `-0.004` n `6`; index avg `-0.0878` n `27`; metal avg `-0.0851` n `20`; unknown avg `383.4503` n `1188`
- 24h: commodity avg `-0.9431` n `13`; crypto_alt avg `-1.0945` n `239`; crypto_major avg `-0.7198` n `8`; equity avg `-4.7561` n `162`; fx avg `-0.1094` n `6`; index avg `-0.5431` n `27`; metal avg `-0.6735` n `20`; unknown avg `508.7199` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
