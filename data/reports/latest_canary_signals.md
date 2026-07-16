# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T23:52:26.932538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `0.0555` n `8`; equity avg `0.0215` n `94`; fx avg `-0.0062` n `6`; index avg `0.0117` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.1382` n `768`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.3279` n `230`; crypto_major avg `-0.408` n `8`; equity avg `-0.3135` n `94`; fx avg `0.0078` n `6`; index avg `-0.0206` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.1095` n `768`
- 4h: commodity avg `0.0875` n `12`; crypto_alt avg `-0.8497` n `230`; crypto_major avg `-0.8957` n `8`; equity avg `-0.6939` n `94`; fx avg `-0.0108` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0624` n `20`; unknown avg `-0.3214` n `768`
- 24h: commodity avg `-0.1607` n `12`; crypto_alt avg `-1.7694` n `230`; crypto_major avg `-2.7841` n `8`; equity avg `-4.319` n `94`; fx avg `-0.1582` n `6`; index avg `-0.559` n `25`; metal avg `-0.8425` n `20`; unknown avg `-0.5643` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
