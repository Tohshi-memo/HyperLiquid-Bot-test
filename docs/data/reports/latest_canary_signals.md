# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T15:22:30.113825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0437` n `229`; crypto_major avg `0.0516` n `8`; equity avg `0.1848` n `91`; fx avg `-0.0122` n `6`; index avg `0.07` n `25`; metal avg `0.0162` n `20`; unknown avg `-0.0345` n `766`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1932` n `229`; crypto_major avg `0.1993` n `8`; equity avg `0.1131` n `91`; fx avg `-0.0021` n `6`; index avg `0.0496` n `25`; metal avg `-0.0532` n `20`; unknown avg `-0.0464` n `766`
- 4h: commodity avg `-0.3926` n `12`; crypto_alt avg `-0.424` n `229`; crypto_major avg `-0.813` n `8`; equity avg `-0.9812` n `91`; fx avg `-0.0652` n `6`; index avg `0.0162` n `25`; metal avg `0.0281` n `20`; unknown avg `-0.2116` n `766`
- 24h: commodity avg `-0.5483` n `12`; crypto_alt avg `0.5733` n `229`; crypto_major avg `0.7307` n `8`; equity avg `-1.0743` n `91`; fx avg `-0.1247` n `6`; index avg `0.0373` n `25`; metal avg `-0.2248` n `20`; unknown avg `-0.2655` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
