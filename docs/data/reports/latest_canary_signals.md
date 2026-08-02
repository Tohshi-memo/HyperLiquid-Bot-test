# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T07:24:56.270187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.1343` n `230`; crypto_major avg `0.0613` n `8`; equity avg `0.0162` n `102`; fx avg `-0.014` n `6`; index avg `0.0086` n `25`; metal avg `0.0134` n `20`; unknown avg `0.0113` n `782`
- 1h: commodity avg `-0.027` n `12`; crypto_alt avg `0.0808` n `230`; crypto_major avg `0.0669` n `8`; equity avg `-0.0404` n `102`; fx avg `-0.0295` n `6`; index avg `0.0007` n `25`; metal avg `0.0192` n `20`; unknown avg `0.0079` n `782`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `0.2554` n `230`; crypto_major avg `0.0531` n `8`; equity avg `0.0485` n `102`; fx avg `-0.0773` n `6`; index avg `0.0696` n `25`; metal avg `0.0631` n `20`; unknown avg `0.4021` n `766`
- 24h: commodity avg `-1.1138` n `12`; crypto_alt avg `0.4037` n `230`; crypto_major avg `0.4879` n `8`; equity avg `0.8491` n `102`; fx avg `-0.1448` n `6`; index avg `0.2726` n `25`; metal avg `0.264` n `20`; unknown avg `0.3652` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
