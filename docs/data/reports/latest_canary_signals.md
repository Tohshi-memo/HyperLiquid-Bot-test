# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T20:38:05.480132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1146` n `12`; crypto_alt avg `-0.3255` n `231`; crypto_major avg `-0.4215` n `8`; equity avg `-0.0219` n `122`; fx avg `0.0054` n `6`; index avg `0.007` n `25`; metal avg `-0.0269` n `20`; unknown avg `-0.1222` n `795`
- 1h: commodity avg `-0.2708` n `12`; crypto_alt avg `-0.3216` n `231`; crypto_major avg `-0.3444` n `8`; equity avg `0.2338` n `122`; fx avg `0.0116` n `6`; index avg `0.0579` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0364` n `795`
- 4h: commodity avg `-0.2506` n `12`; crypto_alt avg `-1.1546` n `231`; crypto_major avg `-0.8852` n `8`; equity avg `0.1166` n `122`; fx avg `0.0073` n `6`; index avg `0.0414` n `25`; metal avg `0.097` n `20`; unknown avg `-0.3478` n `795`
- 24h: commodity avg `-0.7266` n `12`; crypto_alt avg `-1.6748` n `231`; crypto_major avg `-0.4161` n `8`; equity avg `2.1275` n `122`; fx avg `0.0518` n `6`; index avg `0.2807` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.4702` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
