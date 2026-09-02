# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T00:52:26.676627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `-0.2149` n `232`; crypto_major avg `-0.1186` n `8`; equity avg `-0.1311` n `132`; fx avg `-0.0097` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0419` n `20`; unknown avg `-0.1498` n `792`
- 1h: commodity avg `0.2148` n `12`; crypto_alt avg `-0.3149` n `232`; crypto_major avg `-0.2635` n `8`; equity avg `0.077` n `132`; fx avg `-0.0448` n `6`; index avg `0.0097` n `26`; metal avg `-0.0925` n `20`; unknown avg `2.5833` n `790`
- 4h: commodity avg `0.2284` n `12`; crypto_alt avg `-0.0992` n `232`; crypto_major avg `-0.0978` n `8`; equity avg `-0.1436` n `132`; fx avg `-0.0607` n `6`; index avg `0.0059` n `26`; metal avg `-0.0638` n `20`; unknown avg `0.2037` n `784`
- 24h: commodity avg `1.0324` n `12`; crypto_alt avg `-1.198` n `232`; crypto_major avg `-2.0537` n `8`; equity avg `-2.0529` n `130`; fx avg `-0.042` n `6`; index avg `-0.3497` n `26`; metal avg `-1.0836` n `20`; unknown avg `0.1606` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0311`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0309`, n `668`, weak_sample_signal
