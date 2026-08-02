# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T05:37:32.181658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `-0.0321` n `8`; equity avg `-0.0289` n `102`; fx avg `-0.0008` n `6`; index avg `-0.0072` n `25`; metal avg `0.0179` n `20`; unknown avg `0.1293` n `782`
- 1h: commodity avg `0.1152` n `12`; crypto_alt avg `0.0937` n `230`; crypto_major avg `0.0373` n `8`; equity avg `-0.0564` n `102`; fx avg `-0.0208` n `6`; index avg `0.0221` n `25`; metal avg `0.0179` n `20`; unknown avg `0.3345` n `782`
- 4h: commodity avg `-0.7653` n `12`; crypto_alt avg `0.6447` n `230`; crypto_major avg `0.8474` n `8`; equity avg `0.6862` n `102`; fx avg `-0.0674` n `6`; index avg `0.1832` n `25`; metal avg `0.1669` n `20`; unknown avg `0.8101` n `782`
- 24h: commodity avg `-1.0077` n `12`; crypto_alt avg `0.0674` n `230`; crypto_major avg `0.4073` n `8`; equity avg `0.881` n `102`; fx avg `-0.1311` n `6`; index avg `0.2582` n `25`; metal avg `0.2752` n `20`; unknown avg `0.3636` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
