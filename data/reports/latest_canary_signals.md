# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T08:52:23.791704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `0.1114` n `230`; crypto_major avg `0.0361` n `8`; equity avg `0.005` n `121`; fx avg `0.0016` n `6`; index avg `0.0014` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0425` n `794`
- 1h: commodity avg `-0.0328` n `12`; crypto_alt avg `0.6781` n `230`; crypto_major avg `0.61` n `8`; equity avg `0.0997` n `121`; fx avg `-0.0581` n `6`; index avg `0.014` n `25`; metal avg `-0.0101` n `20`; unknown avg `0.137` n `794`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `2.0055` n `230`; crypto_major avg `0.9791` n `8`; equity avg `0.0593` n `121`; fx avg `-0.0375` n `6`; index avg `-0.0143` n `25`; metal avg `0.0053` n `20`; unknown avg `0.6275` n `778`
- 24h: commodity avg `-0.0201` n `12`; crypto_alt avg `-2.1006` n `230`; crypto_major avg `-0.4413` n `8`; equity avg `0.1694` n `121`; fx avg `0.0575` n `6`; index avg `0.0067` n `25`; metal avg `0.0484` n `20`; unknown avg `2.5765` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
