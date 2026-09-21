# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T17:37:32.668267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0836` n `12`; crypto_alt avg `0.086` n `234`; crypto_major avg `0.3051` n `8`; equity avg `-0.0241` n `140`; fx avg `-0.0002` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0474` n `20`; unknown avg `0.011` n `942`
- 1h: commodity avg `0.1496` n `12`; crypto_alt avg `-0.2938` n `234`; crypto_major avg `0.5702` n `8`; equity avg `0.0189` n `140`; fx avg `-0.0054` n `6`; index avg `-0.0085` n `26`; metal avg `-0.1211` n `20`; unknown avg `0.297` n `940`
- 4h: commodity avg `-0.1354` n `12`; crypto_alt avg `-0.2087` n `234`; crypto_major avg `1.1677` n `8`; equity avg `0.89` n `140`; fx avg `-0.0196` n `6`; index avg `0.2293` n `26`; metal avg `-0.2544` n `20`; unknown avg `1.6047` n `870`
- 24h: commodity avg `-1.0082` n `12`; crypto_alt avg `3.6162` n `234`; crypto_major avg `5.2013` n `8`; equity avg `2.5613` n `140`; fx avg `-0.0857` n `6`; index avg `0.5737` n `26`; metal avg `-0.0673` n `20`; unknown avg `7.4646` n `739`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
