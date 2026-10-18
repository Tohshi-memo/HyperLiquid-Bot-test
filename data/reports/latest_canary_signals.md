# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T20:22:30.284683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `0.0649` n `237`; crypto_major avg `-0.0072` n `8`; equity avg `0.061` n `151`; fx avg `-0.0034` n `6`; index avg `0.0051` n `26`; metal avg `-0.0097` n `20`; unknown avg `7.603` n `1194`
- 1h: commodity avg `0.0284` n `13`; crypto_alt avg `-0.8459` n `237`; crypto_major avg `-0.4773` n `8`; equity avg `-0.101` n `151`; fx avg `-0.0454` n `6`; index avg `-0.026` n `26`; metal avg `-0.0549` n `20`; unknown avg `16.0534` n `1178`
- 4h: commodity avg `0.035` n `13`; crypto_alt avg `-1.8896` n `237`; crypto_major avg `-0.7964` n `8`; equity avg `-0.334` n `151`; fx avg `-0.0352` n `6`; index avg `-0.0451` n `26`; metal avg `-0.0384` n `20`; unknown avg `2.9438` n `1158`
- 24h: commodity avg `0.0845` n `13`; crypto_alt avg `-5.0796` n `236`; crypto_major avg `-2.428` n `8`; equity avg `-1.2466` n `151`; fx avg `-0.0423` n `6`; index avg `-0.174` n `26`; metal avg `-0.1016` n `20`; unknown avg `1.4956` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2098`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1416`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
