# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T21:52:31.351455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `-0.0642` n `8`; equity avg `-0.028` n `92`; fx avg `-0.0008` n `6`; index avg `-0.0126` n `25`; metal avg `0.0111` n `20`; unknown avg `2.4163` n `768`
- 1h: commodity avg `-0.0516` n `12`; crypto_alt avg `0.1535` n `230`; crypto_major avg `0.1385` n `8`; equity avg `0.024` n `92`; fx avg `-0.0083` n `6`; index avg `-0.0018` n `25`; metal avg `0.0544` n `20`; unknown avg `-0.4547` n `768`
- 4h: commodity avg `0.2004` n `12`; crypto_alt avg `-0.0744` n `230`; crypto_major avg `0.1571` n `8`; equity avg `0.102` n `92`; fx avg `0.0077` n `6`; index avg `-0.0231` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.1706` n `767`
- 24h: commodity avg `0.2673` n `12`; crypto_alt avg `2.6545` n `230`; crypto_major avg `3.932` n `8`; equity avg `1.4251` n `92`; fx avg `-0.0121` n `6`; index avg `0.4094` n `25`; metal avg `0.6051` n `20`; unknown avg `0.2929` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
