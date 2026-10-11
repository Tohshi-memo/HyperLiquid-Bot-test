# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T22:52:25.266652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `0.0669` n `235`; crypto_major avg `-0.0094` n `8`; equity avg `-0.018` n `150`; fx avg `-0.0004` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0193` n `20`; unknown avg `1.9583` n `1134`
- 1h: commodity avg `0.0428` n `13`; crypto_alt avg `0.3991` n `235`; crypto_major avg `0.262` n `8`; equity avg `0.0618` n `150`; fx avg `-0.0044` n `6`; index avg `0.0041` n `26`; metal avg `-0.0701` n `20`; unknown avg `-0.1415` n `1132`
- 4h: commodity avg `0.117` n `13`; crypto_alt avg `0.3706` n `235`; crypto_major avg `0.0595` n `8`; equity avg `0.0709` n `150`; fx avg `-0.0254` n `6`; index avg `0.0027` n `26`; metal avg `-0.0363` n `20`; unknown avg `-0.178` n `1096`
- 24h: commodity avg `0.2118` n `13`; crypto_alt avg `1.9281` n `235`; crypto_major avg `0.6526` n `8`; equity avg `0.2752` n `150`; fx avg `0.0031` n `6`; index avg `0.0285` n `26`; metal avg `0.0188` n `20`; unknown avg `0.5507` n `965`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
