# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T03:52:32.360543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.0011` n `230`; crypto_major avg `-0.0251` n `8`; equity avg `-0.0713` n `108`; fx avg `-0.002` n `6`; index avg `0.0024` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.0762` n `782`
- 1h: commodity avg `-0.103` n `12`; crypto_alt avg `0.0131` n `230`; crypto_major avg `-0.0423` n `8`; equity avg `-0.2527` n `108`; fx avg `-0.0265` n `6`; index avg `-0.0325` n `25`; metal avg `-0.1415` n `20`; unknown avg `-0.0422` n `782`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.2167` n `230`; crypto_major avg `-0.6413` n `8`; equity avg `-0.1844` n `108`; fx avg `-0.0472` n `6`; index avg `-0.126` n `25`; metal avg `-0.075` n `20`; unknown avg `-0.2308` n `782`
- 24h: commodity avg `0.0658` n `12`; crypto_alt avg `0.0959` n `230`; crypto_major avg `-0.0896` n `8`; equity avg `-1.9335` n `108`; fx avg `-0.0013` n `6`; index avg `-0.3675` n `25`; metal avg `0.5182` n `20`; unknown avg `0.8845` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
