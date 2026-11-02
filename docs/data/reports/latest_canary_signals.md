# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T15:22:33.474099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `0.0738` n `239`; crypto_major avg `0.0398` n `8`; equity avg `0.3993` n `156`; fx avg `0.0127` n `6`; index avg `0.0758` n `27`; metal avg `0.0492` n `20`; unknown avg `15.642` n `1265`
- 1h: commodity avg `-0.1823` n `13`; crypto_alt avg `0.1513` n `239`; crypto_major avg `0.1491` n `8`; equity avg `-0.3904` n `156`; fx avg `0.0238` n `6`; index avg `0.051` n `27`; metal avg `0.1905` n `20`; unknown avg `15.6308` n `1259`
- 4h: commodity avg `-0.4135` n `13`; crypto_alt avg `0.1568` n `238`; crypto_major avg `0.1915` n `8`; equity avg `-0.8699` n `156`; fx avg `0.0252` n `6`; index avg `0.0613` n `27`; metal avg `0.3176` n `20`; unknown avg `74.4979` n `1252`
- 24h: commodity avg `-1.0049` n `13`; crypto_alt avg `-2.0646` n `238`; crypto_major avg `-0.492` n `8`; equity avg `-0.0004` n `156`; fx avg `0.2975` n `6`; index avg `0.3089` n `27`; metal avg `0.3824` n `20`; unknown avg `7.6719` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
