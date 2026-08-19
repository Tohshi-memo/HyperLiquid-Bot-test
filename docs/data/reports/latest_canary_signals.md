# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T10:43:06.992752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0643` n `12`; crypto_alt avg `0.0878` n `230`; crypto_major avg `0.0023` n `8`; equity avg `0.2097` n `120`; fx avg `0.0103` n `6`; index avg `0.0291` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.0433` n `791`
- 1h: commodity avg `0.0737` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `-0.0176` n `8`; equity avg `-0.2888` n `120`; fx avg `-0.0342` n `6`; index avg `-0.0258` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.0563` n `791`
- 4h: commodity avg `0.1101` n `12`; crypto_alt avg `0.1337` n `230`; crypto_major avg `0.2099` n `8`; equity avg `1.0031` n `120`; fx avg `-0.0636` n `6`; index avg `0.1926` n `25`; metal avg `0.1085` n `20`; unknown avg `-0.0925` n `789`
- 24h: commodity avg `0.5267` n `12`; crypto_alt avg `0.2271` n `230`; crypto_major avg `0.2583` n `8`; equity avg `-1.6563` n `120`; fx avg `-0.2075` n `6`; index avg `-0.1796` n `25`; metal avg `-0.4468` n `20`; unknown avg `-0.3853` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
