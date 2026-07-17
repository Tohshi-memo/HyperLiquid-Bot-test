# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T07:52:28.793233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0505` n `12`; crypto_alt avg `0.0938` n `230`; crypto_major avg `0.1718` n `8`; equity avg `-0.0648` n `96`; fx avg `0.0047` n `6`; index avg `-0.0108` n `25`; metal avg `0.0577` n `20`; unknown avg `0.0018` n `768`
- 1h: commodity avg `0.0603` n `12`; crypto_alt avg `-0.2681` n `230`; crypto_major avg `-0.1012` n `8`; equity avg `-0.202` n `96`; fx avg `-0.0212` n `6`; index avg `-0.0054` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0945` n `768`
- 4h: commodity avg `-0.1199` n `12`; crypto_alt avg `-0.8138` n `230`; crypto_major avg `-0.9621` n `8`; equity avg `-0.931` n `96`; fx avg `0.0012` n `6`; index avg `-0.1325` n `25`; metal avg `-0.077` n `20`; unknown avg `-0.1485` n `736`
- 24h: commodity avg `-0.1689` n `12`; crypto_alt avg `-1.962` n `230`; crypto_major avg `-3.1994` n `8`; equity avg `-5.449` n `94`; fx avg `-0.0755` n `6`; index avg `-0.7198` n `25`; metal avg `-0.6859` n `20`; unknown avg `-0.5426` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
