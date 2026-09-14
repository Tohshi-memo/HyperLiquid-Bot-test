# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T04:37:28.315944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0395` n `12`; crypto_alt avg `-0.0227` n `233`; crypto_major avg `0.0324` n `8`; equity avg `-0.0251` n `136`; fx avg `0.0008` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0159` n `20`; unknown avg `0.1544` n `888`
- 1h: commodity avg `-0.0493` n `12`; crypto_alt avg `0.0329` n `233`; crypto_major avg `0.0691` n `8`; equity avg `-0.0984` n `136`; fx avg `-0.0209` n `6`; index avg `-0.0307` n `27`; metal avg `-0.012` n `20`; unknown avg `8.2052` n `880`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `1.3728` n `233`; crypto_major avg `1.4292` n `8`; equity avg `0.1853` n `136`; fx avg `-0.0266` n `6`; index avg `0.0426` n `27`; metal avg `-0.004` n `20`; unknown avg `11.4841` n `762`
- 24h: commodity avg `0.6754` n `12`; crypto_alt avg `-0.488` n `233`; crypto_major avg `0.1334` n `8`; equity avg `-1.4437` n `136`; fx avg `0.0269` n `6`; index avg `-0.3337` n `26`; metal avg `-0.1516` n `20`; unknown avg `1.5692` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
