# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T04:07:24.401394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1683` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0836` n `232`; crypto_major avg `-0.0575` n `8`; equity avg `0.0975` n `134`; fx avg `-0.0048` n `6`; index avg `0.0105` n `26`; metal avg `-0.005` n `20`; unknown avg `0.537` n `792`
- 1h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.601` n `232`; crypto_major avg `-0.4802` n `8`; equity avg `0.1066` n `134`; fx avg `-0.0084` n `6`; index avg `0.0214` n `26`; metal avg `-0.0399` n `20`; unknown avg `-0.1977` n `792`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `-1.2223` n `232`; crypto_major avg `-1.1609` n `8`; equity avg `0.2059` n `134`; fx avg `-0.0113` n `6`; index avg `0.0074` n `26`; metal avg `-0.1047` n `20`; unknown avg `2.967` n `758`
- 24h: commodity avg `0.0329` n `12`; crypto_alt avg `-0.3661` n `232`; crypto_major avg `-0.8129` n `8`; equity avg `0.4579` n `134`; fx avg `0.0399` n `6`; index avg `-0.0037` n `26`; metal avg `-0.1872` n `20`; unknown avg `73.2465` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
