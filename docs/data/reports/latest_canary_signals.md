# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T11:37:30.869728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.206` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0238` n `13`; crypto_alt avg `-0.0265` n `235`; crypto_major avg `-0.0933` n `8`; equity avg `0.078` n `150`; fx avg `-0.011` n `6`; index avg `0.0125` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.1701` n `1077`
- 1h: commodity avg `-0.0638` n `13`; crypto_alt avg `-0.4071` n `235`; crypto_major avg `-0.6076` n `8`; equity avg `0.0763` n `150`; fx avg `-0.0183` n `6`; index avg `0.0463` n `26`; metal avg `0.062` n `20`; unknown avg `0.3848` n `1075`
- 4h: commodity avg `0.1768` n `13`; crypto_alt avg `-0.7186` n `235`; crypto_major avg `-1.2581` n `8`; equity avg `-0.4315` n `150`; fx avg `0.0288` n `6`; index avg `-0.0521` n `26`; metal avg `-0.1096` n `20`; unknown avg `1.8803` n `1059`
- 24h: commodity avg `0.6722` n `13`; crypto_alt avg `0.316` n `235`; crypto_major avg `-1.987` n `8`; equity avg `-1.3691` n `150`; fx avg `0.0207` n `6`; index avg `-0.2193` n `26`; metal avg `-0.155` n `20`; unknown avg `416.5757` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
