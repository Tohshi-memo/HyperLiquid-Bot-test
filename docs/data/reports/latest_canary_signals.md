# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T11:37:26.525611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.0334` n `239`; crypto_major avg `-0.0997` n `8`; equity avg `-0.2115` n `168`; fx avg `-0.0068` n `6`; index avg `-0.0166` n `27`; metal avg `0.0039` n `20`; unknown avg `0.1785` n `1259`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `-0.0493` n `239`; crypto_major avg `-0.0233` n `8`; equity avg `-0.2936` n `168`; fx avg `-0.0198` n `6`; index avg `-0.0162` n `27`; metal avg `-0.0327` n `20`; unknown avg `19.4004` n `1259`
- 4h: commodity avg `-0.2198` n `13`; crypto_alt avg `0.0008` n `239`; crypto_major avg `0.2766` n `8`; equity avg `0.3064` n `168`; fx avg `-0.0332` n `6`; index avg `0.0219` n `27`; metal avg `0.0137` n `20`; unknown avg `179.3285` n `1115`
- 24h: commodity avg `0.0237` n `13`; crypto_alt avg `1.6869` n `239`; crypto_major avg `2.9714` n `8`; equity avg `3.6798` n `168`; fx avg `-0.0959` n `6`; index avg `0.2942` n `27`; metal avg `1.2266` n `20`; unknown avg `59.4021` n `1021`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
