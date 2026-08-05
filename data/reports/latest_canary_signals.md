# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T22:22:26.204762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.0127` n `230`; crypto_major avg `-0.02` n `8`; equity avg `0.1076` n `108`; fx avg `0.0038` n `6`; index avg `0.0275` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0243` n `782`
- 1h: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.0425` n `230`; crypto_major avg `-0.1654` n `8`; equity avg `0.1332` n `108`; fx avg `-0.0021` n `6`; index avg `0.0275` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.0499` n `782`
- 4h: commodity avg `-0.0897` n `12`; crypto_alt avg `-0.225` n `230`; crypto_major avg `-0.6066` n `8`; equity avg `-0.9687` n `108`; fx avg `0.0005` n `6`; index avg `-0.083` n `25`; metal avg `-0.0997` n `20`; unknown avg `0.0552` n `782`
- 24h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.4478` n `230`; crypto_major avg `0.5631` n `8`; equity avg `-0.7956` n `108`; fx avg `-0.0435` n `6`; index avg `-0.1018` n `25`; metal avg `0.7779` n `20`; unknown avg `0.7286` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
