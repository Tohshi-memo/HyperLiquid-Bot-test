# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T19:07:27.013874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.0187` n `236`; crypto_major avg `-0.0914` n `8`; equity avg `0.0142` n `151`; fx avg `-0.0037` n `6`; index avg `0.0012` n `26`; metal avg `-0.0018` n `20`; unknown avg `4.5853` n `1183`
- 1h: commodity avg `0.0164` n `13`; crypto_alt avg `0.3974` n `236`; crypto_major avg `0.0713` n `8`; equity avg `0.1075` n `151`; fx avg `0.0038` n `6`; index avg `0.0367` n `26`; metal avg `0.0085` n `20`; unknown avg `4.7175` n `1175`
- 4h: commodity avg `0.0489` n `13`; crypto_alt avg `-0.0236` n `236`; crypto_major avg `-0.2357` n `8`; equity avg `-0.0485` n `151`; fx avg `-0.0265` n `6`; index avg `-0.023` n `26`; metal avg `-0.0228` n `20`; unknown avg `0.9644` n `1137`
- 24h: commodity avg `0.056` n `13`; crypto_alt avg `-0.2936` n `236`; crypto_major avg `0.3971` n `8`; equity avg `0.2627` n `151`; fx avg `-0.0171` n `6`; index avg `0.0451` n `26`; metal avg `0.0313` n `20`; unknown avg `2.6571` n `1011`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1722`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1473`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
