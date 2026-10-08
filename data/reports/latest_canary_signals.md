# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T12:52:33.477904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.186` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.3537` n `235`; crypto_major avg `-0.1497` n `8`; equity avg `-0.1119` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0127` n `26`; metal avg `-0.074` n `20`; unknown avg `-0.3564` n `1077`
- 1h: commodity avg `0.0644` n `13`; crypto_alt avg `-0.7302` n `235`; crypto_major avg `-0.4729` n `8`; equity avg `-0.0897` n `150`; fx avg `0.0138` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0915` n `20`; unknown avg `-0.535` n `1069`
- 4h: commodity avg `0.1364` n `13`; crypto_alt avg `-0.892` n `235`; crypto_major avg `-1.2317` n `8`; equity avg `-0.3543` n `150`; fx avg `0.0211` n `6`; index avg `-0.0457` n `26`; metal avg `-0.2137` n `20`; unknown avg `-0.1533` n `1069`
- 24h: commodity avg `0.8043` n `13`; crypto_alt avg `-0.0565` n `235`; crypto_major avg `-2.2036` n `8`; equity avg `-1.2703` n `150`; fx avg `0.0895` n `6`; index avg `-0.1858` n `26`; metal avg `0.0823` n `20`; unknown avg `416.6732` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
