# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T01:22:23.780292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0131` n `231`; crypto_major avg `0.0624` n `8`; equity avg `0.0036` n `124`; fx avg `0.0019` n `6`; index avg `-0.0029` n `25`; metal avg `0.0233` n `20`; unknown avg `0.3805` n `795`
- 1h: commodity avg `0.0932` n `12`; crypto_alt avg `-0.5536` n `231`; crypto_major avg `-0.4322` n `8`; equity avg `-0.378` n `124`; fx avg `-0.0384` n `6`; index avg `-0.1138` n `25`; metal avg `0.0639` n `20`; unknown avg `0.4441` n `795`
- 4h: commodity avg `0.0716` n `12`; crypto_alt avg `0.7481` n `231`; crypto_major avg `0.5807` n `8`; equity avg `-0.1095` n `124`; fx avg `-0.0748` n `6`; index avg `-0.0384` n `25`; metal avg `0.2297` n `20`; unknown avg `-0.0532` n `795`
- 24h: commodity avg `0.5032` n `12`; crypto_alt avg `0.7111` n `231`; crypto_major avg `0.6178` n `8`; equity avg `1.4631` n `124`; fx avg `-0.1585` n `6`; index avg `0.2572` n `25`; metal avg `-0.1588` n `20`; unknown avg `0.9127` n `778`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
