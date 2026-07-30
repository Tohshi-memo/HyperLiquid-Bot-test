# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T11:22:29.129357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.0889` n `230`; crypto_major avg `0.0089` n `8`; equity avg `0.0059` n `102`; fx avg `-0.0023` n `6`; index avg `0.0002` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0153` n `779`
- 1h: commodity avg `-0.1282` n `12`; crypto_alt avg `-0.2068` n `230`; crypto_major avg `-0.1169` n `8`; equity avg `0.5462` n `102`; fx avg `-0.0289` n `6`; index avg `0.0637` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.0062` n `779`
- 4h: commodity avg `-0.34` n `12`; crypto_alt avg `-0.1313` n `230`; crypto_major avg `0.3723` n `8`; equity avg `1.6183` n `102`; fx avg `-0.0306` n `6`; index avg `0.2539` n `25`; metal avg `0.3757` n `20`; unknown avg `-0.0431` n `771`
- 24h: commodity avg `0.248` n `12`; crypto_alt avg `-0.2568` n `230`; crypto_major avg `-0.1306` n `8`; equity avg `-2.2839` n `102`; fx avg `-0.0779` n `6`; index avg `-0.4202` n `25`; metal avg `0.4562` n `20`; unknown avg `-0.1425` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
