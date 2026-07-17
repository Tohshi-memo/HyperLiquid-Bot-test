# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T19:07:26.117527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.1579` n `8`; equity avg `-0.1347` n `96`; fx avg `0.0031` n `6`; index avg `-0.028` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.0797` n `769`
- 1h: commodity avg `-0.1315` n `12`; crypto_alt avg `0.131` n `230`; crypto_major avg `0.076` n `8`; equity avg `-0.4727` n `96`; fx avg `-0.001` n `6`; index avg `-0.0358` n `25`; metal avg `-0.047` n `20`; unknown avg `-0.1179` n `769`
- 4h: commodity avg `0.3281` n `12`; crypto_alt avg `1.0626` n `230`; crypto_major avg `1.1883` n `8`; equity avg `1.1504` n `96`; fx avg `0.0495` n `6`; index avg `0.1556` n `25`; metal avg `0.0377` n `20`; unknown avg `1.0202` n `769`
- 24h: commodity avg `0.6543` n `12`; crypto_alt avg `-0.8` n `230`; crypto_major avg `-1.1084` n `8`; equity avg `-1.035` n `94`; fx avg `0.0845` n `6`; index avg `-0.1906` n `25`; metal avg `-0.0851` n `20`; unknown avg `0.0396` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
