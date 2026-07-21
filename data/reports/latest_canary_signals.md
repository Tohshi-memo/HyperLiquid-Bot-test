# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T09:37:24.762847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1578` n `12`; crypto_alt avg `0.0873` n `230`; crypto_major avg `0.1799` n `8`; equity avg `-0.0561` n `98`; fx avg `0.002` n `6`; index avg `-0.0276` n `25`; metal avg `-0.0355` n `20`; unknown avg `0.0057` n `771`
- 1h: commodity avg `0.267` n `12`; crypto_alt avg `-0.0502` n `230`; crypto_major avg `0.0498` n `8`; equity avg `0.0239` n `98`; fx avg `-0.0183` n `6`; index avg `0.0016` n `25`; metal avg `0.0116` n `20`; unknown avg `0.0368` n `771`
- 4h: commodity avg `0.2115` n `12`; crypto_alt avg `0.0867` n `230`; crypto_major avg `0.5417` n `8`; equity avg `0.8708` n `98`; fx avg `0.0501` n `6`; index avg `0.0812` n `25`; metal avg `0.2355` n `20`; unknown avg `0.0226` n `755`
- 24h: commodity avg `0.5017` n `12`; crypto_alt avg `2.3245` n `230`; crypto_major avg `2.8039` n `8`; equity avg `1.8768` n `98`; fx avg `-0.0734` n `6`; index avg `0.2683` n `25`; metal avg `0.6209` n `20`; unknown avg `0.1591` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.076`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
