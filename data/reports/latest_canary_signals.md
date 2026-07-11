# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T01:04:44.644780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0258` n `229`; crypto_major avg `-0.0021` n `8`; equity avg `0.0015` n `92`; fx avg `0.0011` n `6`; index avg `0.0001` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0229` n `765`
- 1h: commodity avg `0.0364` n `12`; crypto_alt avg `-0.0115` n `229`; crypto_major avg `-0.0806` n `8`; equity avg `-0.03` n `92`; fx avg `-0.0043` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0027` n `20`; unknown avg `1.5642` n `765`
- 4h: commodity avg `0.0061` n `12`; crypto_alt avg `0.2542` n `229`; crypto_major avg `0.0685` n `8`; equity avg `0.061` n `92`; fx avg `-0.0004` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0273` n `20`; unknown avg `1.3966` n `765`
- 24h: commodity avg `-0.2327` n `12`; crypto_alt avg `1.1101` n `229`; crypto_major avg `0.9727` n `8`; equity avg `-0.4827` n `92`; fx avg `-0.1638` n `6`; index avg `0.1069` n `25`; metal avg `0.0852` n `20`; unknown avg `1.0726` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
