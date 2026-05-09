# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T16:37:16.461751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0317` n `12`; crypto_alt avg `-0.2169` n `228`; crypto_major avg `-0.1834` n `8`; equity avg `-0.029` n `65`; fx avg `0.0` n `5`; index avg `-0.0024` n `23`; metal avg `-0.0084` n `18`; unknown avg `-0.09` n `376`
- 1h: commodity avg `0.0777` n `12`; crypto_alt avg `0.1654` n `228`; crypto_major avg `0.0458` n `8`; equity avg `-0.0041` n `65`; fx avg `-0.0068` n `5`; index avg `0.0282` n `23`; metal avg `0.0268` n `18`; unknown avg `-0.4002` n `376`
- 4h: commodity avg `0.4176` n `12`; crypto_alt avg `-0.724` n `228`; crypto_major avg `-0.3091` n `8`; equity avg `-0.0064` n `65`; fx avg `-0.0138` n `5`; index avg `0.0786` n `23`; metal avg `-0.0655` n `18`; unknown avg `-0.3484` n `376`
- 24h: commodity avg `-0.2867` n `12`; crypto_alt avg `1.0875` n `228`; crypto_major avg `1.3035` n `8`; equity avg `1.8153` n `65`; fx avg `0.014` n `5`; index avg `0.6349` n `23`; metal avg `0.0343` n `18`; unknown avg `0.0997` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
