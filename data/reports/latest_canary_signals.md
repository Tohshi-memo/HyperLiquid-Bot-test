# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T06:37:24.604214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.0268` n `231`; crypto_major avg `0.0419` n `8`; equity avg `-0.0005` n `127`; fx avg `0.0113` n `6`; index avg `-0.0183` n `26`; metal avg `0.0485` n `20`; unknown avg `0.0286` n `792`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.2558` n `231`; crypto_major avg `0.1931` n `8`; equity avg `0.0511` n `127`; fx avg `-0.0328` n `6`; index avg `-0.0037` n `26`; metal avg `0.1712` n `20`; unknown avg `-0.0068` n `760`
- 4h: commodity avg `-0.0243` n `12`; crypto_alt avg `0.0665` n `231`; crypto_major avg `-0.1121` n `8`; equity avg `-0.4174` n `127`; fx avg `-0.0786` n `6`; index avg `-0.0716` n `26`; metal avg `0.166` n `20`; unknown avg `-0.0886` n `760`
- 24h: commodity avg `0.3811` n `12`; crypto_alt avg `0.7348` n `231`; crypto_major avg `1.8131` n `8`; equity avg `-0.2545` n `127`; fx avg `-0.0797` n `6`; index avg `0.0348` n `26`; metal avg `0.2158` n `20`; unknown avg `0.4491` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
