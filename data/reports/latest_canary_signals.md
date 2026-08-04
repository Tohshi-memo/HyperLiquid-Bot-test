# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T03:22:27.178588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.2309` n `230`; crypto_major avg `-0.1628` n `8`; equity avg `-0.0613` n `107`; fx avg `-0.0061` n `6`; index avg `-0.0123` n `25`; metal avg `0.0274` n `20`; unknown avg `0.605` n `781`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.1196` n `230`; crypto_major avg `-0.1014` n `8`; equity avg `-0.0492` n `107`; fx avg `0.0454` n `6`; index avg `-0.0308` n `25`; metal avg `0.079` n `20`; unknown avg `0.0767` n `780`
- 4h: commodity avg `0.2428` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.1256` n `8`; equity avg `-0.4677` n `107`; fx avg `0.0106` n `6`; index avg `-0.1015` n `25`; metal avg `0.1995` n `20`; unknown avg `-0.3395` n `780`
- 24h: commodity avg `0.2651` n `12`; crypto_alt avg `1.0093` n `230`; crypto_major avg `0.8924` n `8`; equity avg `1.4279` n `107`; fx avg `-0.0014` n `6`; index avg `0.0927` n `25`; metal avg `0.0362` n `20`; unknown avg `0.2078` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
