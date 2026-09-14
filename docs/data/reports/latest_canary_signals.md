# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T04:52:29.545249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.557` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.0096` n `233`; crypto_major avg `0.041` n `8`; equity avg `0.041` n `136`; fx avg `-0.0155` n `6`; index avg `0.0027` n `27`; metal avg `-0.0135` n `20`; unknown avg `-0.0336` n `894`
- 1h: commodity avg `-0.1065` n `12`; crypto_alt avg `0.1116` n `233`; crypto_major avg `0.23` n `8`; equity avg `-0.0335` n `136`; fx avg `-0.0338` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0189` n `20`; unknown avg `-0.2463` n `886`
- 4h: commodity avg `-0.0678` n `12`; crypto_alt avg `1.2889` n `233`; crypto_major avg `1.4516` n `8`; equity avg `0.1607` n `136`; fx avg `-0.0236` n `6`; index avg `0.0105` n `27`; metal avg `-0.1054` n `20`; unknown avg `11.2839` n `762`
- 24h: commodity avg `0.6396` n `12`; crypto_alt avg `-0.4491` n `233`; crypto_major avg `0.1662` n `8`; equity avg `-1.3948` n `136`; fx avg `0.0138` n `6`; index avg `-0.3276` n `26`; metal avg `-0.1701` n `20`; unknown avg `1.8298` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
