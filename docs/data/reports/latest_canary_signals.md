# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T23:07:31.360932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.0704` n `239`; crypto_major avg `-0.0447` n `8`; equity avg `0.103` n `157`; fx avg `-0.0166` n `6`; index avg `0.017` n `27`; metal avg `-0.0112` n `20`; unknown avg `-0.1481` n `1250`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `-0.2764` n `239`; crypto_major avg `-0.1536` n `8`; equity avg `-0.0675` n `157`; fx avg `-0.0336` n `6`; index avg `-0.033` n `27`; metal avg `-0.0034` n `20`; unknown avg `-0.07` n `1248`
- 4h: commodity avg `-0.0202` n `13`; crypto_alt avg `0.2382` n `239`; crypto_major avg `0.3643` n `8`; equity avg `-0.5039` n `157`; fx avg `-0.0203` n `6`; index avg `-0.1281` n `27`; metal avg `-0.0505` n `20`; unknown avg `14.0234` n `1142`
- 24h: commodity avg `-1.3156` n `13`; crypto_alt avg `-2.61` n `238`; crypto_major avg `-1.2116` n `8`; equity avg `-2.6243` n `157`; fx avg `0.2237` n `6`; index avg `0.0164` n `27`; metal avg `0.1953` n `20`; unknown avg `9.689` n `998`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
