# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T22:07:26.437446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `0.0195` n `8`; equity avg `-0.0111` n `94`; fx avg `-0.0072` n `6`; index avg `0.0087` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0068` n `768`
- 1h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.1134` n `230`; crypto_major avg `0.0571` n `8`; equity avg `0.0955` n `94`; fx avg `-0.006` n `6`; index avg `0.0249` n `25`; metal avg `0.0215` n `20`; unknown avg `0.0185` n `768`
- 4h: commodity avg `0.2321` n `12`; crypto_alt avg `0.1307` n `230`; crypto_major avg `0.1254` n `8`; equity avg `-0.0611` n `94`; fx avg `-0.0107` n `6`; index avg `0.028` n `25`; metal avg `-0.0714` n `20`; unknown avg `-0.2174` n `768`
- 24h: commodity avg `-0.1853` n `12`; crypto_alt avg `-0.8104` n `230`; crypto_major avg `-1.8968` n `8`; equity avg `-3.7314` n `94`; fx avg `-0.1723` n `6`; index avg `-0.5094` n `25`; metal avg `-0.8439` n `20`; unknown avg `-0.3952` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
