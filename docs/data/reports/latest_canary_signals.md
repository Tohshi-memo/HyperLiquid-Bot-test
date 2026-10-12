# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T13:07:28.018810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0098` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `0.0307` n `235`; crypto_major avg `-0.0894` n `8`; equity avg `0.0836` n `151`; fx avg `0.0132` n `6`; index avg `0.0112` n `26`; metal avg `0.0441` n `20`; unknown avg `-0.061` n `1132`
- 1h: commodity avg `0.1128` n `13`; crypto_alt avg `-0.3679` n `235`; crypto_major avg `-0.4983` n `8`; equity avg `0.1293` n `151`; fx avg `0.0131` n `6`; index avg `0.0079` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.1506` n `1132`
- 4h: commodity avg `0.2882` n `13`; crypto_alt avg `-1.2689` n `235`; crypto_major avg `-1.0388` n `8`; equity avg `-0.1731` n `151`; fx avg `0.0102` n `6`; index avg `-0.029` n `26`; metal avg `0.025` n `20`; unknown avg `0.1467` n `1059`
- 24h: commodity avg `0.219` n `13`; crypto_alt avg `0.7389` n `235`; crypto_major avg `0.3279` n `8`; equity avg `-1.3086` n `151`; fx avg `-0.1165` n `6`; index avg `-0.1641` n `26`; metal avg `0.0039` n `20`; unknown avg `0.8952` n `911`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2388`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
