# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T13:07:27.689922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.0724` n `233`; crypto_major avg `0.2282` n `8`; equity avg `-0.0568` n `136`; fx avg `0.0017` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0319` n `20`; unknown avg `2.7274` n `906`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `0.5558` n `233`; crypto_major avg `0.6287` n `8`; equity avg `0.0142` n `136`; fx avg `-0.0102` n `6`; index avg `0.0224` n `27`; metal avg `0.0961` n `20`; unknown avg `4.8852` n `900`
- 4h: commodity avg `-0.1785` n `12`; crypto_alt avg `0.3909` n `233`; crypto_major avg `0.8058` n `8`; equity avg `0.6464` n `136`; fx avg `-0.0288` n `6`; index avg `0.1806` n `27`; metal avg `0.2777` n `20`; unknown avg `4.8855` n `898`
- 24h: commodity avg `-0.2691` n `12`; crypto_alt avg `0.0786` n `233`; crypto_major avg `0.5326` n `8`; equity avg `1.1136` n `136`; fx avg `0.1636` n `6`; index avg `0.2078` n `27`; metal avg `0.2069` n `20`; unknown avg `0.0874` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
