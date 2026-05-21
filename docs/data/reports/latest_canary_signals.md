# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T07:22:15.709309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.066` n `12`; crypto_alt avg `-0.1403` n `228`; crypto_major avg `0.0198` n `8`; equity avg `-0.1334` n `66`; fx avg `-0.0466` n `6`; index avg `-0.0638` n `23`; metal avg `-0.092` n `18`; unknown avg `-0.0246` n `385`
- 1h: commodity avg `0.3442` n `12`; crypto_alt avg `-0.0775` n `228`; crypto_major avg `-0.0529` n `8`; equity avg `-0.5353` n `66`; fx avg `-0.0772` n `6`; index avg `-0.2337` n `23`; metal avg `-0.4658` n `18`; unknown avg `-0.32` n `385`
- 4h: commodity avg `0.2414` n `12`; crypto_alt avg `-0.4197` n `228`; crypto_major avg `-0.1538` n `8`; equity avg `-0.4716` n `66`; fx avg `-0.0352` n `6`; index avg `-0.1735` n `23`; metal avg `-0.5604` n `18`; unknown avg `-0.0815` n `374`
- 24h: commodity avg `-1.6626` n `12`; crypto_alt avg `2.09` n `228`; crypto_major avg `2.832` n `8`; equity avg `1.2569` n `66`; fx avg `0.033` n `6`; index avg `1.2523` n `23`; metal avg `0.0508` n `18`; unknown avg `4.6727` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
