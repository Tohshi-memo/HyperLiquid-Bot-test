# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T08:54:57.610671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `13`; crypto_alt avg `0.1864` n `239`; crypto_major avg `0.0911` n `8`; equity avg `-0.0898` n `164`; fx avg `-0.0078` n `6`; index avg `-0.0084` n `27`; metal avg `0.016` n `20`; unknown avg `0.2169` n `1266`
- 1h: commodity avg `-0.0085` n `13`; crypto_alt avg `0.2222` n `239`; crypto_major avg `0.0641` n `8`; equity avg `0.1471` n `164`; fx avg `0.0161` n `6`; index avg `0.0283` n `27`; metal avg `0.0599` n `20`; unknown avg `81.4539` n `1232`
- 4h: commodity avg `-0.0263` n `13`; crypto_alt avg `0.2866` n `239`; crypto_major avg `0.3846` n `8`; equity avg `1.1966` n `164`; fx avg `0.0571` n `6`; index avg `0.1963` n `27`; metal avg `0.1176` n `20`; unknown avg `48.5265` n `1202`
- 24h: commodity avg `0.2966` n `13`; crypto_alt avg `0.1334` n `239`; crypto_major avg `-0.6656` n `8`; equity avg `0.2223` n `164`; fx avg `0.0558` n `6`; index avg `0.1691` n `27`; metal avg `-0.0995` n `20`; unknown avg `3.7756` n `1149`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
