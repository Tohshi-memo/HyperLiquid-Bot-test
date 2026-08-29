# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T13:37:29.344244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0576` n `231`; crypto_major avg `0.0565` n `8`; equity avg `0.0043` n `127`; fx avg `-0.0014` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0421` n `793`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.22` n `231`; crypto_major avg `0.2113` n `8`; equity avg `0.0156` n `127`; fx avg `-0.0006` n `6`; index avg `-0.003` n `26`; metal avg `0.0155` n `20`; unknown avg `0.1339` n `793`
- 4h: commodity avg `0.0252` n `12`; crypto_alt avg `0.2656` n `231`; crypto_major avg `0.1898` n `8`; equity avg `-0.0067` n `127`; fx avg `-0.0186` n `6`; index avg `0.0029` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.0867` n `761`
- 24h: commodity avg `0.1015` n `12`; crypto_alt avg `-1.6005` n `231`; crypto_major avg `-1.8394` n `8`; equity avg `-1.1961` n `127`; fx avg `-0.072` n `6`; index avg `-0.1492` n `26`; metal avg `-0.8283` n `20`; unknown avg `-0.4627` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
