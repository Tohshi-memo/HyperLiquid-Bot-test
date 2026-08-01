# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T16:37:25.897886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.0573` n `230`; crypto_major avg `0.0676` n `8`; equity avg `-0.0055` n `102`; fx avg `0.0011` n `6`; index avg `0.0046` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0107` n `782`
- 1h: commodity avg `0.0788` n `12`; crypto_alt avg `0.2431` n `230`; crypto_major avg `0.1051` n `8`; equity avg `-0.0479` n `102`; fx avg `0.0006` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0706` n `782`
- 4h: commodity avg `0.026` n `12`; crypto_alt avg `0.074` n `230`; crypto_major avg `0.1287` n `8`; equity avg `-0.162` n `102`; fx avg `0.0285` n `6`; index avg `-0.0186` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.13` n `782`
- 24h: commodity avg `0.6994` n `12`; crypto_alt avg `0.5005` n `230`; crypto_major avg `-0.2945` n `8`; equity avg `-0.6921` n `102`; fx avg `-0.0767` n `6`; index avg `-0.0735` n `25`; metal avg `0.0406` n `20`; unknown avg `4.2643` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
