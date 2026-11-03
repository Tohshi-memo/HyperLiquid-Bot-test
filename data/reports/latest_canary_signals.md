# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T02:29:24.286243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `13`; crypto_alt avg `0.0362` n `239`; crypto_major avg `0.1265` n `8`; equity avg `-0.0822` n `157`; fx avg `-0.0104` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.6539` n `1260`
- 1h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.4518` n `239`; crypto_major avg `-0.2801` n `8`; equity avg `0.0297` n `157`; fx avg `-0.0406` n `6`; index avg `-0.0233` n `27`; metal avg `-0.1074` n `20`; unknown avg `0.0919` n `1256`
- 4h: commodity avg `0.0775` n `13`; crypto_alt avg `-0.5098` n `239`; crypto_major avg `-0.0208` n `8`; equity avg `0.3673` n `157`; fx avg `-0.0824` n `6`; index avg `0.0621` n `27`; metal avg `-0.0851` n `20`; unknown avg `-0.4116` n `1246`
- 24h: commodity avg `-1.1055` n `13`; crypto_alt avg `-3.2173` n `238`; crypto_major avg `-1.9198` n `8`; equity avg `-3.1544` n `157`; fx avg `0.0327` n `6`; index avg `-0.1689` n `27`; metal avg `0.0208` n `20`; unknown avg `12.5273` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
