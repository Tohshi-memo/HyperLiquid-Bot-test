# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T01:37:27.244394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.22` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0507` n `12`; crypto_alt avg `-0.4525` n `231`; crypto_major avg `-0.3506` n `8`; equity avg `-0.3668` n `122`; fx avg `0.008` n `6`; index avg `-0.0406` n `25`; metal avg `-0.0353` n `20`; unknown avg `0.6272` n `793`
- 1h: commodity avg `-0.1256` n `12`; crypto_alt avg `-0.9789` n `231`; crypto_major avg `-0.7882` n `8`; equity avg `-0.1279` n `122`; fx avg `0.0124` n `6`; index avg `0.0171` n `25`; metal avg `0.0046` n `20`; unknown avg `0.8476` n `793`
- 4h: commodity avg `-0.2844` n `12`; crypto_alt avg `-2.1808` n `231`; crypto_major avg `-1.2888` n `8`; equity avg `-0.6999` n `122`; fx avg `-0.005` n `6`; index avg `-0.0688` n `25`; metal avg `-0.0777` n `20`; unknown avg `0.8363` n `793`
- 24h: commodity avg `-0.4025` n `12`; crypto_alt avg `1.3966` n `231`; crypto_major avg `-0.6109` n `8`; equity avg `-0.0917` n `122`; fx avg `-0.1368` n `6`; index avg `0.0405` n `25`; metal avg `-0.0053` n `20`; unknown avg `6.2799` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
