# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T12:22:33.915173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0942` n `12`; crypto_alt avg `0.0482` n `230`; crypto_major avg `0.0154` n `8`; equity avg `-0.1385` n `109`; fx avg `-0.0026` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0646` n `20`; unknown avg `0.0053` n `781`
- 1h: commodity avg `0.0304` n `12`; crypto_alt avg `0.0671` n `230`; crypto_major avg `-0.1356` n `8`; equity avg `0.0258` n `109`; fx avg `-0.0099` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0625` n `20`; unknown avg `-0.0044` n `781`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.2375` n `230`; crypto_major avg `-0.4624` n `8`; equity avg `-0.1473` n `109`; fx avg `-0.0319` n `6`; index avg `-0.0397` n `25`; metal avg `0.0157` n `20`; unknown avg `108.1611` n `781`
- 24h: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.1663` n `230`; crypto_major avg `-0.9234` n `8`; equity avg `-1.8372` n `109`; fx avg `0.0035` n `6`; index avg `-0.4345` n `25`; metal avg `0.0948` n `20`; unknown avg `113.0622` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
