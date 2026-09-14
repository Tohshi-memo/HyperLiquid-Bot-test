# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T01:22:26.519111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0095` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `-0.0361` n `233`; crypto_major avg `-0.1095` n `8`; equity avg `-0.1218` n `136`; fx avg `0.0026` n `6`; index avg `-0.0297` n `27`; metal avg `0.0194` n `20`; unknown avg `0.7943` n `894`
- 1h: commodity avg `0.1231` n `12`; crypto_alt avg `0.1285` n `233`; crypto_major avg `0.0483` n `8`; equity avg `-0.331` n `136`; fx avg `0.0092` n `6`; index avg `-0.0146` n `27`; metal avg `-0.0539` n `20`; unknown avg `-0.0382` n `768`
- 4h: commodity avg `0.5245` n `12`; crypto_alt avg `-1.6422` n `233`; crypto_major avg `-1.2177` n `8`; equity avg `-0.9761` n `136`; fx avg `0.0209` n `6`; index avg `-0.2082` n `27`; metal avg `-0.1072` n `20`; unknown avg `12.6934` n `768`
- 24h: commodity avg `0.8268` n `12`; crypto_alt avg `-1.86` n `233`; crypto_major avg `-1.7139` n `8`; equity avg `-2.0248` n `136`; fx avg `0.0659` n `6`; index avg `-0.4236` n `26`; metal avg `-0.1742` n `20`; unknown avg `1.464` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
