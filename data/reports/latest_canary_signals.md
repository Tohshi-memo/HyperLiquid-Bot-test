# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T01:22:23.859419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2025` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `0.0947` n `233`; crypto_major avg `0.2051` n `8`; equity avg `0.0931` n `136`; fx avg `0.0056` n `6`; index avg `0.0218` n `27`; metal avg `0.0698` n `20`; unknown avg `0.7695` n `908`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.0676` n `233`; crypto_major avg `0.1308` n `8`; equity avg `0.2154` n `136`; fx avg `0.0033` n `6`; index avg `0.042` n `27`; metal avg `0.1703` n `20`; unknown avg `-0.1486` n `900`
- 4h: commodity avg `0.0357` n `12`; crypto_alt avg `-0.6798` n `233`; crypto_major avg `-1.0828` n `8`; equity avg `0.3433` n `136`; fx avg `0.0246` n `6`; index avg `0.1197` n `27`; metal avg `0.0022` n `20`; unknown avg `0.8626` n `888`
- 24h: commodity avg `-0.237` n `12`; crypto_alt avg `1.1262` n `233`; crypto_major avg `2.2303` n `8`; equity avg `0.6264` n `136`; fx avg `0.0442` n `6`; index avg `0.1042` n `27`; metal avg `-0.2695` n `20`; unknown avg `5.3966` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
