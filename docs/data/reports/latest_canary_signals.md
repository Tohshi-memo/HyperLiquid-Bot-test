# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T12:07:27.145580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0667` n `12`; crypto_alt avg `-0.0916` n `230`; crypto_major avg `-0.0241` n `8`; equity avg `-0.2585` n `102`; fx avg `0.0239` n `6`; index avg `-0.0281` n `25`; metal avg `0.0447` n `20`; unknown avg `-0.0287` n `780`
- 1h: commodity avg `0.2668` n `12`; crypto_alt avg `-0.3723` n `230`; crypto_major avg `-0.1897` n `8`; equity avg `-0.464` n `102`; fx avg `0.0039` n `6`; index avg `-0.0638` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0812` n `780`
- 4h: commodity avg `0.6848` n `12`; crypto_alt avg `-0.7709` n `230`; crypto_major avg `-0.3148` n `8`; equity avg `0.0787` n `102`; fx avg `0.084` n `6`; index avg `-0.0253` n `25`; metal avg `-0.1128` n `20`; unknown avg `0.704` n `780`
- 24h: commodity avg `0.6113` n `12`; crypto_alt avg `-0.7492` n `230`; crypto_major avg `-0.4758` n `8`; equity avg `6.3664` n `102`; fx avg `-0.0815` n `6`; index avg `0.8959` n `25`; metal avg `0.0225` n `20`; unknown avg `0.7923` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
