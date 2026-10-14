# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T00:35:28.742087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `13`; crypto_alt avg `0.2361` n `235`; crypto_major avg `0.3017` n `8`; equity avg `0.2153` n `151`; fx avg `0.0531` n `6`; index avg `0.0398` n `26`; metal avg `-0.0208` n `20`; unknown avg `0.3762` n `1135`
- 1h: commodity avg `0.1383` n `13`; crypto_alt avg `0.6418` n `235`; crypto_major avg `0.599` n `8`; equity avg `0.3867` n `151`; fx avg `0.0212` n `6`; index avg `0.0716` n `26`; metal avg `0.0059` n `20`; unknown avg `0.6411` n `1127`
- 4h: commodity avg `0.0458` n `13`; crypto_alt avg `0.4367` n `235`; crypto_major avg `0.3996` n `8`; equity avg `0.3929` n `151`; fx avg `0.0178` n `6`; index avg `0.058` n `26`; metal avg `-0.017` n `20`; unknown avg `2.0819` n `1065`
- 24h: commodity avg `0.9226` n `13`; crypto_alt avg `2.615` n `235`; crypto_major avg `2.638` n `8`; equity avg `0.6595` n `151`; fx avg `0.2119` n `6`; index avg `0.0569` n `26`; metal avg `-0.2226` n `20`; unknown avg `0.8582` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.156`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1418`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0959`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `666`, weak_sample_signal
