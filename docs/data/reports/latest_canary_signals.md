# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T18:37:33.978964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0781` n `13`; crypto_alt avg `-0.0951` n `235`; crypto_major avg `-0.0866` n `8`; equity avg `-0.0504` n `150`; fx avg `-0.0084` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0066` n `20`; unknown avg `1.2654` n `1076`
- 1h: commodity avg `0.0384` n `13`; crypto_alt avg `-0.1691` n `235`; crypto_major avg `-0.0074` n `8`; equity avg `-0.1433` n `150`; fx avg `-0.0134` n `6`; index avg `-0.029` n `26`; metal avg `0.0381` n `20`; unknown avg `0.7454` n `1074`
- 4h: commodity avg `0.3874` n `13`; crypto_alt avg `-0.5353` n `235`; crypto_major avg `-0.6445` n `8`; equity avg `0.0537` n `150`; fx avg `0.0054` n `6`; index avg `-0.0356` n `26`; metal avg `0.2019` n `20`; unknown avg `1.0416` n `1060`
- 24h: commodity avg `0.0919` n `13`; crypto_alt avg `-0.2815` n `235`; crypto_major avg `-0.2737` n `8`; equity avg `0.6118` n `149`; fx avg `0.0959` n `6`; index avg `0.0162` n `26`; metal avg `0.0442` n `20`; unknown avg `381.7315` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
