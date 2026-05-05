# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T16:00:38.598646+00:00`
- Correlation status: `ready`
- Asset price records: `372`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0982` n `7`; crypto_alt avg `-0.1236` n `223`; crypto_major avg `-0.1355` n `7`; equity avg `-0.1439` n `47`; fx avg `-0.01` n `4`; index avg `0.038` n `6`; metal avg `-0.1824` n `7`; unknown avg `-0.0053` n `313`
- 1h: commodity avg `-0.2432` n `7`; crypto_alt avg `-0.3496` n `223`; crypto_major avg `0.0824` n `7`; equity avg `0.0723` n `47`; fx avg `-0.1528` n `4`; index avg `0.2591` n `6`; metal avg `-0.334` n `7`; unknown avg `-0.024` n `313`
- 4h: commodity avg `-0.6568` n `7`; crypto_alt avg `-0.268` n `223`; crypto_major avg `0.3282` n `7`; equity avg `0.5007` n `47`; fx avg `-0.1208` n `4`; index avg `0.7831` n `6`; metal avg `-0.3369` n `7`; unknown avg `0.2435` n `312`
- 24h: commodity avg `-1.226` n `7`; crypto_alt avg `1.6872` n `223`; crypto_major avg `2.2766` n `7`; equity avg `1.2707` n `47`; fx avg `-0.0652` n `4`; index avg `1.0835` n `6`; metal avg `0.9427` n `7`; unknown avg `0.9521` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `368`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2009`, n `368`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `368`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `368`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1058`, n `364`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `368`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `368`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.103`, n `368`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0976`, n `364`, weak_sample_signal
