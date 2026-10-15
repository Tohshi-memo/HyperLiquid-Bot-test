# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T07:37:28.042698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0249` n `13`; crypto_alt avg `0.0008` n `236`; crypto_major avg `0.1368` n `8`; equity avg `0.0348` n `151`; fx avg `0.0171` n `6`; index avg `0.0289` n `26`; metal avg `0.0216` n `20`; unknown avg `0.9441` n `1136`
- 1h: commodity avg `-0.0292` n `13`; crypto_alt avg `-0.1465` n `236`; crypto_major avg `0.1076` n `8`; equity avg `-0.1973` n `151`; fx avg `0.0361` n `6`; index avg `0.0212` n `26`; metal avg `0.1217` n `20`; unknown avg `1.4146` n `1134`
- 4h: commodity avg `-0.0803` n `13`; crypto_alt avg `-0.0739` n `236`; crypto_major avg `0.4949` n `8`; equity avg `-0.3086` n `151`; fx avg `-0.0371` n `6`; index avg `0.0449` n `26`; metal avg `0.0439` n `20`; unknown avg `2.669` n `1102`
- 24h: commodity avg `-0.4374` n `13`; crypto_alt avg `-5.3772` n `236`; crypto_major avg `-3.525` n `8`; equity avg `-5.9343` n `151`; fx avg `0.0635` n `6`; index avg `-0.9351` n `26`; metal avg `-0.5259` n `20`; unknown avg `1394.6536` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1133`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0901`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0678`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
