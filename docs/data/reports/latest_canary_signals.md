# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T20:37:29.628979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `13`; crypto_alt avg `-0.1307` n `238`; crypto_major avg `-0.1174` n `8`; equity avg `-0.3846` n `155`; fx avg `0.0024` n `6`; index avg `-0.0706` n `27`; metal avg `-0.063` n `20`; unknown avg `2.1777` n `1168`
- 1h: commodity avg `-0.2349` n `13`; crypto_alt avg `0.1613` n `238`; crypto_major avg `0.0145` n `8`; equity avg `-0.7094` n `155`; fx avg `-0.0022` n `6`; index avg `-0.0648` n `27`; metal avg `0.0682` n `20`; unknown avg `4.6883` n `1130`
- 4h: commodity avg `-0.4822` n `13`; crypto_alt avg `1.1508` n `238`; crypto_major avg `0.88` n `8`; equity avg `-0.2027` n `155`; fx avg `-0.0263` n `6`; index avg `-0.0373` n `27`; metal avg `0.1089` n `20`; unknown avg `7.9283` n `1130`
- 24h: commodity avg `0.0936` n `13`; crypto_alt avg `0.9194` n `238`; crypto_major avg `0.7429` n `8`; equity avg `1.1055` n `154`; fx avg `0.2475` n `6`; index avg `0.2083` n `27`; metal avg `-0.0898` n `20`; unknown avg `26.5367` n `1068`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
