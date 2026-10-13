# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T21:07:30.398176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `13`; crypto_alt avg `0.0177` n `235`; crypto_major avg `0.0277` n `8`; equity avg `0.0002` n `151`; fx avg `-0.0164` n `6`; index avg `0.0034` n `26`; metal avg `0.0211` n `20`; unknown avg `-0.5239` n `1127`
- 1h: commodity avg `-0.0187` n `13`; crypto_alt avg `-0.0591` n `235`; crypto_major avg `-0.0441` n `8`; equity avg `-0.0414` n `151`; fx avg `-0.0119` n `6`; index avg `-0.0031` n `26`; metal avg `0.0024` n `20`; unknown avg `0.1709` n `1089`
- 4h: commodity avg `0.1937` n `13`; crypto_alt avg `0.5341` n `235`; crypto_major avg `0.1778` n `8`; equity avg `0.4309` n `151`; fx avg `0.0033` n `6`; index avg `0.0422` n `26`; metal avg `0.0317` n `20`; unknown avg `1.9338` n `1075`
- 24h: commodity avg `0.8938` n `13`; crypto_alt avg `-1.1257` n `235`; crypto_major avg `-0.3297` n `8`; equity avg `-0.6756` n `151`; fx avg `0.1548` n `6`; index avg `-0.1293` n `26`; metal avg `-0.2798` n `20`; unknown avg `14.587` n `1019`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1577`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `666`, weak_sample_signal
