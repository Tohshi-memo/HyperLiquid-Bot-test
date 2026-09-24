# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T18:22:29.825947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `0.2522` n `234`; crypto_major avg `0.4335` n `8`; equity avg `0.1767` n `141`; fx avg `-0.0011` n `6`; index avg `0.0229` n `26`; metal avg `0.0486` n `20`; unknown avg `0.3446` n `941`
- 1h: commodity avg `-0.0901` n `12`; crypto_alt avg `-0.3254` n `234`; crypto_major avg `0.0325` n `8`; equity avg `-0.1937` n `141`; fx avg `0.0108` n `6`; index avg `-0.0356` n `26`; metal avg `0.0491` n `20`; unknown avg `4.8445` n `939`
- 4h: commodity avg `0.4974` n `12`; crypto_alt avg `0.5608` n `234`; crypto_major avg `0.7743` n `8`; equity avg `0.468` n `141`; fx avg `0.0067` n `6`; index avg `0.0465` n `26`; metal avg `0.0744` n `20`; unknown avg `10.899` n `881`
- 24h: commodity avg `1.0209` n `12`; crypto_alt avg `3.3717` n `234`; crypto_major avg `1.8263` n `8`; equity avg `-0.6002` n `141`; fx avg `0.042` n `6`; index avg `-0.1246` n `26`; metal avg `-0.0902` n `20`; unknown avg `265.3664` n `831`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
