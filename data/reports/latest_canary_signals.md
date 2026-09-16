# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T04:37:27.932085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.009` n `234`; crypto_major avg `-0.0274` n `8`; equity avg `-0.1293` n `137`; fx avg `0.0093` n `6`; index avg `-0.0318` n `27`; metal avg `-0.0174` n `20`; unknown avg `2.3042` n `913`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `0.4559` n `234`; crypto_major avg `0.3184` n `8`; equity avg `0.1088` n `137`; fx avg `-0.0176` n `6`; index avg `0.0043` n `27`; metal avg `0.0248` n `20`; unknown avg `2.0728` n `911`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `0.1232` n `234`; crypto_major avg `0.3396` n `8`; equity avg `0.5167` n `137`; fx avg `-0.0201` n `6`; index avg `0.0426` n `27`; metal avg `0.3171` n `20`; unknown avg `1.5937` n `907`
- 24h: commodity avg `0.1364` n `12`; crypto_alt avg `-2.898` n `234`; crypto_major avg `-2.8673` n `8`; equity avg `-0.3198` n `137`; fx avg `0.2191` n `6`; index avg `0.0354` n `27`; metal avg `0.3907` n `20`; unknown avg `18796.136` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
