# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T17:52:47.650746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0791` n `13`; crypto_alt avg `-0.0647` n `236`; crypto_major avg `-0.2288` n `8`; equity avg `-0.1879` n `151`; fx avg `-0.0188` n `6`; index avg `-0.0358` n `26`; metal avg `-0.0503` n `20`; unknown avg `0.7889` n `1136`
- 1h: commodity avg `0.083` n `13`; crypto_alt avg `-0.4157` n `236`; crypto_major avg `-0.4424` n `8`; equity avg `-0.5924` n `151`; fx avg `0.0027` n `6`; index avg `-0.0967` n `26`; metal avg `-0.0339` n `20`; unknown avg `-0.4095` n `1134`
- 4h: commodity avg `0.1027` n `13`; crypto_alt avg `-0.8803` n `236`; crypto_major avg `-1.294` n `8`; equity avg `-1.9257` n `151`; fx avg `-0.0379` n `6`; index avg `-0.3145` n `26`; metal avg `-0.2935` n `20`; unknown avg `0.3948` n `1101`
- 24h: commodity avg `0.111` n `13`; crypto_alt avg `-1.9504` n `236`; crypto_major avg `-1.8085` n `8`; equity avg `-3.559` n `151`; fx avg `-0.1529` n `6`; index avg `-0.4879` n `26`; metal avg `-0.7697` n `20`; unknown avg `1262.5119` n `980`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0572`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0571`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0536`, n `666`, weak_sample_signal
