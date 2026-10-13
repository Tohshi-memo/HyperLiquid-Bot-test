# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T22:37:28.184108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.0874` n `235`; crypto_major avg `-0.0001` n `8`; equity avg `0.1037` n `151`; fx avg `0.0109` n `6`; index avg `0.0046` n `26`; metal avg `-0.0046` n `20`; unknown avg `1.4531` n `1135`
- 1h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.0074` n `235`; crypto_major avg `0.0418` n `8`; equity avg `0.1474` n `151`; fx avg `0.0085` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0085` n `20`; unknown avg `2.8035` n `1077`
- 4h: commodity avg `0.1274` n `13`; crypto_alt avg `0.3841` n `235`; crypto_major avg `0.2158` n `8`; equity avg `0.3997` n `151`; fx avg `-0.0106` n `6`; index avg `0.0164` n `26`; metal avg `-0.0226` n `20`; unknown avg `2.831` n `1019`
- 24h: commodity avg `0.7749` n `13`; crypto_alt avg `-0.1736` n `235`; crypto_major avg `0.325` n `8`; equity avg `-0.4754` n `151`; fx avg `0.1622` n `6`; index avg `-0.1497` n `26`; metal avg `-0.3024` n `20`; unknown avg `1.6829` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1573`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1435`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0914`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
