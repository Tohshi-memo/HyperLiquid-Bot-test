# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T18:07:21.038963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1224` n `12`; crypto_alt avg `0.171` n `228`; crypto_major avg `0.2431` n `8`; equity avg `0.0618` n `67`; fx avg `0.0029` n `6`; index avg `0.0109` n `23`; metal avg `0.0179` n `18`; unknown avg `1.1989` n `396`
- 1h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.1215` n `228`; crypto_major avg `0.2198` n `8`; equity avg `0.1223` n `67`; fx avg `0.0105` n `6`; index avg `-0.0321` n `23`; metal avg `0.0417` n `18`; unknown avg `1.2368` n `396`
- 4h: commodity avg `-0.5615` n `12`; crypto_alt avg `1.5005` n `228`; crypto_major avg `1.2343` n `8`; equity avg `0.5598` n `67`; fx avg `0.0071` n `6`; index avg `0.1069` n `23`; metal avg `0.2124` n `18`; unknown avg `1.8841` n `396`
- 24h: commodity avg `0.2099` n `12`; crypto_alt avg `-2.2445` n `228`; crypto_major avg `-1.5704` n `8`; equity avg `-0.7665` n `67`; fx avg `0.0192` n `6`; index avg `-0.3278` n `23`; metal avg `-0.1414` n `18`; unknown avg `-0.7889` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
