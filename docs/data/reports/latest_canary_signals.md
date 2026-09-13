# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T15:37:29.533135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.1441` n `233`; crypto_major avg `0.0536` n `8`; equity avg `-0.0149` n `136`; fx avg `0.0022` n `6`; index avg `-0.0142` n `27`; metal avg `0.0034` n `20`; unknown avg `0.5441` n `838`
- 1h: commodity avg `0.1245` n `12`; crypto_alt avg `-0.5896` n `233`; crypto_major avg `-0.1953` n `8`; equity avg `-0.1226` n `136`; fx avg `0.0023` n `6`; index avg `-0.0329` n `27`; metal avg `-0.0194` n `20`; unknown avg `22.8412` n `836`
- 4h: commodity avg `0.0238` n `12`; crypto_alt avg `0.1469` n `233`; crypto_major avg `0.3707` n `8`; equity avg `0.0577` n `136`; fx avg `0.0104` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0009` n `20`; unknown avg `2.6162` n `826`
- 24h: commodity avg `0.3153` n `12`; crypto_alt avg `-0.7693` n `233`; crypto_major avg `-1.5334` n `8`; equity avg `-1.6981` n `136`; fx avg `0.0104` n `6`; index avg `-0.2903` n `26`; metal avg `-0.0814` n `20`; unknown avg `2.0922` n `708`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
