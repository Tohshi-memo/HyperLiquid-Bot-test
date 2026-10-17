# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T11:07:30.786315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `-0.1187` n `236`; crypto_major avg `-0.0405` n `8`; equity avg `0.0245` n `151`; fx avg `0.0031` n `6`; index avg `0.0008` n `26`; metal avg `0.0051` n `20`; unknown avg `1.0955` n `1191`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `0.0062` n `236`; crypto_major avg `0.1104` n `8`; equity avg `0.0691` n `151`; fx avg `0.0026` n `6`; index avg `-0.0007` n `26`; metal avg `0.0131` n `20`; unknown avg `0.7379` n `1189`
- 4h: commodity avg `0.0669` n `13`; crypto_alt avg `-0.4014` n `236`; crypto_major avg `-0.094` n `8`; equity avg `0.0497` n `151`; fx avg `0.0057` n `6`; index avg `0.0265` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.0562` n `1173`
- 24h: commodity avg `0.323` n `13`; crypto_alt avg `-2.252` n `236`; crypto_major avg `-1.5874` n `8`; equity avg `-3.3372` n `151`; fx avg `0.01` n `6`; index avg `-0.5408` n `26`; metal avg `-0.2141` n `20`; unknown avg `8.6282` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1827`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1502`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1255`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0708`, n `666`, weak_sample_signal
