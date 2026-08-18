# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T07:52:26.807642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `-0.0688` n `230`; crypto_major avg `-0.1388` n `8`; equity avg `-0.0432` n `114`; fx avg `0.0016` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.0178` n `795`
- 1h: commodity avg `-0.0896` n `12`; crypto_alt avg `-0.0512` n `230`; crypto_major avg `-0.1607` n `8`; equity avg `-0.1897` n `114`; fx avg `0.0037` n `6`; index avg `-0.0269` n `25`; metal avg `-0.071` n `20`; unknown avg `0.0103` n `793`
- 4h: commodity avg `-0.0506` n `12`; crypto_alt avg `0.413` n `230`; crypto_major avg `0.2165` n `8`; equity avg `-0.3034` n `114`; fx avg `0.0029` n `6`; index avg `-0.0898` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0408` n `761`
- 24h: commodity avg `0.6834` n `12`; crypto_alt avg `-1.137` n `230`; crypto_major avg `-0.0417` n `8`; equity avg `-1.8497` n `114`; fx avg `-0.0247` n `6`; index avg `-0.4654` n `25`; metal avg `-0.2808` n `20`; unknown avg `0.0019` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
