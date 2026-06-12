# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T21:07:33.042848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1237` n `12`; crypto_alt avg `0.0189` n `228`; crypto_major avg `0.0442` n `8`; equity avg `-0.0185` n `74`; fx avg `-0.0364` n `6`; index avg `-0.0266` n `23`; metal avg `-0.0071` n `18`; unknown avg `-0.2267` n `643`
- 1h: commodity avg `-0.2315` n `12`; crypto_alt avg `-0.1981` n `228`; crypto_major avg `-0.1208` n `8`; equity avg `0.0349` n `74`; fx avg `-0.0224` n `6`; index avg `0.0122` n `23`; metal avg `0.1088` n `18`; unknown avg `0.6589` n `643`
- 4h: commodity avg `-0.2845` n `12`; crypto_alt avg `-0.7931` n `228`; crypto_major avg `-0.8508` n `8`; equity avg `-0.4346` n `74`; fx avg `-0.0254` n `6`; index avg `-0.0406` n `23`; metal avg `0.2986` n `18`; unknown avg `0.2509` n `643`
- 24h: commodity avg `-0.7268` n `12`; crypto_alt avg `-0.5342` n `228`; crypto_major avg `0.4119` n `8`; equity avg `-0.2925` n `74`; fx avg `0.0236` n `6`; index avg `0.5447` n `23`; metal avg `0.5248` n `18`; unknown avg `40.4498` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
