# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T17:37:27.931704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.0696` n `238`; crypto_major avg `0.0503` n `8`; equity avg `0.0006` n `156`; fx avg `0.0032` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.2022` n `1262`
- 1h: commodity avg `0.0098` n `13`; crypto_alt avg `-0.3676` n `238`; crypto_major avg `-0.0234` n `8`; equity avg `0.0222` n `156`; fx avg `0.0049` n `6`; index avg `-0.0012` n `27`; metal avg `-0.0027` n `20`; unknown avg `-0.4777` n `1256`
- 4h: commodity avg `-0.0762` n `13`; crypto_alt avg `0.5962` n `238`; crypto_major avg `0.198` n `8`; equity avg `0.1407` n `156`; fx avg `0.002` n `6`; index avg `0.0093` n `27`; metal avg `0.0271` n `20`; unknown avg `165.2403` n `1236`
- 24h: commodity avg `-0.4975` n `13`; crypto_alt avg `1.1077` n `238`; crypto_major avg `0.0244` n `8`; equity avg `1.1706` n `156`; fx avg `0.004` n `6`; index avg `0.0345` n `27`; metal avg `0.1108` n `20`; unknown avg `1.8639` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
