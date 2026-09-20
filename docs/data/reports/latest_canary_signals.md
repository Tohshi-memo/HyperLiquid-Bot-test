# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T14:07:26.373881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.3211` n `234`; crypto_major avg `0.2315` n `8`; equity avg `0.036` n `140`; fx avg `-0.0032` n `6`; index avg `-0.0028` n `26`; metal avg `0.003` n `20`; unknown avg `0.0725` n `941`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `-0.0536` n `234`; crypto_major avg `0.0885` n `8`; equity avg `0.0027` n `140`; fx avg `-0.0043` n `6`; index avg `-0.0038` n `26`; metal avg `0.0106` n `20`; unknown avg `1.0319` n `941`
- 4h: commodity avg `0.0476` n `12`; crypto_alt avg `0.4822` n `234`; crypto_major avg `0.4531` n `8`; equity avg `0.0652` n `140`; fx avg `-0.0079` n `6`; index avg `0.0033` n `26`; metal avg `-0.0203` n `20`; unknown avg `1.6578` n `935`
- 24h: commodity avg `0.2662` n `12`; crypto_alt avg `-2.1546` n `234`; crypto_major avg `-2.2215` n `8`; equity avg `-0.2845` n `140`; fx avg `-0.0577` n `6`; index avg `-0.0542` n `26`; metal avg `-0.0267` n `20`; unknown avg `1.3565` n `818`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
