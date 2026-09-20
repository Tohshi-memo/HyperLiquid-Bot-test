# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T15:07:30.094536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.3548` n `234`; crypto_major avg `0.308` n `8`; equity avg `0.0494` n `140`; fx avg `0.0061` n `6`; index avg `0.0001` n `26`; metal avg `0.0021` n `20`; unknown avg `4.1434` n `941`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.239` n `234`; crypto_major avg `0.2242` n `8`; equity avg `0.0181` n `140`; fx avg `0.0308` n `6`; index avg `0.0072` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.4769` n `941`
- 4h: commodity avg `0.0153` n `12`; crypto_alt avg `0.425` n `234`; crypto_major avg `0.5946` n `8`; equity avg `0.0711` n `140`; fx avg `-0.0075` n `6`; index avg `0.0232` n `26`; metal avg `-0.0012` n `20`; unknown avg `2.5963` n `935`
- 24h: commodity avg `0.3253` n `12`; crypto_alt avg `-2.0817` n `234`; crypto_major avg `-2.2259` n `8`; equity avg `-0.2517` n `140`; fx avg `-0.0336` n `6`; index avg `-0.0479` n `26`; metal avg `-0.0427` n `20`; unknown avg `178.0039` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
