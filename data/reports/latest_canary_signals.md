# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T23:22:28.235768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `-0.1136` n `235`; crypto_major avg `-0.0979` n `8`; equity avg `-0.0056` n `150`; fx avg `-0.0007` n `6`; index avg `0.0011` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.2072` n `1117`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `-0.2351` n `235`; crypto_major avg `-0.0729` n `8`; equity avg `-0.0188` n `150`; fx avg `-0.0055` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0024` n `20`; unknown avg `3.6693` n `1115`
- 4h: commodity avg `0.1584` n `13`; crypto_alt avg `-0.0928` n `235`; crypto_major avg `-0.1375` n `8`; equity avg `0.0417` n `150`; fx avg `-0.0067` n `6`; index avg `0.0108` n `26`; metal avg `0.0123` n `20`; unknown avg `2.7641` n `1055`
- 24h: commodity avg `0.0467` n `13`; crypto_alt avg `1.8591` n `235`; crypto_major avg `0.6561` n `8`; equity avg `0.1786` n `150`; fx avg `-0.0107` n `6`; index avg `0.0188` n `26`; metal avg `0.0045` n `20`; unknown avg `0.1808` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
