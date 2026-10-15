# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T03:37:27.076646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.0505` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5717` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.046` n `13`; crypto_alt avg `-0.4314` n `236`; crypto_major avg `-0.2098` n `8`; equity avg `0.0281` n `151`; fx avg `-0.0187` n `6`; index avg `0.0095` n `26`; metal avg `-0.0112` n `20`; unknown avg `-0.322` n `1136`
- 1h: commodity avg `0.0228` n `13`; crypto_alt avg `-0.4439` n `236`; crypto_major avg `-0.5661` n `8`; equity avg `-0.128` n `151`; fx avg `-0.0156` n `6`; index avg `-0.0276` n `26`; metal avg `0.0361` n `20`; unknown avg `-0.5843` n `1134`
- 4h: commodity avg `-0.1958` n `13`; crypto_alt avg `-3.2587` n `236`; crypto_major avg `-1.8362` n `8`; equity avg `-0.5179` n `151`; fx avg `0.1497` n `6`; index avg `-0.2645` n `26`; metal avg `0.2143` n `20`; unknown avg `-0.0758` n `1128`
- 24h: commodity avg `-0.389` n `13`; crypto_alt avg `-6.0371` n `236`; crypto_major avg `-4.4738` n `8`; equity avg `-6.2421` n `151`; fx avg `0.075` n `6`; index avg `-1.0717` n `26`; metal avg `-0.7154` n `20`; unknown avg `1392.6569` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1432`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1365`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1069`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0837`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0803`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0648`, n `666`, weak_sample_signal
