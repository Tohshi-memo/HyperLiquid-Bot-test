# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T19:37:29.575084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.3951` n `231`; crypto_major avg `-0.4519` n `8`; equity avg `0.0225` n `122`; fx avg `-0.0091` n `6`; index avg `0.0058` n `25`; metal avg `-0.0372` n `20`; unknown avg `0.0128` n `795`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `-0.5845` n `231`; crypto_major avg `-0.3655` n `8`; equity avg `-0.0765` n `122`; fx avg `-0.0137` n `6`; index avg `-0.0052` n `25`; metal avg `0.0719` n `20`; unknown avg `-0.1108` n `795`
- 4h: commodity avg `0.1392` n `12`; crypto_alt avg `-0.5042` n `231`; crypto_major avg `-0.2892` n `8`; equity avg `-0.0868` n `122`; fx avg `-0.002` n `6`; index avg `-0.0233` n `25`; metal avg `0.0577` n `20`; unknown avg `-0.2022` n `795`
- 24h: commodity avg `-0.5621` n `12`; crypto_alt avg `-0.9579` n `231`; crypto_major avg `0.3693` n `8`; equity avg `1.7896` n `122`; fx avg `0.0381` n `6`; index avg `0.1829` n `25`; metal avg `0.012` n `20`; unknown avg `-0.3746` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
