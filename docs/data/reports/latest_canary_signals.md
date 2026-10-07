# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T15:52:30.839384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.055` n `13`; crypto_alt avg `0.3226` n `235`; crypto_major avg `0.0303` n `8`; equity avg `0.0685` n `150`; fx avg `-0.0082` n `6`; index avg `0.0131` n `26`; metal avg `-0.0539` n `20`; unknown avg `1.9871` n `1076`
- 1h: commodity avg `-0.1564` n `13`; crypto_alt avg `0.6395` n `235`; crypto_major avg `0.345` n `8`; equity avg `0.2619` n `150`; fx avg `-0.0121` n `6`; index avg `0.095` n `26`; metal avg `0.0417` n `20`; unknown avg `3.3974` n `1074`
- 4h: commodity avg `-0.0897` n `13`; crypto_alt avg `-0.0039` n `235`; crypto_major avg `-0.2418` n `8`; equity avg `0.191` n `150`; fx avg `-0.021` n `6`; index avg `0.0284` n `26`; metal avg `-0.0962` n `20`; unknown avg `0.1683` n `1022`
- 24h: commodity avg `1.0156` n `13`; crypto_alt avg `-5.4737` n `235`; crypto_major avg `-3.8024` n `8`; equity avg `-1.8417` n `150`; fx avg `-0.1841` n `6`; index avg `-0.3588` n `26`; metal avg `-0.6461` n `20`; unknown avg `16.2969` n `988`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1446`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1406`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0837`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0777`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0775`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.074`, n `669`, weak_sample_signal
