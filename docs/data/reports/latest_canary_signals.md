# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T16:15:02.997992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `13`; crypto_alt avg `-0.1911` n `235`; crypto_major avg `-0.1411` n `8`; equity avg `-0.0538` n `150`; fx avg `0.0008` n `6`; index avg `-0.009` n `26`; metal avg `-0.0296` n `20`; unknown avg `0.4849` n `1076`
- 1h: commodity avg `0.2432` n `13`; crypto_alt avg `-0.6855` n `235`; crypto_major avg `-0.6847` n `8`; equity avg `-0.3617` n `150`; fx avg `-0.0058` n `6`; index avg `-0.0523` n `26`; metal avg `0.0219` n `20`; unknown avg `1.1693` n `1068`
- 4h: commodity avg `0.5292` n `13`; crypto_alt avg `-0.4172` n `235`; crypto_major avg `-0.375` n `8`; equity avg `0.0059` n `150`; fx avg `-0.0327` n `6`; index avg `-0.0571` n `26`; metal avg `-0.0649` n `20`; unknown avg `5.577` n `1018`
- 24h: commodity avg `-0.2389` n `13`; crypto_alt avg `0.5794` n `235`; crypto_major avg `0.6255` n `8`; equity avg `0.7858` n `149`; fx avg `0.1175` n `6`; index avg `0.1266` n `26`; metal avg `0.0747` n `20`; unknown avg `381.6157` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
