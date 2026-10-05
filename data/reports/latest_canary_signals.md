# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T07:37:27.757904+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `0.1051` n `235`; crypto_major avg `0.087` n `8`; equity avg `-0.0121` n `144`; fx avg `0.0078` n `6`; index avg `-0.0016` n `26`; metal avg `-0.004` n `20`; unknown avg `0.1858` n `1079`
- 1h: commodity avg `0.0342` n `13`; crypto_alt avg `0.5916` n `235`; crypto_major avg `0.4568` n `8`; equity avg `-0.0335` n `144`; fx avg `0.0362` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.5814` n `1077`
- 4h: commodity avg `0.091` n `13`; crypto_alt avg `0.5669` n `235`; crypto_major avg `0.3305` n `8`; equity avg `-0.157` n `144`; fx avg `0.0179` n `6`; index avg `-0.0316` n `26`; metal avg `0.0644` n `20`; unknown avg `0.138` n `1015`
- 24h: commodity avg `-0.2309` n `13`; crypto_alt avg `1.0153` n `235`; crypto_major avg `1.5094` n `8`; equity avg `0.2727` n `144`; fx avg `-0.0744` n `6`; index avg `-0.042` n `26`; metal avg `0.1699` n `20`; unknown avg `-0.0197` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
