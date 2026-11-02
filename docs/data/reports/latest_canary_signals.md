# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T16:22:33.664652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.22` n `13`; crypto_alt avg `-0.309` n `239`; crypto_major avg `-0.2545` n `8`; equity avg `-0.3449` n `156`; fx avg `0.001` n `6`; index avg `-0.0244` n `27`; metal avg `0.0372` n `20`; unknown avg `0.0591` n `1265`
- 1h: commodity avg `-0.1823` n `13`; crypto_alt avg `-0.5747` n `239`; crypto_major avg `-0.6442` n `8`; equity avg `-0.7174` n `156`; fx avg `-0.021` n `6`; index avg `-0.0798` n `27`; metal avg `0.0365` n `20`; unknown avg `0.5763` n `1251`
- 4h: commodity avg `-0.6867` n `13`; crypto_alt avg `-0.7926` n `238`; crypto_major avg `-0.7414` n `8`; equity avg `-1.5657` n `156`; fx avg `-0.0082` n `6`; index avg `-0.0064` n `27`; metal avg `0.379` n `20`; unknown avg `38.062` n `1253`
- 24h: commodity avg `-1.1113` n `13`; crypto_alt avg `-2.3567` n `238`; crypto_major avg `-1.0627` n `8`; equity avg `-0.7358` n `156`; fx avg `0.2591` n `6`; index avg `0.2176` n `27`; metal avg `0.4204` n `20`; unknown avg `7.836` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
