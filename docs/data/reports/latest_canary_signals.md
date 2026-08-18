# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T09:07:28.418134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.036` n `8`; equity avg `-0.103` n `114`; fx avg `-0.0088` n `6`; index avg `-0.0308` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.004` n `795`
- 1h: commodity avg `-0.0307` n `12`; crypto_alt avg `0.2533` n `230`; crypto_major avg `0.2351` n `8`; equity avg `-0.2073` n `114`; fx avg `0.0175` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0133` n `20`; unknown avg `0.0201` n `795`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `0.3553` n `230`; crypto_major avg `0.0839` n `8`; equity avg `-0.9938` n `114`; fx avg `-0.0035` n `6`; index avg `-0.1787` n `25`; metal avg `-0.0843` n `20`; unknown avg `0.0061` n `761`
- 24h: commodity avg `0.5859` n `12`; crypto_alt avg `-0.7288` n `230`; crypto_major avg `0.2903` n `8`; equity avg `-2.57` n `114`; fx avg `0.0069` n `6`; index avg `-0.5353` n `25`; metal avg `-0.2563` n `20`; unknown avg `0.1281` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
