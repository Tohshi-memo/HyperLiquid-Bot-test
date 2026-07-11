# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T17:22:28.198082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `0.0142` n `8`; equity avg `-0.0028` n `92`; fx avg `0.0194` n `6`; index avg `-0.0045` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.1981` n `765`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `0.1596` n `230`; crypto_major avg `0.0554` n `8`; equity avg `0.0777` n `92`; fx avg `0.0266` n `6`; index avg `-0.0008` n `25`; metal avg `0.0027` n `20`; unknown avg `0.171` n `765`
- 4h: commodity avg `-0.0409` n `12`; crypto_alt avg `0.1372` n `230`; crypto_major avg `0.2815` n `8`; equity avg `0.0903` n `92`; fx avg `-0.0029` n `6`; index avg `0.0155` n `25`; metal avg `-0.0194` n `20`; unknown avg `0.2604` n `765`
- 24h: commodity avg `0.06` n `12`; crypto_alt avg `0.7938` n `229`; crypto_major avg `0.6197` n `8`; equity avg `0.1357` n `92`; fx avg `-0.015` n `6`; index avg `0.0579` n `25`; metal avg `0.035` n `20`; unknown avg `2.3807` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
