# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T01:37:28.088154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `0.0805` n `238`; crypto_major avg `0.1512` n `8`; equity avg `0.0274` n `154`; fx avg `0.0313` n `6`; index avg `0.0077` n `27`; metal avg `-0.0105` n `20`; unknown avg `3.1642` n `1238`
- 1h: commodity avg `0.1064` n `13`; crypto_alt avg `0.3645` n `238`; crypto_major avg `0.38` n `8`; equity avg `0.5632` n `154`; fx avg `0.0579` n `6`; index avg `0.1129` n `27`; metal avg `0.0014` n `20`; unknown avg `2.6558` n `1234`
- 4h: commodity avg `0.1501` n `13`; crypto_alt avg `0.0078` n `238`; crypto_major avg `-0.0254` n `8`; equity avg `0.6998` n `154`; fx avg `0.1069` n `6`; index avg `0.1489` n `27`; metal avg `-0.0245` n `20`; unknown avg `4.4344` n `1212`
- 24h: commodity avg `0.056` n `13`; crypto_alt avg `1.5469` n `237`; crypto_major avg `1.4504` n `8`; equity avg `1.7733` n `154`; fx avg `0.0613` n `6`; index avg `0.4099` n `27`; metal avg `0.2138` n `20`; unknown avg `355.6565` n `1028`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
