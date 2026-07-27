# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T20:07:33.026333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.0822` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `0.1638` n `102`; fx avg `-0.0074` n `6`; index avg `0.0285` n `25`; metal avg `-0.031` n `20`; unknown avg `0.1449` n `774`
- 1h: commodity avg `-0.088` n `12`; crypto_alt avg `0.1376` n `230`; crypto_major avg `0.0821` n `8`; equity avg `0.1433` n `102`; fx avg `-0.0153` n `6`; index avg `0.0136` n `25`; metal avg `0.0288` n `20`; unknown avg `95.7553` n `774`
- 4h: commodity avg `-0.335` n `12`; crypto_alt avg `0.398` n `230`; crypto_major avg `0.5161` n `8`; equity avg `0.9069` n `102`; fx avg `-0.0409` n `6`; index avg `0.128` n `25`; metal avg `-0.0226` n `20`; unknown avg `95.929` n `774`
- 24h: commodity avg `-1.0782` n `12`; crypto_alt avg `-0.9376` n `230`; crypto_major avg `-0.266` n `8`; equity avg `-0.9475` n `102`; fx avg `-0.031` n `6`; index avg `-0.3208` n `25`; metal avg `0.2238` n `20`; unknown avg `97.7046` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
