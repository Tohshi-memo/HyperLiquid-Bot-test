# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T04:06:07.008246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.2247` n `230`; crypto_major avg `-0.0681` n `8`; equity avg `-0.0286` n `121`; fx avg `-0.0043` n `6`; index avg `0.0` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.1621` n `794`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `-0.8989` n `230`; crypto_major avg `-0.4517` n `8`; equity avg `-0.0523` n `121`; fx avg `-0.005` n `6`; index avg `0.0017` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.2243` n `794`
- 4h: commodity avg `-0.0179` n `12`; crypto_alt avg `-2.2587` n `230`; crypto_major avg `-0.6676` n `8`; equity avg `0.0571` n `121`; fx avg `0.0033` n `6`; index avg `0.0229` n `25`; metal avg `0.0107` n `20`; unknown avg `1.7692` n `794`
- 24h: commodity avg `0.0535` n `12`; crypto_alt avg `-7.7176` n `230`; crypto_major avg `-3.5199` n `8`; equity avg `-0.314` n `121`; fx avg `0.1013` n `6`; index avg `-0.0217` n `25`; metal avg `-0.0422` n `20`; unknown avg `2.023` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
