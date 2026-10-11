# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T20:22:29.775613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `13`; crypto_alt avg `-0.0428` n `235`; crypto_major avg `0.0082` n `8`; equity avg `0.0039` n `150`; fx avg `-0.0005` n `6`; index avg `-0.0016` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.1756` n `1134`
- 1h: commodity avg `0.0537` n `13`; crypto_alt avg `0.0808` n `235`; crypto_major avg `-0.0884` n `8`; equity avg `0.0136` n `150`; fx avg `0.0064` n `6`; index avg `0.001` n `26`; metal avg `0.0155` n `20`; unknown avg `-0.1949` n `1118`
- 4h: commodity avg `0.0914` n `13`; crypto_alt avg `-0.0688` n `235`; crypto_major avg `-0.2741` n `8`; equity avg `0.0622` n `150`; fx avg `0.0108` n `6`; index avg `0.0153` n `26`; metal avg `0.0433` n `20`; unknown avg `0.1637` n `1100`
- 24h: commodity avg `0.3365` n `13`; crypto_alt avg `1.9674` n `235`; crypto_major avg `0.7116` n `8`; equity avg `0.2828` n `150`; fx avg `0.0265` n `6`; index avg `0.0348` n `26`; metal avg `0.0934` n `20`; unknown avg `1.0177` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
