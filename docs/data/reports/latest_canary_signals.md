# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T09:07:33.723138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0747` n `12`; crypto_alt avg `0.1541` n `230`; crypto_major avg `0.0972` n `8`; equity avg `0.22` n `96`; fx avg `-0.0019` n `6`; index avg `0.0262` n `25`; metal avg `0.0401` n `20`; unknown avg `-0.0193` n `768`
- 1h: commodity avg `0.1331` n `12`; crypto_alt avg `0.1722` n `230`; crypto_major avg `0.1158` n `8`; equity avg `-0.3988` n `96`; fx avg `0.0101` n `6`; index avg `-0.0824` n `25`; metal avg `-0.0247` n `20`; unknown avg `-0.0907` n `768`
- 4h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.6129` n `230`; crypto_major avg `-0.615` n `8`; equity avg `-0.6658` n `96`; fx avg `0.043` n `6`; index avg `-0.0658` n `25`; metal avg `0.069` n `20`; unknown avg `-0.1287` n `736`
- 24h: commodity avg `0.0991` n `12`; crypto_alt avg `-1.522` n `230`; crypto_major avg `-2.7667` n `8`; equity avg `-5.7088` n `94`; fx avg `-0.0406` n `6`; index avg `-0.8223` n `25`; metal avg `-0.7835` n `20`; unknown avg `-0.517` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
