# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T09:37:32.331971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1218` n `12`; crypto_alt avg `0.1069` n `234`; crypto_major avg `0.0811` n `8`; equity avg `0.0477` n `137`; fx avg `-0.0054` n `6`; index avg `0.0116` n `27`; metal avg `0.0196` n `20`; unknown avg `-0.1105` n `919`
- 1h: commodity avg `-0.0565` n `12`; crypto_alt avg `0.4933` n `234`; crypto_major avg `0.5243` n `8`; equity avg `0.1642` n `137`; fx avg `0.0069` n `6`; index avg `0.0201` n `27`; metal avg `0.0523` n `20`; unknown avg `0.0055` n `917`
- 4h: commodity avg `-0.0577` n `12`; crypto_alt avg `-0.3264` n `234`; crypto_major avg `-0.1335` n `8`; equity avg `0.2863` n `137`; fx avg `-0.0213` n `6`; index avg `0.0567` n `27`; metal avg `-0.0628` n `20`; unknown avg `6.1722` n `881`
- 24h: commodity avg `-0.0078` n `12`; crypto_alt avg `-3.0451` n `234`; crypto_major avg `-2.7168` n `8`; equity avg `0.2525` n `137`; fx avg `0.0936` n `6`; index avg `0.1495` n `27`; metal avg `0.5477` n `20`; unknown avg `18892.7969` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
