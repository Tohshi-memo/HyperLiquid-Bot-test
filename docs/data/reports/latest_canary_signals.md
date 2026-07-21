# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T08:07:27.357093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1161` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.1994` n `98`; fx avg `0.0255` n `6`; index avg `0.0146` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0168` n `771`
- 1h: commodity avg `-0.2027` n `12`; crypto_alt avg `-0.1062` n `230`; crypto_major avg `0.0754` n `8`; equity avg `0.1627` n `98`; fx avg `0.0137` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0294` n `20`; unknown avg `-0.044` n `771`
- 4h: commodity avg `-0.0527` n `12`; crypto_alt avg `0.2259` n `230`; crypto_major avg `0.35` n `8`; equity avg `0.5635` n `98`; fx avg `0.0695` n `6`; index avg `0.0105` n `25`; metal avg `0.3297` n `20`; unknown avg `0.0465` n `755`
- 24h: commodity avg `-0.0149` n `12`; crypto_alt avg `2.4987` n `230`; crypto_major avg `2.7721` n `8`; equity avg `1.782` n `98`; fx avg `-0.0838` n `6`; index avg `0.2953` n `25`; metal avg `0.597` n `20`; unknown avg `0.1883` n `753`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
