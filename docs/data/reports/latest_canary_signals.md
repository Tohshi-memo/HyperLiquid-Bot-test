# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T08:52:30.377812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0661` n `13`; crypto_alt avg `-0.1996` n `235`; crypto_major avg `-0.1988` n `8`; equity avg `-0.2335` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0609` n `20`; unknown avg `0.0257` n `1119`
- 1h: commodity avg `0.1003` n `13`; crypto_alt avg `-0.5066` n `235`; crypto_major avg `-0.4878` n `8`; equity avg `-0.6187` n `151`; fx avg `-0.0186` n `6`; index avg `-0.0918` n `26`; metal avg `-0.1459` n `20`; unknown avg `0.2814` n `1055`
- 4h: commodity avg `0.2903` n `13`; crypto_alt avg `-0.7834` n `235`; crypto_major avg `-0.5346` n `8`; equity avg `-0.9726` n `151`; fx avg `-0.0656` n `6`; index avg `-0.1327` n `26`; metal avg `-0.1607` n `20`; unknown avg `0.4989` n `1031`
- 24h: commodity avg `-0.1702` n `13`; crypto_alt avg `1.8831` n `235`; crypto_major avg `1.3851` n `8`; equity avg `-1.1378` n `151`; fx avg `-0.1116` n `6`; index avg `-0.1151` n `26`; metal avg `-0.0504` n `20`; unknown avg `0.0693` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
