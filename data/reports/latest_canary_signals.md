# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T21:22:26.686372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0465` n `12`; crypto_alt avg `-0.2754` n `228`; crypto_major avg `-0.1675` n `8`; equity avg `0.0008` n `88`; fx avg `-0.013` n `6`; index avg `0.0123` n `23`; metal avg `-0.0136` n `20`; unknown avg `-0.039` n `764`
- 1h: commodity avg `-0.249` n `12`; crypto_alt avg `-0.4051` n `228`; crypto_major avg `-0.28` n `8`; equity avg `0.0659` n `88`; fx avg `-0.0376` n `6`; index avg `0.0791` n `23`; metal avg `0.0086` n `20`; unknown avg `-0.3213` n `764`
- 4h: commodity avg `-0.3566` n `12`; crypto_alt avg `-0.4865` n `228`; crypto_major avg `-0.3728` n `8`; equity avg `0.1237` n `88`; fx avg `-0.0545` n `6`; index avg `0.0759` n `23`; metal avg `0.0326` n `20`; unknown avg `0.6743` n `764`
- 24h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.9849` n `228`; crypto_major avg `-1.3463` n `8`; equity avg `0.2234` n `88`; fx avg `-0.0825` n `6`; index avg `0.0254` n `23`; metal avg `0.0128` n `20`; unknown avg `15.0648` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
