# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T22:45:56.215777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.013` n `228`; crypto_major avg `0.0334` n `8`; equity avg `-0.0037` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0004` n `20`; unknown avg `0.0883` n `765`
- 1h: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.0447` n `228`; crypto_major avg `-0.0507` n `8`; equity avg `0.013` n `88`; fx avg `-0.0102` n `6`; index avg `0.0155` n `23`; metal avg `0.0826` n `20`; unknown avg `-0.2243` n `765`
- 4h: commodity avg `-0.0515` n `12`; crypto_alt avg `-0.512` n `228`; crypto_major avg `-0.3947` n `8`; equity avg `0.2822` n `88`; fx avg `-0.0142` n `6`; index avg `-0.0346` n `23`; metal avg `-0.2641` n `20`; unknown avg `5.099` n `763`
- 24h: commodity avg `0.1408` n `12`; crypto_alt avg `-2.2232` n `228`; crypto_major avg `-2.3662` n `8`; equity avg `1.2038` n `88`; fx avg `0.099` n `6`; index avg `0.2626` n `23`; metal avg `0.0382` n `20`; unknown avg `11.7369` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
