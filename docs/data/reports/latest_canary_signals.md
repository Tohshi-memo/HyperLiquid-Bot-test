# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T19:37:32.823626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `13`; crypto_alt avg `-0.0477` n `239`; crypto_major avg `-0.0858` n `8`; equity avg `-0.0457` n `160`; fx avg `-0.0071` n `6`; index avg `0.0072` n `27`; metal avg `-0.0206` n `20`; unknown avg `0.9556` n `1262`
- 1h: commodity avg `0.0652` n `13`; crypto_alt avg `-0.7112` n `239`; crypto_major avg `-0.327` n `8`; equity avg `0.0023` n `160`; fx avg `0.0105` n `6`; index avg `0.0266` n `27`; metal avg `-0.0037` n `20`; unknown avg `18.8882` n `1256`
- 4h: commodity avg `0.5549` n `13`; crypto_alt avg `-0.9435` n `239`; crypto_major avg `-0.2329` n `8`; equity avg `-1.1764` n `160`; fx avg `-0.0041` n `6`; index avg `-0.1115` n `27`; metal avg `-0.1297` n `20`; unknown avg `18.2904` n `1250`
- 24h: commodity avg `-0.0519` n `13`; crypto_alt avg `-2.1083` n `239`; crypto_major avg `-2.8898` n `8`; equity avg `-1.8653` n `160`; fx avg `-0.0799` n `6`; index avg `-0.2008` n `27`; metal avg `-0.553` n `20`; unknown avg `-0.0419` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2506`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
