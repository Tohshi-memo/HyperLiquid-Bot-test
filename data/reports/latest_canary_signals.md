# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T17:52:43.875537+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0627` n `12`; crypto_alt avg `-0.3144` n `231`; crypto_major avg `-0.2923` n `8`; equity avg `-0.063` n `122`; fx avg `0.0024` n `6`; index avg `-0.0043` n `25`; metal avg `0.0103` n `20`; unknown avg `0.02` n `797`
- 1h: commodity avg `-0.0949` n `12`; crypto_alt avg `0.4876` n `231`; crypto_major avg `0.699` n `8`; equity avg `0.3143` n `122`; fx avg `-0.0003` n `6`; index avg `0.0365` n `25`; metal avg `0.0372` n `20`; unknown avg `0.3064` n `797`
- 4h: commodity avg `0.2107` n `12`; crypto_alt avg `-0.3426` n `231`; crypto_major avg `-0.0332` n `8`; equity avg `-0.243` n `122`; fx avg `-0.0089` n `6`; index avg `-0.0423` n `25`; metal avg `-0.2212` n `20`; unknown avg `0.0693` n `797`
- 24h: commodity avg `0.2843` n `12`; crypto_alt avg `-1.9655` n `231`; crypto_major avg `-1.7543` n `8`; equity avg `-0.0885` n `122`; fx avg `-0.0448` n `6`; index avg `0.0478` n `25`; metal avg `-0.3063` n `20`; unknown avg `0.5771` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
