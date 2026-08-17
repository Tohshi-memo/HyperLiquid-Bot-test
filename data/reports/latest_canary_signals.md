# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T07:07:27.187329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0744` n `230`; crypto_major avg `-0.0481` n `8`; equity avg `-0.016` n `114`; fx avg `-0.0082` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0418` n `20`; unknown avg `0.0065` n `792`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `0.1864` n `230`; crypto_major avg `0.2657` n `8`; equity avg `0.096` n `114`; fx avg `-0.0168` n `6`; index avg `0.0129` n `25`; metal avg `-0.04` n `20`; unknown avg `0.7122` n `792`
- 4h: commodity avg `-0.1124` n `12`; crypto_alt avg `0.1876` n `230`; crypto_major avg `0.2868` n `8`; equity avg `0.5737` n `114`; fx avg `0.0095` n `6`; index avg `0.0992` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0448` n `776`
- 24h: commodity avg `-0.2257` n `12`; crypto_alt avg `0.5489` n `230`; crypto_major avg `1.0089` n `8`; equity avg `1.1135` n `114`; fx avg `-0.0276` n `6`; index avg `0.1457` n `25`; metal avg `0.2313` n `20`; unknown avg `0.1395` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
