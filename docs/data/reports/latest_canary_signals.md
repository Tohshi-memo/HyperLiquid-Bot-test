# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T19:08:22.501975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0518` n `231`; crypto_major avg `-0.0865` n `8`; equity avg `0.0804` n `122`; fx avg `-0.0035` n `6`; index avg `0.018` n `25`; metal avg `-0.03` n `20`; unknown avg `0.0537` n `797`
- 1h: commodity avg `-0.0796` n `12`; crypto_alt avg `0.143` n `231`; crypto_major avg `-0.1485` n `8`; equity avg `0.1561` n `122`; fx avg `-0.0079` n `6`; index avg `0.0412` n `25`; metal avg `-0.0414` n `20`; unknown avg `-0.0216` n `797`
- 4h: commodity avg `-0.0157` n `12`; crypto_alt avg `0.3305` n `231`; crypto_major avg `0.3776` n `8`; equity avg `0.3509` n `122`; fx avg `0.0013` n `6`; index avg `0.0484` n `25`; metal avg `-0.126` n `20`; unknown avg `0.1241` n `797`
- 24h: commodity avg `0.0657` n `12`; crypto_alt avg `-1.7982` n `231`; crypto_major avg `-1.8601` n `8`; equity avg `-0.0854` n `122`; fx avg `-0.0562` n `6`; index avg `0.0677` n `25`; metal avg `-0.3867` n `20`; unknown avg `0.4229` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
