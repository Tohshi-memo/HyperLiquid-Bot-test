# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T11:07:27.065892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `13`; crypto_alt avg `-0.3771` n `235`; crypto_major avg `-0.19` n `8`; equity avg `-0.2389` n `151`; fx avg `-0.0066` n `6`; index avg `-0.0299` n `26`; metal avg `-0.0164` n `20`; unknown avg `-0.0556` n `1115`
- 1h: commodity avg `0.0973` n `13`; crypto_alt avg `-0.4072` n `235`; crypto_major avg `-0.1723` n `8`; equity avg `-0.2555` n `151`; fx avg `-0.0119` n `6`; index avg `-0.0507` n `26`; metal avg `-0.0228` n `20`; unknown avg `-0.1958` n `1115`
- 4h: commodity avg `0.3347` n `13`; crypto_alt avg `-1.048` n `235`; crypto_major avg `-0.8571` n `8`; equity avg `-0.6345` n `151`; fx avg `-0.0455` n `6`; index avg `-0.1117` n `26`; metal avg `-0.0737` n `20`; unknown avg `0.3219` n `981`
- 24h: commodity avg `-0.0146` n `13`; crypto_alt avg `1.7608` n `235`; crypto_major avg `1.1463` n `8`; equity avg `-1.2825` n `151`; fx avg `-0.1318` n `6`; index avg `-0.1726` n `26`; metal avg `0.0243` n `20`; unknown avg `0.6648` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2313`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
