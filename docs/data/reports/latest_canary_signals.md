# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T03:22:31.076842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.49` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.2851` n `228`; crypto_major avg `0.1535` n `8`; equity avg `0.0699` n `77`; fx avg `0.0037` n `6`; index avg `0.081` n `23`; metal avg `0.0109` n `18`; unknown avg `0.0523` n `687`
- 1h: commodity avg `-0.1286` n `12`; crypto_alt avg `-0.279` n `228`; crypto_major avg `-0.2063` n `8`; equity avg `0.0702` n `77`; fx avg `-0.009` n `6`; index avg `0.0988` n `23`; metal avg `0.2526` n `18`; unknown avg `-0.0098` n `679`
- 4h: commodity avg `-0.4238` n `12`; crypto_alt avg `-0.3582` n `228`; crypto_major avg `-0.3528` n `8`; equity avg `-0.2048` n `77`; fx avg `-0.0842` n `6`; index avg `0.1096` n `23`; metal avg `-0.315` n `18`; unknown avg `-0.0347` n `671`
- 24h: commodity avg `0.5687` n `12`; crypto_alt avg `-0.2349` n `228`; crypto_major avg `1.3741` n `8`; equity avg `0.8555` n `76`; fx avg `-0.0687` n `6`; index avg `0.6188` n `23`; metal avg `-0.5503` n `18`; unknown avg `0.7667` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
