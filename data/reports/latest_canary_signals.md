# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T11:52:29.162744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.0405` n `230`; crypto_major avg `-0.0429` n `8`; equity avg `-0.1054` n `109`; fx avg `-0.0028` n `6`; index avg `-0.0399` n `25`; metal avg `-0.0399` n `20`; unknown avg `-0.0099` n `781`
- 1h: commodity avg `-0.0754` n `12`; crypto_alt avg `0.2444` n `230`; crypto_major avg `0.1095` n `8`; equity avg `0.1002` n `109`; fx avg `0.0068` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0959` n `20`; unknown avg `0.0335` n `781`
- 4h: commodity avg `0.0054` n `12`; crypto_alt avg `-0.1607` n `230`; crypto_major avg `-0.3443` n `8`; equity avg `-0.1222` n `109`; fx avg `-0.0502` n `6`; index avg `-0.0423` n `25`; metal avg `0.159` n `20`; unknown avg `108.129` n `781`
- 24h: commodity avg `-0.1002` n `12`; crypto_alt avg `0.3084` n `230`; crypto_major avg `-0.3236` n `8`; equity avg `-1.5936` n `109`; fx avg `-0.0043` n `6`; index avg `-0.4124` n `25`; metal avg `0.2261` n `20`; unknown avg `113.1173` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
