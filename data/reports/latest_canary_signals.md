# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T23:07:27.505918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0592` n `13`; crypto_alt avg `-0.3291` n `239`; crypto_major avg `-0.1984` n `8`; equity avg `-0.0261` n `160`; fx avg `0.0123` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0206` n `20`; unknown avg `0.007` n `1257`
- 1h: commodity avg `-0.0472` n `13`; crypto_alt avg `-0.0823` n `239`; crypto_major avg `0.2809` n `8`; equity avg `-0.1253` n `160`; fx avg `0.0127` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0292` n `20`; unknown avg `-0.1708` n `1253`
- 4h: commodity avg `-0.2841` n `13`; crypto_alt avg `-0.6311` n `239`; crypto_major avg `0.3338` n `8`; equity avg `0.5099` n `160`; fx avg `0.0123` n `6`; index avg `0.091` n `27`; metal avg `0.2373` n `20`; unknown avg `-0.3015` n `1205`
- 24h: commodity avg `-0.4635` n `13`; crypto_alt avg `1.3951` n `239`; crypto_major avg `-0.4503` n `8`; equity avg `4.7856` n `160`; fx avg `-0.0966` n `6`; index avg `0.5802` n `27`; metal avg `0.5778` n `20`; unknown avg `4.3411` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
