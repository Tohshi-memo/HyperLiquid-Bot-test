# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T21:22:26.568620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0955` n `229`; crypto_major avg `-0.1305` n `8`; equity avg `0.026` n `91`; fx avg `-0.0039` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0062` n `20`; unknown avg `-0.0877` n `764`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `-0.4523` n `229`; crypto_major avg `-0.4113` n `8`; equity avg `0.0099` n `91`; fx avg `-0.0102` n `6`; index avg `0.01` n `25`; metal avg `-0.0209` n `20`; unknown avg `-0.1913` n `764`
- 4h: commodity avg `0.1587` n `12`; crypto_alt avg `-0.6654` n `229`; crypto_major avg `-0.5532` n `8`; equity avg `0.5226` n `91`; fx avg `-0.0248` n `6`; index avg `0.0197` n `25`; metal avg `0.0311` n `20`; unknown avg `0.9059` n `764`
- 24h: commodity avg `0.4012` n `12`; crypto_alt avg `-2.3057` n `229`; crypto_major avg `-2.6651` n `8`; equity avg `1.0045` n `91`; fx avg `0.0016` n `6`; index avg `-0.0472` n `25`; metal avg `-0.8088` n `20`; unknown avg `0.0492` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
