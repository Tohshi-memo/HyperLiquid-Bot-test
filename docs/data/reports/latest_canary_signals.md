# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T05:22:28.536433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `0.1002` n `228`; crypto_major avg `0.1902` n `8`; equity avg `0.0964` n `88`; fx avg `0.0036` n `6`; index avg `0.0515` n `23`; metal avg `-0.0156` n `20`; unknown avg `0.4441` n `764`
- 1h: commodity avg `-0.1056` n `12`; crypto_alt avg `-0.4865` n `228`; crypto_major avg `-0.4811` n `8`; equity avg `-0.0397` n `88`; fx avg `0.0008` n `6`; index avg `0.0541` n `23`; metal avg `-0.13` n `20`; unknown avg `3.457` n `764`
- 4h: commodity avg `-0.1178` n `12`; crypto_alt avg `0.4293` n `228`; crypto_major avg `0.1884` n `8`; equity avg `0.1284` n `88`; fx avg `0.0739` n `6`; index avg `0.0412` n `23`; metal avg `-0.0408` n `20`; unknown avg `-0.4919` n `764`
- 24h: commodity avg `-0.4098` n `12`; crypto_alt avg `-0.2496` n `228`; crypto_major avg `-0.3283` n `8`; equity avg `-0.0436` n `88`; fx avg `0.0515` n `6`; index avg `-0.0189` n `23`; metal avg `-0.3057` n `20`; unknown avg `-0.9649` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
