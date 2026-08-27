# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T22:52:34.377936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.0227` n `231`; crypto_major avg `0.0227` n `8`; equity avg `-0.0101` n `127`; fx avg `-0.0026` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0126` n `20`; unknown avg `-0.0672` n `792`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `0.2509` n `231`; crypto_major avg `0.3763` n `8`; equity avg `-0.0007` n `127`; fx avg `0.0121` n `6`; index avg `-0.0187` n `26`; metal avg `0.0479` n `20`; unknown avg `-0.0357` n `792`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.3` n `231`; crypto_major avg `0.3269` n `8`; equity avg `-0.036` n `127`; fx avg `0.0038` n `6`; index avg `0.0688` n `26`; metal avg `0.044` n `20`; unknown avg `-0.1209` n `792`
- 24h: commodity avg `0.3614` n `12`; crypto_alt avg `1.6547` n `231`; crypto_major avg `2.983` n `8`; equity avg `-0.2784` n `127`; fx avg `-0.0199` n `6`; index avg `-0.1284` n `26`; metal avg `0.1345` n `20`; unknown avg `0.986` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
