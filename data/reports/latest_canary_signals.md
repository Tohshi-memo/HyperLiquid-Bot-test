# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T10:06:38.664672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `-0.0363` n `8`; equity avg `-0.081` n `98`; fx avg `-0.0082` n `6`; index avg `-0.009` n `25`; metal avg `-0.0359` n `20`; unknown avg `-0.0166` n `771`
- 1h: commodity avg `0.2413` n `12`; crypto_alt avg `0.1577` n `230`; crypto_major avg `0.2304` n `8`; equity avg `-0.1144` n `98`; fx avg `0.0066` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0547` n `20`; unknown avg `-0.0144` n `771`
- 4h: commodity avg `0.2367` n `12`; crypto_alt avg `0.054` n `230`; crypto_major avg `0.4582` n `8`; equity avg `0.4732` n `98`; fx avg `0.0414` n `6`; index avg `0.0442` n `25`; metal avg `0.1472` n `20`; unknown avg `0.0467` n `771`
- 24h: commodity avg `0.4167` n `12`; crypto_alt avg `2.3748` n `230`; crypto_major avg `2.8514` n `8`; equity avg `1.7112` n `98`; fx avg `-0.0764` n `6`; index avg `0.2581` n `25`; metal avg `0.571` n `20`; unknown avg `0.2554` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0851`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
