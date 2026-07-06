# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T03:52:31.926571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.1138` n `229`; crypto_major avg `-0.1638` n `8`; equity avg `-0.1599` n `88`; fx avg `0.0067` n `6`; index avg `-0.0554` n `25`; metal avg `-0.0753` n `20`; unknown avg `4.2905` n `765`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.1534` n `229`; crypto_major avg `-0.3337` n `8`; equity avg `0.4142` n `88`; fx avg `-0.0045` n `6`; index avg `0.0473` n `25`; metal avg `-0.1192` n `20`; unknown avg `-0.1138` n `763`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.5829` n `229`; crypto_major avg `-0.6131` n `8`; equity avg `-1.1029` n `88`; fx avg `0.0511` n `6`; index avg `-0.2602` n `25`; metal avg `-0.3471` n `20`; unknown avg `-0.1173` n `763`
- 24h: commodity avg `-0.2497` n `12`; crypto_alt avg `0.5089` n `229`; crypto_major avg `1.2846` n `8`; equity avg `-0.8429` n `88`; fx avg `0.0758` n `6`; index avg `-0.1339` n `25`; metal avg `-0.2317` n `20`; unknown avg `1.1342` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
