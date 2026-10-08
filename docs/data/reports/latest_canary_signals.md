# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T09:52:28.511239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0945` n `13`; crypto_alt avg `0.0853` n `235`; crypto_major avg `-0.0406` n `8`; equity avg `-0.0641` n `150`; fx avg `-0.0069` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0316` n `20`; unknown avg `-0.1015` n `1077`
- 1h: commodity avg `0.0349` n `13`; crypto_alt avg `0.812` n `235`; crypto_major avg `0.2962` n `8`; equity avg `0.0641` n `150`; fx avg `0.0067` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0887` n `20`; unknown avg `0.1095` n `1075`
- 4h: commodity avg `0.4419` n `13`; crypto_alt avg `1.1316` n `235`; crypto_major avg `0.358` n `8`; equity avg `-0.4968` n `150`; fx avg `0.0357` n `6`; index avg `-0.1312` n `26`; metal avg `-0.1039` n `20`; unknown avg `1.1002` n `1031`
- 24h: commodity avg `0.7727` n `13`; crypto_alt avg `0.9043` n `235`; crypto_major avg `-1.35` n `8`; equity avg `-1.3333` n `150`; fx avg `0.003` n `6`; index avg `-0.2644` n `26`; metal avg `-0.084` n `20`; unknown avg `416.5022` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
