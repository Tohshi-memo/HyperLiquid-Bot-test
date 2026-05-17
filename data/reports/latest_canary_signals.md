# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T22:07:16.556460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.2434` n `228`; crypto_major avg `-0.1669` n `8`; equity avg `0.0312` n `65`; fx avg `0.0108` n `5`; index avg `0.0018` n `23`; metal avg `0.5152` n `18`; unknown avg `0.0226` n `384`
- 1h: commodity avg `0.0232` n `12`; crypto_alt avg `0.1223` n `228`; crypto_major avg `0.1135` n `8`; equity avg `0.1643` n `65`; fx avg `0.0087` n `5`; index avg `0.0957` n `23`; metal avg `0.5512` n `18`; unknown avg `0.1125` n `384`
- 4h: commodity avg `-0.0578` n `12`; crypto_alt avg `0.446` n `228`; crypto_major avg `1.0674` n `8`; equity avg `0.5011` n `65`; fx avg `-0.0191` n `5`; index avg `0.1849` n `23`; metal avg `0.4603` n `18`; unknown avg `0.0954` n `384`
- 24h: commodity avg `1.7217` n `12`; crypto_alt avg `-9.1113` n `228`; crypto_major avg `-1.2494` n `8`; equity avg `-2.119` n `65`; fx avg `-0.1731` n `5`; index avg `-1.424` n `23`; metal avg `-5.4607` n `18`; unknown avg `550.4998` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
