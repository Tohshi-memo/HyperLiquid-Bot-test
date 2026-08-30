# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T12:07:23.522347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.3422` n `231`; crypto_major avg `0.2861` n `8`; equity avg `0.0048` n `128`; fx avg `0.0` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0187` n `20`; unknown avg `1.5001` n `793`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `0.3863` n `231`; crypto_major avg `0.1669` n `8`; equity avg `0.024` n `128`; fx avg `0.0048` n `6`; index avg `0.003` n `26`; metal avg `-0.0171` n `20`; unknown avg `1.3918` n `791`
- 4h: commodity avg `0.022` n `12`; crypto_alt avg `0.8594` n `231`; crypto_major avg `0.3313` n `8`; equity avg `0.0469` n `128`; fx avg `0.0022` n `6`; index avg `0.0056` n `26`; metal avg `-0.0231` n `20`; unknown avg `0.9972` n `789`
- 24h: commodity avg `-0.0133` n `12`; crypto_alt avg `1.9028` n `231`; crypto_major avg `1.2356` n `8`; equity avg `0.3023` n `128`; fx avg `0.0144` n `6`; index avg `0.0599` n `26`; metal avg `0.0742` n `20`; unknown avg `-0.0949` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
