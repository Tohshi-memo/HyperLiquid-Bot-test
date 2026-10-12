# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T20:07:28.639098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0705` n `13`; crypto_alt avg `0.0827` n `235`; crypto_major avg `0.1765` n `8`; equity avg `0.0297` n `151`; fx avg `-0.0035` n `6`; index avg `0.0003` n `26`; metal avg `-0.0009` n `20`; unknown avg `5.7246` n `1106`
- 1h: commodity avg `-0.1156` n `13`; crypto_alt avg `0.3862` n `235`; crypto_major avg `0.534` n `8`; equity avg `0.1999` n `151`; fx avg `-0.0045` n `6`; index avg `0.0196` n `26`; metal avg `0.0215` n `20`; unknown avg `12.1745` n `1106`
- 4h: commodity avg `-0.1633` n `13`; crypto_alt avg `-0.4151` n `235`; crypto_major avg `-0.3383` n `8`; equity avg `-0.3996` n `151`; fx avg `-0.0103` n `6`; index avg `-0.0714` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.6484` n `1106`
- 24h: commodity avg `0.2742` n `13`; crypto_alt avg `-2.8026` n `235`; crypto_major avg `-1.4638` n `8`; equity avg `-3.3478` n `151`; fx avg `-0.1768` n `6`; index avg `-0.3374` n `26`; metal avg `-0.1778` n `20`; unknown avg `0.1822` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2048`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1738`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0962`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `666`, weak_sample_signal
