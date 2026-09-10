# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T06:37:29.830944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `0.134` n `233`; crypto_major avg `0.0665` n `8`; equity avg `0.0448` n `134`; fx avg `0.0002` n `6`; index avg `0.0066` n `26`; metal avg `-0.0` n `20`; unknown avg `1.5707` n `797`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.438` n `233`; crypto_major avg `-0.3864` n `8`; equity avg `-0.175` n `134`; fx avg `0.0037` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0839` n `20`; unknown avg `1.5801` n `773`
- 4h: commodity avg `-0.168` n `12`; crypto_alt avg `0.1675` n `233`; crypto_major avg `-0.0574` n `8`; equity avg `0.2697` n `134`; fx avg `0.0039` n `6`; index avg `0.1081` n `26`; metal avg `-0.0128` n `20`; unknown avg `125.7461` n `767`
- 24h: commodity avg `-0.159` n `12`; crypto_alt avg `-4.0072` n `233`; crypto_major avg `-2.8548` n `8`; equity avg `-1.1213` n `134`; fx avg `0.0468` n `6`; index avg `-0.113` n `26`; metal avg `0.2349` n `20`; unknown avg `0.9408` n `670`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
