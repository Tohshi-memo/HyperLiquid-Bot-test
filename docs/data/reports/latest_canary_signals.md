# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T06:07:27.434282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `13`; crypto_alt avg `-0.2771` n `235`; crypto_major avg `-0.2284` n `8`; equity avg `-0.1535` n `151`; fx avg `-0.0029` n `6`; index avg `-0.0344` n `26`; metal avg `-0.025` n `20`; unknown avg `0.0051` n `1111`
- 1h: commodity avg `0.1306` n `13`; crypto_alt avg `-0.5643` n `235`; crypto_major avg `-0.4178` n `8`; equity avg `-0.296` n `151`; fx avg `-0.0` n `6`; index avg `-0.0609` n `26`; metal avg `-0.0316` n `20`; unknown avg `0.0549` n `1103`
- 4h: commodity avg `0.1563` n `13`; crypto_alt avg `0.6803` n `235`; crypto_major avg `0.4659` n `8`; equity avg `-0.8329` n `151`; fx avg `-0.0166` n `6`; index avg `-0.0878` n `26`; metal avg `-0.1255` n `20`; unknown avg `0.2623` n `1023`
- 24h: commodity avg `-0.3204` n `13`; crypto_alt avg `2.9135` n `235`; crypto_major avg `1.7439` n `8`; equity avg `-0.4657` n `151`; fx avg `-0.0465` n `6`; index avg `-0.0501` n `26`; metal avg `0.0699` n `20`; unknown avg `0.5212` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
