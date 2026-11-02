# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T20:18:19.779069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `0.0842` n `239`; crypto_major avg `-0.0038` n `8`; equity avg `-0.1616` n `157`; fx avg `-0.003` n `6`; index avg `-0.0294` n `27`; metal avg `-0.0273` n `20`; unknown avg `18.5691` n `1262`
- 1h: commodity avg `-0.0415` n `13`; crypto_alt avg `0.2226` n `239`; crypto_major avg `0.2271` n `8`; equity avg `0.0106` n `157`; fx avg `-0.0032` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0298` n `20`; unknown avg `21.0373` n `1236`
- 4h: commodity avg `-0.2282` n `13`; crypto_alt avg `-1.1308` n `239`; crypto_major avg `-0.8` n `8`; equity avg `-2.0799` n `157`; fx avg `0.0043` n `6`; index avg `-0.2215` n `27`; metal avg `-0.2196` n `20`; unknown avg `20.0993` n `1170`
- 24h: commodity avg `-1.3799` n `13`; crypto_alt avg `-2.46` n `238`; crypto_major avg `-1.164` n `8`; equity avg `-2.5183` n `157`; fx avg `0.2715` n `6`; index avg `0.0444` n `27`; metal avg `0.2183` n `20`; unknown avg `3.8394` n `1016`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
