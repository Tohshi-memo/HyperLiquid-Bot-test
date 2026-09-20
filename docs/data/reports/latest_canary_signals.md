# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T02:22:27.913156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0601` n `12`; crypto_alt avg `-0.165` n `234`; crypto_major avg `-0.1952` n `8`; equity avg `0.0068` n `140`; fx avg `0.0074` n `6`; index avg `0.0015` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.0115` n `943`
- 1h: commodity avg `0.0461` n `12`; crypto_alt avg `0.0905` n `234`; crypto_major avg `-0.2941` n `8`; equity avg `0.0406` n `140`; fx avg `0.0056` n `6`; index avg `0.0074` n `26`; metal avg `-0.0096` n `20`; unknown avg `2.0838` n `941`
- 4h: commodity avg `0.1847` n `12`; crypto_alt avg `1.0402` n `234`; crypto_major avg `0.1034` n `8`; equity avg `0.0776` n `140`; fx avg `0.0066` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.4981` n `919`
- 24h: commodity avg `0.098` n `12`; crypto_alt avg `0.7108` n `234`; crypto_major avg `-1.1707` n `8`; equity avg `0.1351` n `140`; fx avg `-0.0428` n `6`; index avg `0.0302` n `26`; metal avg `0.0177` n `20`; unknown avg `1.4702` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
