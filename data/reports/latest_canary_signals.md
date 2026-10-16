# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T00:37:29.228529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `0.1705` n `236`; crypto_major avg `0.1454` n `8`; equity avg `0.338` n `151`; fx avg `0.0292` n `6`; index avg `0.0624` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.1389` n `1136`
- 1h: commodity avg `0.0276` n `13`; crypto_alt avg `0.4292` n `236`; crypto_major avg `0.1921` n `8`; equity avg `-0.2842` n `151`; fx avg `0.0424` n `6`; index avg `-0.038` n `26`; metal avg `-0.0743` n `20`; unknown avg `1.1015` n `1128`
- 4h: commodity avg `-0.068` n `13`; crypto_alt avg `-0.0807` n `236`; crypto_major avg `-0.3544` n `8`; equity avg `-0.7664` n `151`; fx avg `0.0206` n `6`; index avg `-0.1394` n `26`; metal avg `-0.1429` n `20`; unknown avg `-0.0365` n `1090`
- 24h: commodity avg `-0.1688` n `13`; crypto_alt avg `0.7772` n `236`; crypto_major avg `0.4641` n `8`; equity avg `0.7436` n `151`; fx avg `0.0584` n `6`; index avg `0.1055` n `26`; metal avg `0.1898` n `20`; unknown avg `25.0798` n `910`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0943`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0868`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0626`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0569`, n `666`, weak_sample_signal
