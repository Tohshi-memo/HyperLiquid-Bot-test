# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T04:37:31.308973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `13`; crypto_alt avg `0.5894` n `235`; crypto_major avg `0.4572` n `8`; equity avg `0.2065` n `151`; fx avg `0.0018` n `6`; index avg `0.0362` n `26`; metal avg `0.006` n `20`; unknown avg `0.0808` n `1107`
- 1h: commodity avg `0.021` n `13`; crypto_alt avg `0.4162` n `235`; crypto_major avg `0.4098` n `8`; equity avg `0.0352` n `151`; fx avg `0.018` n `6`; index avg `0.0055` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.2426` n `1099`
- 4h: commodity avg `-0.0265` n `13`; crypto_alt avg `0.6038` n `235`; crypto_major avg `0.5067` n `8`; equity avg `-0.8148` n `151`; fx avg `-0.0414` n `6`; index avg `-0.0571` n `26`; metal avg `-0.0152` n `20`; unknown avg `0.1255` n `1071`
- 24h: commodity avg `-0.4659` n `13`; crypto_alt avg `3.3615` n `235`; crypto_major avg `1.6864` n `8`; equity avg `-0.1539` n `151`; fx avg `-0.0621` n `6`; index avg `0.0283` n `26`; metal avg `0.1414` n `20`; unknown avg `1.1079` n `902`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
