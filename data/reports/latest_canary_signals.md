# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T05:52:29.940970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0436` n `12`; crypto_alt avg `-0.1547` n `228`; crypto_major avg `-0.2096` n `8`; equity avg `-0.114` n `88`; fx avg `0.0015` n `6`; index avg `-0.0275` n `25`; metal avg `0.0234` n `20`; unknown avg `2.4228` n `763`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `-0.3234` n `228`; crypto_major avg `-0.479` n `8`; equity avg `-0.1915` n `88`; fx avg `0.0181` n `6`; index avg `-0.0618` n `25`; metal avg `-0.0657` n `20`; unknown avg `1.5866` n `763`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `0.2577` n `228`; crypto_major avg `0.3488` n `8`; equity avg `-0.7386` n `88`; fx avg `-0.0104` n `6`; index avg `-0.226` n `25`; metal avg `0.0262` n `20`; unknown avg `-0.0912` n `761`
- 24h: commodity avg `-0.5395` n `12`; crypto_alt avg `1.4325` n `228`; crypto_major avg `0.8781` n `8`; equity avg `-1.7751` n `88`; fx avg `0.0465` n `6`; index avg `-0.4608` n `25`; metal avg `1.0336` n `20`; unknown avg `25.3358` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
