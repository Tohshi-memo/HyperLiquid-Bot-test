# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T23:52:29.055084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.0126` n `230`; crypto_major avg `-0.1027` n `8`; equity avg `-0.0038` n `96`; fx avg `-0.0034` n `6`; index avg `0.0019` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0349` n `769`
- 1h: commodity avg `-0.0137` n `12`; crypto_alt avg `0.0518` n `230`; crypto_major avg `0.0224` n `8`; equity avg `-0.05` n `96`; fx avg `0.0037` n `6`; index avg `-0.0103` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.094` n `769`
- 4h: commodity avg `0.1709` n `12`; crypto_alt avg `-0.0404` n `230`; crypto_major avg `-0.2551` n `8`; equity avg `-0.4252` n `96`; fx avg `-0.0602` n `6`; index avg `-0.1075` n `25`; metal avg `0.0002` n `20`; unknown avg `0.0346` n `769`
- 24h: commodity avg `0.7225` n `12`; crypto_alt avg `-0.31` n `230`; crypto_major avg `-0.4424` n `8`; equity avg `-0.7709` n `94`; fx avg `0.0427` n `6`; index avg `-0.2644` n `25`; metal avg `0.0397` n `20`; unknown avg `0.1149` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
