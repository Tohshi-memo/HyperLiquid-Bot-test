# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T00:22:26.295202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `-0.0141` n `228`; crypto_major avg `-0.0721` n `8`; equity avg `0.0288` n `88`; fx avg `0.0037` n `6`; index avg `0.0178` n `25`; metal avg `0.0676` n `20`; unknown avg `1.1528` n `763`
- 1h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.3972` n `228`; crypto_major avg `-0.5488` n `8`; equity avg `-0.3097` n `88`; fx avg `0.0073` n `6`; index avg `-0.1146` n `25`; metal avg `0.0728` n `20`; unknown avg `1.2191` n `763`
- 4h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.0731` n `228`; crypto_major avg `-0.2571` n `8`; equity avg `-0.1964` n `88`; fx avg `0.0441` n `6`; index avg `-0.1071` n `25`; metal avg `0.0829` n `20`; unknown avg `142.9062` n `763`
- 24h: commodity avg `-0.6287` n `12`; crypto_alt avg `1.5774` n `228`; crypto_major avg `1.1142` n `8`; equity avg `-1.9267` n `88`; fx avg `0.0213` n `6`; index avg `-0.6047` n `25`; metal avg `0.4382` n `20`; unknown avg `148.1103` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
