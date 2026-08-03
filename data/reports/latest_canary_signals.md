# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T02:37:36.751482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1405` n `230`; crypto_major avg `-0.1085` n `8`; equity avg `-0.0291` n `102`; fx avg `-0.0164` n `6`; index avg `-0.0294` n `25`; metal avg `-0.0342` n `20`; unknown avg `-0.0406` n `784`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.0439` n `230`; crypto_major avg `-0.0105` n `8`; equity avg `0.4372` n `102`; fx avg `-0.0437` n `6`; index avg `0.1178` n `25`; metal avg `-0.034` n `20`; unknown avg `-0.1329` n `784`
- 4h: commodity avg `0.0485` n `12`; crypto_alt avg `-0.6637` n `230`; crypto_major avg `-0.707` n `8`; equity avg `0.4959` n `102`; fx avg `-0.2931` n `6`; index avg `-0.0133` n `25`; metal avg `-0.1225` n `20`; unknown avg `-0.0754` n `783`
- 24h: commodity avg `-0.3499` n `12`; crypto_alt avg `-0.4107` n `230`; crypto_major avg `0.0391` n `8`; equity avg `1.0883` n `102`; fx avg `-0.3167` n `6`; index avg `0.1042` n `25`; metal avg `-0.0078` n `20`; unknown avg `1.3009` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
