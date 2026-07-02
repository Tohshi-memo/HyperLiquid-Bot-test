# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T02:06:47.930093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `-0.0148` n `228`; crypto_major avg `-0.0382` n `8`; equity avg `0.0591` n `88`; fx avg `-0.0146` n `6`; index avg `0.0056` n `25`; metal avg `-0.0783` n `20`; unknown avg `0.1447` n `763`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `0.6391` n `228`; crypto_major avg `0.6476` n `8`; equity avg `0.3767` n `88`; fx avg `-0.0069` n `6`; index avg `0.1764` n `25`; metal avg `-0.026` n `20`; unknown avg `-0.3404` n `761`
- 4h: commodity avg `-0.0572` n `12`; crypto_alt avg `-0.391` n `228`; crypto_major avg `-0.8739` n `8`; equity avg `0.0901` n `88`; fx avg `0.0021` n `6`; index avg `0.0747` n `25`; metal avg `0.2071` n `20`; unknown avg `13.0984` n `761`
- 24h: commodity avg `-0.5508` n `12`; crypto_alt avg `2.4641` n `228`; crypto_major avg `1.4101` n `8`; equity avg `-0.5517` n `88`; fx avg `-0.0359` n `6`; index avg `-0.1402` n `25`; metal avg `0.97` n `20`; unknown avg `16.0016` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
