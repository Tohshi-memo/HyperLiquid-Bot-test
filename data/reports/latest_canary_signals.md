# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T00:37:26.274685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0551` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `-0.0416` n `8`; equity avg `-0.1812` n `108`; fx avg `-0.0199` n `6`; index avg `-0.0406` n `25`; metal avg `0.0373` n `20`; unknown avg `-0.172` n `782`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1481` n `230`; crypto_major avg `0.0767` n `8`; equity avg `-0.3431` n `108`; fx avg `-0.018` n `6`; index avg `-0.1048` n `25`; metal avg `0.1035` n `20`; unknown avg `-0.2415` n `782`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0366` n `230`; crypto_major avg `-0.36` n `8`; equity avg `-0.4635` n `108`; fx avg `-0.0109` n `6`; index avg `-0.1102` n `25`; metal avg `0.2055` n `20`; unknown avg `0.0561` n `782`
- 24h: commodity avg `-0.0999` n `12`; crypto_alt avg `0.7286` n `230`; crypto_major avg `0.7663` n `8`; equity avg `-1.731` n `108`; fx avg `-0.0216` n `6`; index avg `-0.3205` n `25`; metal avg `0.9607` n `20`; unknown avg `1.0866` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
