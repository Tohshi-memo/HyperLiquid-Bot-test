# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T22:22:28.926101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.104` n `231`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0074` n `128`; fx avg `-0.001` n `6`; index avg `-0.0024` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.4842` n `783`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.1199` n `231`; crypto_major avg `-0.0881` n `8`; equity avg `0.0068` n `128`; fx avg `0.0024` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.237` n `774`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.0636` n `231`; crypto_major avg `0.0359` n `8`; equity avg `0.2007` n `128`; fx avg `-0.0163` n `6`; index avg `0.0365` n `26`; metal avg `0.005` n `20`; unknown avg `0.2698` n `774`
- 24h: commodity avg `-0.0423` n `12`; crypto_alt avg `0.6572` n `231`; crypto_major avg `1.0683` n `8`; equity avg `0.4323` n `128`; fx avg `-0.0371` n `6`; index avg `0.0764` n `26`; metal avg `0.1157` n `20`; unknown avg `4591.0466` n `732`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
