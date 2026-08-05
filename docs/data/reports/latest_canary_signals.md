# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T16:52:32.015208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1876` n `12`; crypto_alt avg `-0.1428` n `230`; crypto_major avg `-0.1695` n `8`; equity avg `0.0165` n `108`; fx avg `-0.0125` n `6`; index avg `0.0107` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.0497` n `782`
- 1h: commodity avg `-0.1174` n `12`; crypto_alt avg `0.0858` n `230`; crypto_major avg `0.2432` n `8`; equity avg `0.2498` n `108`; fx avg `-0.0011` n `6`; index avg `0.0297` n `25`; metal avg `0.0488` n `20`; unknown avg `-0.064` n `782`
- 4h: commodity avg `-0.342` n `12`; crypto_alt avg `-0.0417` n `230`; crypto_major avg `0.2699` n `8`; equity avg `-0.0812` n `108`; fx avg `-0.0282` n `6`; index avg `-0.0641` n `25`; metal avg `0.2411` n `20`; unknown avg `-0.1062` n `782`
- 24h: commodity avg `-0.2086` n `12`; crypto_alt avg `0.7775` n `230`; crypto_major avg `0.8837` n `8`; equity avg `0.2281` n `108`; fx avg `-0.0008` n `6`; index avg `0.0805` n `25`; metal avg `0.6274` n `20`; unknown avg `0.7688` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
