# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T03:22:33.051092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0607` n `13`; crypto_alt avg `0.1473` n `239`; crypto_major avg `0.1141` n `8`; equity avg `0.0711` n `157`; fx avg `0.0131` n `6`; index avg `0.0513` n `27`; metal avg `-0.0244` n `20`; unknown avg `3.2539` n `1264`
- 1h: commodity avg `0.0589` n `13`; crypto_alt avg `-0.2107` n `239`; crypto_major avg `-0.2516` n `8`; equity avg `-0.2307` n `157`; fx avg `-0.0118` n `6`; index avg `0.0194` n `27`; metal avg `-0.1233` n `20`; unknown avg `2.8975` n `1256`
- 4h: commodity avg `0.1697` n `13`; crypto_alt avg `-0.5873` n `239`; crypto_major avg `-0.1312` n `8`; equity avg `-0.1657` n `157`; fx avg `-0.0799` n `6`; index avg `0.0201` n `27`; metal avg `-0.1986` n `20`; unknown avg `161.3533` n `1252`
- 24h: commodity avg `-0.9289` n `13`; crypto_alt avg `-3.4785` n `238`; crypto_major avg `-2.1753` n `8`; equity avg `-3.7163` n `157`; fx avg `-0.0345` n `6`; index avg `-0.1796` n `27`; metal avg `-0.0108` n `20`; unknown avg `14.1071` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
