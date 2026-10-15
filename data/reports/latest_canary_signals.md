# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T01:37:30.030585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0792` n `13`; crypto_alt avg `0.349` n `236`; crypto_major avg `0.2139` n `8`; equity avg `0.1477` n `151`; fx avg `0.0318` n `6`; index avg `0.0218` n `26`; metal avg `-0.0168` n `20`; unknown avg `0.8517` n `1136`
- 1h: commodity avg `-0.0957` n `13`; crypto_alt avg `-0.2849` n `236`; crypto_major avg `-0.1114` n `8`; equity avg `-0.2722` n `151`; fx avg `0.0957` n `6`; index avg `-0.0812` n `26`; metal avg `0.0781` n `20`; unknown avg `1.8848` n `1134`
- 4h: commodity avg `-0.2138` n `13`; crypto_alt avg `-0.5306` n `236`; crypto_major avg `-0.2924` n `8`; equity avg `-1.1426` n `151`; fx avg `0.2464` n `6`; index avg `-0.3442` n `26`; metal avg `0.2583` n `20`; unknown avg `0.6563` n `1048`
- 24h: commodity avg `-0.4575` n `13`; crypto_alt avg `-2.5851` n `236`; crypto_major avg `-2.0912` n `8`; equity avg `-5.5168` n `151`; fx avg `0.0803` n `6`; index avg `-0.913` n `26`; metal avg `-0.4635` n `20`; unknown avg `1393.7559` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1125`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
