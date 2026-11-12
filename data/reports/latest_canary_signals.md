# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T17:07:35.656716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `13`; crypto_alt avg `-0.2463` n `239`; crypto_major avg `-0.1378` n `8`; equity avg `-0.2499` n `162`; fx avg `0.0044` n `6`; index avg `-0.0256` n `27`; metal avg `-0.0615` n `20`; unknown avg `43.5745` n `1255`
- 1h: commodity avg `0.1406` n `13`; crypto_alt avg `-0.6558` n `239`; crypto_major avg `-0.5942` n `8`; equity avg `-0.573` n `162`; fx avg `-0.0236` n `6`; index avg `-0.0623` n `27`; metal avg `-0.0199` n `20`; unknown avg `43.955` n `1237`
- 4h: commodity avg `0.3619` n `13`; crypto_alt avg `-0.5192` n `239`; crypto_major avg `-0.6947` n `8`; equity avg `0.6008` n `162`; fx avg `-0.0405` n `6`; index avg `0.1225` n `27`; metal avg `-0.4049` n `20`; unknown avg `44.5642` n `1227`
- 24h: commodity avg `0.0076` n `13`; crypto_alt avg `-4.027` n `239`; crypto_major avg `-3.6186` n `8`; equity avg `-2.8148` n `162`; fx avg `-0.1382` n `6`; index avg `-0.138` n `27`; metal avg `-0.9023` n `20`; unknown avg `1.1035` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
