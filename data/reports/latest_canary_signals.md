# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T07:22:27.960299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.1136` n `228`; crypto_major avg `0.063` n `8`; equity avg `0.0955` n `88`; fx avg `0.0012` n `6`; index avg `0.0411` n `23`; metal avg `0.0158` n `20`; unknown avg `0.0186` n `764`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `-0.157` n `228`; crypto_major avg `-0.3947` n `8`; equity avg `0.076` n `88`; fx avg `0.0054` n `6`; index avg `0.0076` n `23`; metal avg `-0.0738` n `20`; unknown avg `-0.0218` n `764`
- 4h: commodity avg `-0.078` n `12`; crypto_alt avg `-0.2096` n `228`; crypto_major avg `-0.2693` n `8`; equity avg `0.4498` n `88`; fx avg `0.017` n `6`; index avg `0.1614` n `23`; metal avg `-0.2491` n `20`; unknown avg `-0.0037` n `732`
- 24h: commodity avg `-0.4816` n `12`; crypto_alt avg `0.4983` n `228`; crypto_major avg `0.2538` n `8`; equity avg `0.4754` n `88`; fx avg `0.0557` n `6`; index avg `0.1146` n `23`; metal avg `-0.175` n `20`; unknown avg `1.1225` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
