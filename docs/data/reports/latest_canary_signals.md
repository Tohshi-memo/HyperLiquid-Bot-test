# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T08:37:34.814916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0448` n `12`; crypto_alt avg `-0.1218` n `232`; crypto_major avg `-0.2365` n `8`; equity avg `-0.0189` n `132`; fx avg `-0.0017` n `6`; index avg `0.0007` n `26`; metal avg `-0.004` n `20`; unknown avg `0.1557` n `792`
- 1h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.1973` n `232`; crypto_major avg `-0.6001` n `8`; equity avg `-0.2557` n `132`; fx avg `-0.022` n `6`; index avg `-0.0215` n `26`; metal avg `-0.0497` n `20`; unknown avg `-0.0095` n `790`
- 4h: commodity avg `-0.0878` n `12`; crypto_alt avg `-0.0068` n `232`; crypto_major avg `-0.495` n `8`; equity avg `-0.0655` n `132`; fx avg `-0.1038` n `6`; index avg `0.0078` n `26`; metal avg `0.1427` n `20`; unknown avg `0.1585` n `770`
- 24h: commodity avg `0.4866` n `12`; crypto_alt avg `0.1533` n `232`; crypto_major avg `-1.3332` n `8`; equity avg `-1.6407` n `130`; fx avg `-0.2007` n `6`; index avg `-0.2571` n `26`; metal avg `-0.3942` n `20`; unknown avg `-0.4916` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
