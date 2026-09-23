# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T08:22:28.546604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0789` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.7336` n `234`; crypto_major avg `0.3381` n `8`; equity avg `0.1235` n `140`; fx avg `-0.0178` n `6`; index avg `0.0084` n `26`; metal avg `0.012` n `20`; unknown avg `0.2432` n `945`
- 1h: commodity avg `0.051` n `12`; crypto_alt avg `-0.2243` n `234`; crypto_major avg `-0.3436` n `8`; equity avg `0.0537` n `140`; fx avg `0.0033` n `6`; index avg `-0.0102` n `26`; metal avg `-0.046` n `20`; unknown avg `0.157` n `937`
- 4h: commodity avg `0.228` n `12`; crypto_alt avg `0.0042` n `234`; crypto_major avg `-1.0912` n `8`; equity avg `-0.0486` n `140`; fx avg `0.1332` n `6`; index avg `-0.0123` n `26`; metal avg `-0.2499` n `20`; unknown avg `0.4843` n `921`
- 24h: commodity avg `0.0629` n `12`; crypto_alt avg `3.7842` n `234`; crypto_major avg `1.7908` n `8`; equity avg `1.7699` n `140`; fx avg `-0.0657` n `6`; index avg `0.2086` n `26`; metal avg `0.1939` n `20`; unknown avg `1.838` n `840`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
