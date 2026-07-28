# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T03:07:37.092715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.0364` n `8`; equity avg `-0.1454` n `102`; fx avg `0.0256` n `6`; index avg `-0.0397` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.0006` n `774`
- 1h: commodity avg `-0.1522` n `12`; crypto_alt avg `0.2059` n `230`; crypto_major avg `-0.0573` n `8`; equity avg `-0.3215` n `102`; fx avg `-0.0533` n `6`; index avg `-0.0516` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0037` n `774`
- 4h: commodity avg `-0.3045` n `12`; crypto_alt avg `-0.3386` n `230`; crypto_major avg `-0.627` n `8`; equity avg `-1.6457` n `102`; fx avg `0.0119` n `6`; index avg `-0.3858` n `25`; metal avg `-0.3189` n `20`; unknown avg `0.4348` n `774`
- 24h: commodity avg `-1.003` n `12`; crypto_alt avg `-3.8991` n `230`; crypto_major avg `-3.2952` n `8`; equity avg `-3.4839` n `102`; fx avg `-0.122` n `6`; index avg `-0.7583` n `25`; metal avg `-0.3151` n `20`; unknown avg `1161.8713` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.181`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
