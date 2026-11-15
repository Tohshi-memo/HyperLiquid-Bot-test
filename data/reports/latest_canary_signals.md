# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T01:52:24.831003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.5306` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.5118` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0054` n `13`; crypto_alt avg `-0.237` n `239`; crypto_major avg `-0.2098` n `8`; equity avg `-0.0826` n `162`; fx avg `0.0052` n `6`; index avg `-0.0087` n `27`; metal avg `-0.038` n `20`; unknown avg `0.0969` n `1262`
- 1h: commodity avg `0.0075` n `13`; crypto_alt avg `-0.986` n `239`; crypto_major avg `-1.5399` n `8`; equity avg `-0.3213` n `162`; fx avg `0.0151` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0793` n `20`; unknown avg `2.1246` n `1260`
- 4h: commodity avg `0.1175` n `13`; crypto_alt avg `-0.4895` n `239`; crypto_major avg `-1.5248` n `8`; equity avg `-0.3769` n `162`; fx avg `0.0104` n `6`; index avg `-0.013` n `27`; metal avg `-0.0751` n `20`; unknown avg `164.8791` n `1216`
- 24h: commodity avg `-0.0201` n `13`; crypto_alt avg `-9.1746` n `239`; crypto_major avg `-9.6667` n `8`; equity avg `-1.7733` n `162`; fx avg `0.0281` n `6`; index avg `-0.1378` n `27`; metal avg `-0.6281` n `20`; unknown avg `46.4873` n `1072`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
