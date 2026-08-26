# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T13:52:30.665122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0788` n `12`; crypto_alt avg `-0.3617` n `231`; crypto_major avg `-0.3356` n `8`; equity avg `0.0624` n `122`; fx avg `0.0006` n `6`; index avg `0.0143` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.1183` n `797`
- 1h: commodity avg `0.2864` n `12`; crypto_alt avg `-0.8103` n `231`; crypto_major avg `-0.6092` n `8`; equity avg `0.5944` n `122`; fx avg `0.0049` n `6`; index avg `0.0909` n `25`; metal avg `-0.0399` n `20`; unknown avg `-0.1984` n `797`
- 4h: commodity avg `0.3726` n `12`; crypto_alt avg `-0.3793` n `231`; crypto_major avg `-0.3085` n `8`; equity avg `0.1086` n `122`; fx avg `-0.0044` n `6`; index avg `0.0471` n `25`; metal avg `-0.0752` n `20`; unknown avg `-0.1008` n `797`
- 24h: commodity avg `0.1805` n `12`; crypto_alt avg `-0.7398` n `231`; crypto_major avg `-0.3676` n `8`; equity avg `0.1676` n `122`; fx avg `-0.0528` n `6`; index avg `0.0163` n `25`; metal avg `0.2445` n `20`; unknown avg `0.6651` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
