# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T04:07:29.804277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `13`; crypto_alt avg `-0.3644` n `238`; crypto_major avg `-0.3511` n `8`; equity avg `-0.0931` n `156`; fx avg `-0.0206` n `6`; index avg `-0.0075` n `27`; metal avg `-0.0422` n `20`; unknown avg `-0.1404` n `1248`
- 1h: commodity avg `-0.0347` n `13`; crypto_alt avg `0.8139` n `238`; crypto_major avg `0.8508` n `8`; equity avg `0.3936` n `156`; fx avg `-0.0248` n `6`; index avg `0.0574` n `27`; metal avg `-0.0377` n `20`; unknown avg `0.4052` n `1238`
- 4h: commodity avg `0.1218` n `13`; crypto_alt avg `-0.4794` n `238`; crypto_major avg `0.7638` n `8`; equity avg `-0.1931` n `156`; fx avg `-0.054` n `6`; index avg `-0.1167` n `27`; metal avg `-0.2823` n `20`; unknown avg `5.9625` n `1234`
- 24h: commodity avg `-0.0589` n `13`; crypto_alt avg `-4.1523` n `238`; crypto_major avg `-0.0644` n `8`; equity avg `-2.495` n `155`; fx avg `0.1176` n `6`; index avg `-0.2624` n `27`; metal avg `-0.6789` n `20`; unknown avg `28.5419` n `974`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
