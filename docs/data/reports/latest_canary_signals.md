# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T16:52:25.576742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.1422` n `230`; crypto_major avg `0.2382` n `8`; equity avg `-0.0077` n `121`; fx avg `0.001` n `6`; index avg `-0.0005` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0155` n `794`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `1.0366` n `230`; crypto_major avg `1.0367` n `8`; equity avg `0.0375` n `121`; fx avg `0.01` n `6`; index avg `-0.0022` n `25`; metal avg `0.0087` n `20`; unknown avg `0.1889` n `794`
- 4h: commodity avg `-0.0511` n `12`; crypto_alt avg `-0.0015` n `230`; crypto_major avg `-0.1589` n `8`; equity avg `-0.0616` n `121`; fx avg `0.0062` n `6`; index avg `-0.004` n `25`; metal avg `0.0151` n `20`; unknown avg `0.1723` n `794`
- 24h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.5455` n `230`; crypto_major avg `2.7696` n `8`; equity avg `-0.5037` n `121`; fx avg `0.0665` n `6`; index avg `-0.062` n `25`; metal avg `-0.1807` n `20`; unknown avg `0.4338` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
