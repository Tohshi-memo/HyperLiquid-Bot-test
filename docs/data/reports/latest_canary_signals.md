# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T06:07:36.554825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.2725` n `230`; crypto_major avg `-0.3748` n `8`; equity avg `-0.2032` n `102`; fx avg `-0.019` n `6`; index avg `-0.0359` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0642` n `758`
- 1h: commodity avg `0.1297` n `12`; crypto_alt avg `-0.3092` n `230`; crypto_major avg `-0.5253` n `8`; equity avg `-0.4815` n `102`; fx avg `-0.0383` n `6`; index avg `-0.0877` n `25`; metal avg `-0.0277` n `20`; unknown avg `-0.1052` n `758`
- 4h: commodity avg `0.1051` n `12`; crypto_alt avg `0.1245` n `230`; crypto_major avg `-0.2824` n `8`; equity avg `-0.5499` n `102`; fx avg `-0.1077` n `6`; index avg `-0.0891` n `25`; metal avg `-0.0358` n `20`; unknown avg `-0.0938` n `758`
- 24h: commodity avg `-0.555` n `12`; crypto_alt avg `-4.2803` n `230`; crypto_major avg `-4.2165` n `8`; equity avg `-4.1109` n `102`; fx avg `-0.1719` n `6`; index avg `-0.9104` n `25`; metal avg `-0.4327` n `20`; unknown avg `1161.768` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
