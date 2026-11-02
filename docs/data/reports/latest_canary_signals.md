# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T14:22:41.555430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0554` n `13`; crypto_alt avg `-0.3001` n `239`; crypto_major avg `-0.2017` n `8`; equity avg `-0.13` n `156`; fx avg `0.0024` n `6`; index avg `0.0003` n `27`; metal avg `-0.0487` n `20`; unknown avg `243.5096` n `1265`
- 1h: commodity avg `-0.3199` n `13`; crypto_alt avg `0.2488` n `239`; crypto_major avg `0.3246` n `8`; equity avg `0.3141` n `156`; fx avg `-0.0191` n `6`; index avg `0.0626` n `27`; metal avg `0.2356` n `20`; unknown avg `0.2911` n `1257`
- 4h: commodity avg `-0.3633` n `13`; crypto_alt avg `0.0786` n `238`; crypto_major avg `-0.0177` n `8`; equity avg `-0.5897` n `156`; fx avg `-0.0079` n `6`; index avg `0.0113` n `27`; metal avg `0.1598` n `20`; unknown avg `3.8514` n `1250`
- 24h: commodity avg `-0.8356` n `13`; crypto_alt avg `-2.3716` n `238`; crypto_major avg `-0.7063` n `8`; equity avg `0.3888` n `156`; fx avg `0.2751` n `6`; index avg `0.2861` n `27`; metal avg `0.1857` n `20`; unknown avg `7.3044` n `1075`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
