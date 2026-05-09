# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T01:07:17.629400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1169` n `12`; crypto_alt avg `0.0666` n `228`; crypto_major avg `0.1125` n `8`; equity avg `0.033` n `65`; fx avg `-0.0053` n `5`; index avg `0.1068` n `23`; metal avg `0.087` n `18`; unknown avg `-0.0335` n `375`
- 1h: commodity avg `-0.0553` n `12`; crypto_alt avg `0.6753` n `228`; crypto_major avg `0.3326` n `8`; equity avg `0.0762` n `65`; fx avg `-0.0157` n `5`; index avg `-0.1143` n `23`; metal avg `0.1407` n `18`; unknown avg `0.0473` n `375`
- 4h: commodity avg `-0.405` n `12`; crypto_alt avg `1.0322` n `228`; crypto_major avg `0.4936` n `8`; equity avg `0.3178` n `65`; fx avg `-0.0452` n `5`; index avg `0.1762` n `23`; metal avg `-0.1274` n `18`; unknown avg `-0.4515` n `375`
- 24h: commodity avg `-0.7295` n `12`; crypto_alt avg `4.204` n `228`; crypto_major avg `2.0818` n `8`; equity avg `3.6907` n `65`; fx avg `0.0964` n `5`; index avg `1.3184` n `23`; metal avg `0.2218` n `18`; unknown avg `1.0037` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
