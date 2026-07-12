# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T12:37:24.847578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0265` n `12`; crypto_alt avg `-0.0505` n `230`; crypto_major avg `-0.0221` n `8`; equity avg `0.004` n `92`; fx avg `-0.0043` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0135` n `765`
- 1h: commodity avg `-0.1153` n `12`; crypto_alt avg `0.1096` n `230`; crypto_major avg `0.098` n `8`; equity avg `-0.0004` n `92`; fx avg `0.0033` n `6`; index avg `0.0036` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0379` n `765`
- 4h: commodity avg `-0.0506` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.3027` n `8`; equity avg `0.0747` n `92`; fx avg `0.0025` n `6`; index avg `-0.0145` n `25`; metal avg `-0.0039` n `20`; unknown avg `-0.0581` n `763`
- 24h: commodity avg `0.3535` n `12`; crypto_alt avg `-0.8177` n `230`; crypto_major avg `-0.4021` n `8`; equity avg `-0.1246` n `92`; fx avg `0.0068` n `6`; index avg `-0.12` n `25`; metal avg `-0.1002` n `20`; unknown avg `0.1084` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
