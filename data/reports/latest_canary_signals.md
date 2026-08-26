# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T06:52:28.577552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.069` n `12`; crypto_alt avg `0.1917` n `231`; crypto_major avg `0.1869` n `8`; equity avg `0.0722` n `122`; fx avg `-0.0152` n `6`; index avg `0.0054` n `25`; metal avg `0.0124` n `20`; unknown avg `-0.0333` n `797`
- 1h: commodity avg `-0.0597` n `12`; crypto_alt avg `-0.1801` n `231`; crypto_major avg `-0.2445` n `8`; equity avg `-0.0141` n `122`; fx avg `-0.0118` n `6`; index avg `0.0097` n `25`; metal avg `-0.0939` n `20`; unknown avg `0.0727` n `781`
- 4h: commodity avg `0.0686` n `12`; crypto_alt avg `-0.368` n `231`; crypto_major avg `-0.2156` n `8`; equity avg `-0.0883` n `122`; fx avg `-0.0447` n `6`; index avg `-0.0027` n `25`; metal avg `-0.2189` n `20`; unknown avg `0.1619` n `781`
- 24h: commodity avg `-0.592` n `12`; crypto_alt avg `-2.2619` n `231`; crypto_major avg `-2.317` n `8`; equity avg `0.7219` n `122`; fx avg `-0.0329` n `6`; index avg `0.0788` n `25`; metal avg `0.0944` n `20`; unknown avg `0.7708` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
